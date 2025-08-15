def test_true():
    assert True

def test_load_config():
    config = load_config()
    assert config is not None
    assert "setting1" in config
    assert "setting2" in config
