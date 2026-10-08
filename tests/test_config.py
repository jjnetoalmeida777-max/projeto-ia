from src.config import get_env


def test_get_env_returns_value(monkeypatch):
    monkeypatch.setenv("TEST_VAR", "valor")
    assert get_env("TEST_VAR") == "valor"


def test_get_env_returns_none_when_missing():
    assert get_env("VAR_INEXISTENTE") is None


def test_get_env_raises_when_required(monkeypatch):
    monkeypatch.delenv("VAR_INEXISTENTE", raising=False)

    try:
        get_env("VAR_INEXISTENTE", required=True)
    except RuntimeError as exc:
        assert "VAR_INEXISTENTE" in str(exc)
    else:
        raise AssertionError("Era esperado RuntimeError")
