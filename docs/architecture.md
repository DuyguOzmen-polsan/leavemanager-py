# Architecture

> Bootstrap 2026-11-09. Ajanlar planlamadan önce bu dosyayı okur.

## System overview
LeaveManager, İK personelinin çalışan izinlerini takip ettiği, iç ağda çalışan bir Flask web
uygulamasıdır (sunucuda üretilen HTML, JavaScript yok). Mimari stil: **katmanlı küçük monolit**
(`web → service → domain`, `service → repository`). Gerekçe: iş kuralları web'den bağımsız test
edilebilsin ve bellek içi depodan SQL'e geçiş yalnızca `repository` katmanını etkilesin.

**Bugünkü durum ≠ hedef.** Bugün tüm kod tek dosyada (`app.py`): veri (`Db`, `seed`), iş mantığı
(`LeaveService`, içinde HTML de var) ve route'lar (içinde iş kuralı da var) iç içe. Aşağıdaki
katmanlar **hedeftir**; geçiş bir refactor spec'i ile yapılır (`workflows/refactor.md`).

## Modules / components and ownership

| Module | Single responsibility | Owns |
|---|---|---|
| `domain` | İş kuralları (BR-1…BR-8, `docs/domain.md`): kıdem, hak edilen izin, izin günü, bakiye, talep doğrulama. Saf Python | Personel, İzin talebi, Durum kavramları |
| `repository` | Kalıcılık. Bugün bellek içi (`seed` verisi), ileride SQL — aynı arayüz | Personel ve talep kayıtları; ID üretimi |
| `service` | Kullanım senaryoları (talep oluştur, bakiye özeti); `domain` ile `repository`'yi birleştirir | — |
| `web` | Flask route'ları, form ayrıştırma ve doğrulama, HTML şablonları (durum rozeti dahil), hata → HTTP eşlemesi | — |

## Communication rules
- Yalnızca doğrudan fonksiyon çağrısı. Olay/mesaj altyapısı yok.
- Bağımlılık yönü tek: `web → service → domain` ve `service → repository`.
- "Bugün" (tarih) `web` katmanında bir kez alınır ve parametre olarak aşağı geçirilir.

## Forbidden dependencies (make them testable)
Refactor sonrası `tests/test_architecture.py` (stdlib `ast` ile import ve çağrı taraması) bunları
doğrular; test refactor spec'inin parçasıdır.
- **Y1:** `domain`; `flask`, `werkzeug`, `web`, `service`, `repository` import etmez.
- **Y2:** `domain` ve `service`; `datetime.now()`, `datetime.today()`, `date.today()` çağırmaz.
- **Y3:** `web`, `repository`'yi import etmez; her erişim `service` üzerinden.
- **Y4:** HTML yalnızca `web` içinde üretilir (`status_badge` dahil).
- **Y5:** `repository`; `web` ve `service` import etmez.

## Deliberately out of scope
Talep onay/red ekranı (yol haritasında) · kimlik doğrulama ve roller · resmî tatil takvimi
(açık karar) · yıl sonu izin devri (açık karar) · kalıcı veritabanı (refactor'dan sonra) ·
tarayıcı tabanlı e2e testleri.
