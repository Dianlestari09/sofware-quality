try:
    import pytest  # type: ignore[reportMissingImports]
except Exception:
    # Minimal fallback so tests can run (or be linted) when pytest isn't installed.
    class _RaisesCtx:
        def __init__(self, exc_type):
            self.exc_type = exc_type

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            if exc_type is None:
                raise AssertionError(f"{self.exc_type.__name__} not raised")
            if not issubclass(exc_type, self.exc_type):
                # Propagate unexpected exceptions
                return False
            # Suppress the expected exception
            return True

    class _DummyPytest:
        @staticmethod
        def raises(exc_type):
            return _RaisesCtx(exc_type)

    pytest = _DummyPytest()
from calculator import add, divide

def test_add_basic():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
