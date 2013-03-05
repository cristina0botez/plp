import sys


class my_decorator_with_args(object):

    def __init__(self, threshold=None, output=sys.stdout):
        self._threshold = threshold
        self._output = output

    def __call__(self, func):
        def func_wrapper(*args, **kwargs):
            self._output.write('Before %s\n' % func.__name__)
            if self._threshold is not None:
                self._output.write('%d\n' % self._threshold)
            result = func(*args, **kwargs)
            self._output.write('After %s\n' % func.__name__)
            return result
        return func_wrapper


class my_decorator(object):

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print 'Before %s' % self._func.__name__
        result = self._func(*args, **kwargs)
        print 'After %s' % self._func.__name__
        return result


@my_decorator_with_args(threshold=3)
def fun():
    print 'Having fun'

@my_decorator
def add(a, b):
    return a + b


if __name__ == '__main__':
    fun()
    print add('a', 'b')

