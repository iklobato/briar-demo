import importlib


def test_secret_key_comes_from_environment(monkeypatch):
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "test-value")
    import expenses.config as config

    config = importlib.reload(config)
    assert config.aws_secret_access_key == "test-value"


def test_secret_key_is_none_when_unset(monkeypatch):
    monkeypatch.delenv("AWS_SECRET_ACCESS_KEY", raising=False)
    import expenses.config as config

    config = importlib.reload(config)
    assert config.aws_secret_access_key is None
