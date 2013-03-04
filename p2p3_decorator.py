""""
Problem statement:
Write a function decorator that tracks how long the execution of the wrapped
function took. The decorator will log slow function calls including details
about the execution time and function name. The decorator should take an
optional threshold argument.
Examples:

@time_slow
def myfast():
    pass

@time_slow(threshold=0.05)
def myfast():
    pass

"""


from time import time, sleep
from datetime import datetime
import doctest
import sys


_SNAIL_MESSAGE_FORMAT = 'Function <%(func_name)s> took %(duration).4f ' + \
        'seconds [started @ %(start_time)s, ended @ %(end_time)s].'
_EXCEEDED_THRESHOLD_MESSAGE_FORMAT = 'Function execution exceeded the ' + \
        'threshold of %.4f seconds.'


def generate_output(func_name, start_time, end_time, threshold):
    """
    Generates the message that will be printed out by the decorator. The
    message will include the name of the decorated function, the time in
    seconds that the function started, respectively ended execution and the
    threshold the function executin is not supposed to exceed.

    >>> generate_output('a_func', 1362391085.392695, 1362391086.772795, 2)
    'Function <a_func> took 1.3801 seconds [started @ 04.03.2013 11:58:05.392695, ended @ 04.03.2013 11:58:06.772795].'

    >>> generate_output('a_func', 1362391085.392695, 1362391086.772795, None)
    'Function <a_func> took 1.3801 seconds [started @ 04.03.2013 11:58:05.392695, ended @ 04.03.2013 11:58:06.772795].'

    >>> generate_output('a_func', 1362391085.392695, 1362391086.772795, 1.1)
    'Function <a_func> took 1.3801 seconds [started @ 04.03.2013 11:58:05.392695, ended @ 04.03.2013 11:58:06.772795]. Function execution exceeded the threshold of 1.1000 seconds.'

    """
    start_time_dt = datetime.fromtimestamp(start_time)
    end_time_dt = datetime.fromtimestamp(end_time)
    duration = end_time - start_time
    output_details = {'func_name': func_name,
                      'duration': duration,
                      'start_time': start_time_dt.strftime(
                          '%d.%m.%Y %H:%M:%S.%f'),
                      'end_time': end_time_dt.strftime(
                          '%d.%m.%Y %H:%M:%S.%f')}
    result = _SNAIL_MESSAGE_FORMAT % output_details
    if threshold is not None and threshold < duration:
        result = result + ' ' + _EXCEEDED_THRESHOLD_MESSAGE_FORMAT % \
                threshold
    return result


def _function_timer_decorator_maker(func=None, threshold=None,
                                    output=sys.stdout):
    """
    Function used to create a decorator that can process decorator arguments.

    >>> from StringIO import StringIO
    >>> iostr = StringIO()
    >>> @_function_timer_decorator_maker(output=iostr)
    ... def f(): pass
    ...
    >>> f()
    >>> len(iostr.getvalue()) > 0
    True

    >>> @_function_timer_decorator_maker(threshold=2, output=iostr)
    ... def f(a, b):
    ...     return a + b
    ...
    >>> f(1, 2)
    3
    >>> len(iostr.getvalue()) > 0
    True

    """
    def function_timer_decorator(_func):
        """
        The actual function decorator that will return the wrapper around the
        given function.

        """
        def func_wrapper(*args, **kwargs):
            """
            The wrapper around the decorated function.
            Takes the parameters of the function as input and returns its
            result.

            """
            start_time = time()
            result = _func(*args, **kwargs)
            end_time = time()
            output.write(generate_output(_func.func_name, start_time,
                                         end_time, threshold))
            output.write('\n')
            return result
        return func_wrapper
    # Decide which function to return.
    if func is None:
        # The decorator was invoked in function mode:
        # @_function_timer_decorator_maker() or
        # @_function_timer_decorator_maker(threshold=45)
        # => return the decorator function.
        return function_timer_decorator
    else:
        # The decorator was invoked in normal mode:
        # @_function_timer_decorator_maker
        # => return the function wrapper
        return function_timer_decorator(func)
# Give a "pretty" name to the decorator.
function_timer = _function_timer_decorator_maker


@function_timer(threshold=2)
def slow_function():
    sleep(2.45)
    return 'smth'

@function_timer
def even_slower_function(s):
    sleep(s)

@function_timer(threshold=3)
def another_function(s, msg):
    sleep(s)
    return msg


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        doctest.testmod()
    else:
        print 'RUNNING slow_function'
        print slow_function()
        print '\nRUNNING even_slower_function'
        even_slower_function(3.04)
        print '\nRUNNING another_function'
        print another_function(1.4, 'Hello!!')

