
import api
import pytest

@pytest.mark.little_test
@pytest.mark.func
def test_func():
    with pytest.raises(AttributeError):
        class obj:
            def name(self):
                pass
        api.func(obj)

def test_add():
    with pytest.raises(TypeError):
        api.add(n=2.3)

@pytest.mark.little_test
def test_cmp():
    with pytest.raises(ValueError):
        api.cmp(3, 4)