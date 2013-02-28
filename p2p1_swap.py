"""
Given a dictionary, swap keys <-> values. The program should use some custom
logic to check if the swap is possible, but without using try..except
constructs or the __hash__() function.
Example:
Input: {'a': 123, 'b': 456}
Output: {123: 'a', 456: 'b'}
------------------------------------------------
Input: {'a': (1, 2, [3])}
Output: Swap is not possible

"""

from collections import Hashable, Container, Iterable


def is_immutable(obj):
    """
    Verifies that an object is immutable.
    Example:

    >>> is_immutable(1)
    True

    >>> is_immutable((1, 2, 'abc', (1, 2, u'3sd4')))
    True

    >>> is_immutable([1, 2])
    False

    >>> is_immutable((1, [1]))
    False

    """
    if isinstance(obj, Hashable):
        if isinstance(obj, Container) or isinstance(obj, Iterable):
            return is_deep_immutable(obj)
        else:
            return True
    else:
        return False


def is_deep_immutable(collection):
    """
    Verifies that a collection has immutable elements.
    Example:

    >>> is_deep_immutable('abc')
    True

    >>> is_deep_immutable(u'abc')
    True

    >>> is_deep_immutable((1, 2, [1, 2]))
    False

    >>> is_deep_immutable((1, 'abc', (1, 2)))
    True

    """
    if isinstance(collection, basestring):
        return True
    is_deep_immutable = True
    for element in collection:
        is_deep_immutable = is_deep_immutable and is_immutable(element)
    return is_deep_immutable


def swap_keys_with_values(dictionary):
    """
    Swaps the keys and values in the given dictionary.
    Example:

    >>> swap_keys_with_values({'a': 123, 'b': 456}) == {123: 'a', 456: 'b'}
    True

    >>> swap_keys_with_values({'a': (1, 2, [3])})

    >>> swap_keys_with_values({})
    {}

    """
    result = dict()
    for key, value in dictionary.iteritems():
        if is_immutable(value):
            result[value] = key
        else:
            return None
    return result


if __name__ == '__main__':
    initial_dictionary = input(
            'Type in a dictionary (raw Python representation): ')
    result = swap_keys_with_values(initial_dictionary)
    if result is None:
        print 'Swap is not possible'
    else:
        print result

