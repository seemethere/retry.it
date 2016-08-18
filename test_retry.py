import pytest

import retry

exception_message = 'testing exceptions'


def foo(bar):
    if bar < 0:
        raise ArithmeticError(exception_message)
    return bar


def test_success_criteria():
    foo_with_success = retry.retry(success=lambda x: x > 0)(foo)
    with pytest.raises(retry.MaximumRetriesExceeded):
        foo_with_success(0)


def test_exception_criteria():
    foo_with_exception = retry.retry(exceptions=(ArithmeticError,))(foo)
    with pytest.raises(ArithmeticError) as exc_info:
        foo_with_exception(-1)
    assert exception_message in str(exc_info.value)


def test_execution():
    foo_with_both = retry.retry(
        exceptions=(ArithmeticError,), success=lambda x: x > 0)(foo)
    assert foo_with_both(1) == 1


def test_invalid_parameters():
    with pytest.raises(TypeError):
        retry.retry(exceptions=None, success=None)(foo)


def test_timeout():
    foo_with_timeout = retry.retry(
        success=lambda x: x > 0, timeout=5, interval=1)(foo)
    with pytest.raises(retry.MaximumTimeoutExceeded):
        foo_with_timeout(-1)
