"""A simple python module to add a retry function decorator"""
import functools
import logging
import time

__version__ = '0.0.1'
__author__ = 'Eli Uriegas'
__license__ = 'MIT'

_retries_error_msg = ('Exceeded maximum number of retries {} at '
                      'an interval of {}s for function {}')


class _DummyException(Exception):
    pass


class MaximumRetriesExceeded(Exception):
    pass


def retry(exceptions=(Exception,), interval=0, max_retries=10, success=None):
    """Decorator to retry a function 'max_retries' amount of times

    Args:
        exceptions (:tuple:None, optional): Exceptions to be caught for retries
        interval (int, optional): Interval between retries in seconds
        max_retries (int, optional): Maximum number of retries to have
        success (function, optional): Function to indicate success criteria

    Raises:
        MaximumRetriesExceeded: Maximum number of retries hit without reaching
            the success criteria

    Examples:
        Use it to decorate a function!
        >>>@retry(exceptions=(ArithmeticError,), success=lambda x: x > 0)
        >>>def foo(bar):
        >>>    if bar < 0:
        >>>        raise ArithmeticError('testing this')
        >>>    return bar
        >>>foo(5)
        5
        >>>foo(-1)
        ArithmeticError...
        >>>foo(0)
        MaximumRetriesExceeded...


    """
    if not exceptions and not success:
        raise Exception(
            '`exceptions` and `success` parameter can not both be None')
    # For python 3 compatability
    exceptions = exceptions or (_DummyException,)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            run_func = functools.partial(func, *args, **kwargs)
            logger = logging.getLogger(func.__module__)
            for num, _ in enumerate(range(max_retries), 1):
                try:
                    result = run_func()
                    if success and not success(result):
                        continue
                    return result
                except exceptions as exception:
                    logger.exception(exception)
                    if num == max_retries:
                        raise
                logger.warning(
                    'Retrying {} in {}s...'.format(
                        func.__name__, interval))
                time.sleep(interval)
            else:
                raise MaximumRetriesExceeded(
                    _retries_error_msg.format(
                        max_retries, interval, func.__name__))
        return wrapper
    return decorator
