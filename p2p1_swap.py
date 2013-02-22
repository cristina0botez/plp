from collections import Hashable, Container, Iterable

def isImmutable(obj):
    if isinstance(obj, Hashable):
        if isinstance(obj, Container) or isinstance(obj, Iterable):
            return isDeepImmutable(obj)
        else:
            return True
    else:
        return False

def isDeepImmutable(collection):
    if isinstance(collection, str):
        return True
    isDeepImmutable = True
    for element in collection:
        isDeepImmutable = isDeepImmutable and isImmutable(element)
    return isDeepImmutable

def swapKeysWithValues(dictionary):
    swapResult = dict()
    for key, value in dictionary.iteritems():
        if isImmutable(value):
            swapResult[value] = key
        else:
            raise SwapError('The following value is not immputable: %r. It cannot be a key.' % (value,))
    return swapResult


class SwapError(Exception):
    pass


if __name__ == '__main__':
    try:
        initialDictionary = input('Type in a dictionary (raw Python representation): ')
        swappedDictionary = swapKeysWithValues(initialDictionary)
        print swappedDictionary
    except SwapError, se:
        print 'A key - value swap is not possible. Details: %s' % se.message

