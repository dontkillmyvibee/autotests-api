import pytest

SYS_VERSION = "v1.2.0"

@pytest.mark.skipif(SYS_VERSION == "v1.3.0", reason=f"Тест не может быть запущен на этой версии {SYS_VERSION}")
def test_system_version_valid():
    ...

@pytest.mark.skipif(SYS_VERSION == "v1.2.0", reason=f"Тест не может быть запущен на этой версии {SYS_VERSION}")
def test_system_version_invalid():
    ...