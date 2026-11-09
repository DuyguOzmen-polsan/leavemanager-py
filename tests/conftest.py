from datetime import datetime

import pytest

import app as app_module

# Testlerde "bugün" sabittir (docs/testing.md). Refactor sonrası parametre olarak verilir (Y2).
FIXED_NOW = datetime(2026, 11, 9, 12, 0)


class _FixedDatetime(datetime):
    @classmethod
    def now(cls, tz=None):
        return FIXED_NOW


@pytest.fixture(autouse=True)
def known_state(monkeypatch):
    """Her test bilinen durumdan başlar: seed verisi ve sabit tarih."""
    app_module.seed()
    monkeypatch.setattr(app_module, "datetime", _FixedDatetime)


@pytest.fixture
def client():
    return app_module.app.test_client()
