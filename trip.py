class Trip:
    _all = []

    def __init__(self, start, end, driver):
        self._start = start
        self._destination = end
        self._driver = driver
        Trip._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def start():
        doc = "The start property."
        def fget(self):
            return self._start
        def fset(self, value):
            self._start = value
        def fdel(self):
            del self._start
        return locals()
    start = property(**start())

    def destination():
        doc = "The destination property."
        def fget(self):
            return self._destination
        def fset(self, value):
            self._destination = value
        def fdel(self):
            del self._destination
        return locals()
    destination = property(**destination())

    def driver():
        doc = "The driver property."
        def fget(self):
            return self._driver
        def fset(self, value):
            self._driver = value
        def fdel(self):
            del self._driver
        return locals()
    driver = property(**driver())
