# remeber to import the trip class here

from trip import Trip
class Driver:

    def __init__(self, name):
        self.name = name

    def name():
        doc = "The name property."
        def fget(self):
            return self._name
        def fset(self, value):
            self._name = value
        def fdel(self):
            del self._name
        return locals()
    name = property(**name())

    def my_trips(self):
        trips = Trip.all()
        return [trip for trip in trips if trip.driver == self]

    def my_trip_summaries(self):
        trips = self.my_trips()
        return ["{} to {}".format(trip.start, trip.destination) for trip in trips]
