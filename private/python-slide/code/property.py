class C(object):
    def __init__(self):
        self._x = None
    def getx(self):
        print 'get x'
        return self._x
    def setx(self, value):
        print 'set x'
        self._x = value
    def delx(self):
        print 'del x'
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")


class Parrot(object):
    def __init__(self):
        self._voltage = 100000
    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage
    @voltage.setter
    def voltage(self, value):
        """Set to current voltage."""
        self._voltage = value
