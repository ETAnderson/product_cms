import json
import os

class GenericDatabase(object):
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self , location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location , "r"))

    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except Exception as e:
            print("Error Dumping Database : " + str(e))
            return False

    def set(self , key , value):
        try:
            self.db[str(key)] = value
            return self.dumpdb()
        except Exception as e:
            print("Error Saving Values to Database : " + str(e))
            return False

    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key))  
            return False

    def delete(self , key):
        if not str(key) in self.db:
            return False
        del self.db[str(key)]
        return self.dumpdb()

    def resetdb(self):
        self.db = {}
        return self.dumpdb()