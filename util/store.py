"""Store interface

Allows arbitrary classes to offer a simple get/set
store interface by deriving from the Store class in
this module
"""

class Store(object):
    """Interface for storing and retrieving simple values"""
    def __init__(self):
        super(Store, self).__init__()
        self._data = {}

    def set(self, key, value):
        """Set 'key' to 'value', overwriting 'key' if it exists already"""
        self._data[key] = { 'value': value, 'used': False }

    def unused_keys(self):
        return [ key for key, value in self._data.items() if value['used'] == False ]

    def get(self, key, default=None):
        """Return the current value of 'key', or 'default' if 'key' is not set"""
        if key in self._data:
            self._data[key]['used'] = True
        return self._data.get(key, { 'value': default })['value']

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
