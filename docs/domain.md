# Domain

> Bootstrap 2026-11-09. Kod, spec ve sohbette aynı kelime aynı anlamı taşır.
> Kod adları İngilizcedir (`docs/conventions.md`); eşleşme "Code" sütunundadır.

## Ubiquitous language

| Term | Meaning | Notes / not to be confused with |
|---|---|---|
| Personel (`Employee`) | İzin hakkı olan çalışan: ad, birim, işe giriş tarihi | Kullanıcı değildir — uygulamayı İK kullanır |
| Birim (`department`) | Personelin departmanı (IT, Muhasebe, IK, Satis) | |
| İşe giriş tarihi (`hire_date`) | Kıdemin başladığı gün | |
| Kıdem (`seniority_years`) | Tamamlanmış hizmet yılı (BR-2) | Yıl farkı değildir |
| Hak edilen izin (`entitlement`) | Kıdeme göre yıllık izin günü (BR-1) | |
| İzin talebi (`LeaveRequest`) | Başlangıç, bitiş, neden ve durumdan oluşan kayıt | |
| Durum (`LeaveStatus`) | `Beklemede` / `Onaylandi` / `Reddedildi` — veride bu yazımla | Değerler veri; "yazım düzeltmesi" davranış değişikliğidir |
| İzin günü (`leave_days`) | Talep aralığındaki hafta içi gün sayısı (BR-3) | Takvim günü değildir |
| Kullanılan izin (`used_days`) | Takvim yılındaki `Onaylandi` taleplerin izin günleri (BR-7) | Bekleyenler dahil değil |
| Kalan bakiye (`remaining`) | Hak edilen izin − kullanılan izin | Talep kontrolünde bekleyenler de düşülür (BR-6) |

## Business rules
> ⚠ **Kod uyumsuz:** BR-1'in yorumu, BR-2…BR-8 ve S-1/S-2 (`docs/security.md`) bugünkü `app.py`'de
> farklı davranıyor. Her biri ayrı bir `/change` ile düzeltilir; **refactor'dan önce**, ki
> karakterizasyon testleri doğru davranışı sabitlesin.

- **BR-1 Hak edilen izin:** kıdem < 1 → 0 gün; 1–5 → 14; 6–15 → 20; 16 ve üstü → 26.
  (Kod doğru; "15 gün" diyen eski yorum yanlış.)
- **BR-2 Kıdem:** "bugün"e kadar tamamlanmış yıl sayısıdır; yıl dönümü günü dolar. 02.11.2024'te
  giren 02.11.2026'da 2, 01.11.2026'da 1 yıl kıdemlidir. 29 Şubat'ta girenlerin yıl dönümü artık
  olmayan yıllarda 1 Mart'tır.
- **BR-3 İzin günü:** başlangıç ve bitiş dahil aralıktaki pazartesi–cuma günleridir; cumartesi ve
  pazar sayılmaz. (Resmî tatiller: açık karar.)
- **BR-4 Bakiye kontrolü:** talep, `kalan < izin günü` ise reddedilir; kalan kadar izin istenebilir.
  Servis ve web aynı kuralı uygular.
- **BR-5 Bilinmeyen personel:** talep oluşturulmaz; `EmployeeNotFound` hatası, formda mesaj, HTTP 404.
- **BR-6 Bekleyenler:** yeni talep kontrolünde `hak − onaylanan − bekleyen < izin günü` ise
  reddedilir. Panodaki "Kalan" sütunu yalnızca onaylananları düşer.
- **BR-7 Dönem:** kullanılan izin takvim yılı bazında sayılır. (Yıl sonu devri: açık karar.)
- **BR-8 Tarih aralığı:** bitiş < başlangıç ise talep reddedilir, formda mesaj gösterilir.
  Geçmiş tarihli talepler serbesttir (İK geriye dönük giriş yapar).

## Key domain invariants
- Yeni talep her zaman `Beklemede` durumunda açılır.
- Bir talep, kayıtlı bir personele aittir.
- Kural hesapları "bugün"ü parametre olarak alır; sistem saatine doğrudan bakmaz (Y2).
