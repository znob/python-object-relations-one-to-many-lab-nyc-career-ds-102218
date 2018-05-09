class Car:

    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)
        #remember to associate a car with its owner

    @classmethod
    def all(cls):
        return cls._all

    def make():
        doc = "The make property."
        def fget(self):
            return self._make
        def fset(self, value):
            self._make = value
        def fdel(self):
            del self._make
        return locals()
    make = property(**make())

    def model():
        doc = "The model property."
        def fget(self):
            return self._model
        def fset(self, value):
            self._model = value
        def fdel(self):
            del self._model
        return locals()
    model = property(**model())

    def year():
        doc = "The year property."
        def fget(self):
            return self._year
        def fset(self, value):
            self._year = value
        def fdel(self):
            del self._year
        return locals()
    year = property(**year())

    def owner():
        doc = "The owner property."
        def fget(self):
            return self._owner
        def fset(self, value):
            self._owner = value
        def fdel(self):
            del self._owner
        return locals()
    owner = property(**owner())
