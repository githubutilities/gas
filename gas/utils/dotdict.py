
class DotDict(dict):
    """Container object for datasets

    Dictionary-like object that exposes its keys as attributes.
    Support getitem using dot key.

    >>> b = DotDict(a=1, b=2)
    >>> b['b']
    2
    >>> b.b
    2
    >>> b.a = 3
    >>> b['a']
    3
    >>> b.c = 6
    >>> b['c']
    6
    >>> b['c'] = { 'd': 'e' }
    >>> b['c.d']
    'e'

    """

    def __init__(self, **kwargs):
        dict.__init__(self, kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __getitem__(self, key):
        key_str = key
        keys = key_str.split('.')
        cur = None
        for key in keys:
            try:
                cur = self.get(key) if cur is None else cur.get(key)
            except KeyError:
                raise AttributeError("{} in {}".format(key, key_str))
        return cur

    def __getstate__(self):
        return self.__dict__
