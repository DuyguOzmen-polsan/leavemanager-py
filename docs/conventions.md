# Conventions

> Bootstrap 2026-11-09. Buradaki her kural araçla zorlanır ya da incelemede kontrol edilir.

## Language
<!-- Set at bootstrap (step 0) and mirrored in AGENTS.md. Changing it later is allowed — edit both
     places; existing documents are not translated retroactively. -->
- Chat language (interviews, sessions): Turkish
- Document language (docs/, specs, plans, ADRs, review and verify reports): Turkish
- Always English (protocol, not prose): ANEW core files, template headings and field labels,
  `Status:` values (Draft / Approved / In progress / Shipped), `Approved by / on:`, `Source:`.
- Code identifiers, branch names, commit messages: English. Code comments and user-facing texts:
  Turkish (ruff allows `ı`/`İ` via `allowed-confusables`).
- Agent messages (handoff summaries, refusals, `Next:` lines): chat language; command names, file
  paths and protocol fields verbatim.

## Language & framework versions
- Python `>=3.12` (`pyproject.toml`); yerelde Windows'ta `py` başlatıcısı (3.15). `python` komutu
  bu makinede yok — araçlar her zaman `./scripts/python` ile `.venv` üzerinden çalışır.
- Flask `~=3.1`; geliştirme: pytest `~=9.2`, ruff `~=0.17.4` (`[dependency-groups] dev`).
- Kurulum: `py -m venv .venv` → `./scripts/python -m pip install -e . --group dev`.

## Naming
- Kod adları İngilizce, PEP 8 (`Employee`, `LeaveRequest`, `EmployeeNotFound`). Türkçe terim ↔ kod
  adı eşleşmesi `docs/domain.md` sözlüğündedir.
- Durum değerleri veride `Beklemede` / `Onaylandi` / `Reddedildi`; kodda bir `Enum` üzerinden
  kullanılır, metin karşılaştırması yapılmaz.
- Testler: `tests/test_<konu>.py`; iş kuralı testlerinin adında kural numarası geçer
  (`test_br2_...`).

## Error handling
- `domain` tipli hatalar fırlatır; hepsi `LeaveError`'dan türer (ör. `EmployeeNotFound`).
- `web` yalnızca bu hataları yakalar → Türkçe kullanıcı mesajı + doğru HTTP kodu.
- `except Exception` ile hata yutmak yasak (ruff `BLE`). Beklenmeyen hata → 500, genel sayfa,
  ayrıntı loglanır.
- Kullanıcıya asla gösterilmez: stack trace, iç hata kodu, dahili telefon/IT bilgisi.
- ⚠ **Kod uyumsuz (`/change`):** `create_request` ve `/new` route'u hataları yutuyor; bakiye
  mesajı "ERR-412 NullReferenceGibi … dahili 4127" iç bilgi sızdırıyor.

## Data rules
- Tarihler `datetime.date`; saat bilgisi yok. "Bugün" parametre olarak verilir (Y2).
- Gün sayıları `int`. ID'leri `repository` üretir.

## Enforced by tooling
- `ruff check`: `E4,E7,E9,F,I,B,UP,BLE,RUF` (import sırası, kör `except`, modern sözdizimi…).
- `ruff format --check`: biçim tartışılmaz.
- **Geçici muafiyet:** `app.py` bugünkü ihlalleri için `per-file-ignores` ve format `exclude`
  altında (`pyproject.toml`). Refactor spec'i bu muafiyetleri kaldırır; yeni koda muafiyet yok.
- Mimari kurallar Y1–Y5: refactor sonrası `tests/test_architecture.py`.
