# Security

> Bootstrap 2026-11-09. Ajanlar her plan ve incelemede bu kurallara uyar.

## Secrets
- Secrets never enter the repo, specs, prompts, or chat. `.env` is gitignored; provide `.env.example`.
- Agents never print secret values, even when debugging.
- Bugün gizli bilgi yok. İleride `SECRET_KEY` veya veritabanı şifresi yalnızca ortam
  değişkeninden okunur; o gün `.env.example` eklenir.

## Input & output
- Kullanıcıdan gelen her değer HTML'e **kaçışlı** basılır: Jinja otomatik kaçışı açık; kullanıcı
  verisi içeren yerde `|safe` ve metin birleştirerek HTML üretmek yasak.
- Form alanları `web` katmanında doğrulanır: tarih biçimi, personel ID'si, neden uzunluğu.
- Hata mesajlarında stack trace, iç kod veya dahili bilgi yok (`docs/conventions.md`).
- Debug modu varsayılan **kapalı**; yalnızca `FLASK_DEBUG=1` ile açılır.
- ⚠ **Kod uyumsuz (öncelik 1, `/change`):**
  - **S-1 XSS:** `reason` alanı `/requests` sayfasında kaçışsız basılıyor (`body|safe`).
  - **S-2 Debug:** `app.run(debug=True)` sabit kodlu — Werkzeug debugger uzaktan kod çalıştırır.

## AuthN / AuthZ
- **Bugün kimlik doğrulama yok — bilinçli kabul edilmiş risk.** Koşul: uygulama yalnızca iç ağda,
  İK kullanımında çalışır; internete açılmaz; `127.0.0.1` veya iç ağ adresine bağlanır.
- CSRF koruması kimlik doğrulamayla birlikte gelir; o spec'te **zorunlu** maddedir.

## Dependencies
- Her yeni paket plan aşamasında insan onayı alır: lisans, bakım durumu, bilinen açıklar.
- `pip-audit` şimdilik check'te yok (ağ gerektirir); bağımlılık sayısı artınca yeniden
  değerlendirilir.

## Review lens
Security is a mandatory dimension of every independent review (see `prompts/review.md`), not a
separate afterthought phase.
