import pyrebase

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton

class Pyre():
    def __init__(self, *args, **kwargs):
        self._config = {"apiKey": "AIzaSyBdvRJ2ixcDi4Glspl2C6gGEjlZuS83Hy8",
                       "authDomain": "ffacegram.firebaseio.com",
                       "databaseURL": "https://ffacegram.firebaseio.com/",
                       "storageBucket": "ffacegram.appspot.com",
                       "serviceAccount": "GooCreds.json"}
        self._firebase = pyrebase.initialize_app(self._config)
        self.pyre = self._firebase.database()

    def increment(self, a, b):
        av = self.pyre.child("users").child("scores").child(a).get().val()
        bv = self.pyre.child("users").child("scores").child(b).get().val()

        e_a = 1/(1+10**((bv-av)/400))
        e_b = 1/(1+10**((av-bv)/400))

        av1 = av + 10*(1-e_a) 
        bv1 = bv - 10*e_b
        
        self.pyre.child("users").child("scores").update({a : av1})
        self.pyre.child("users").child("scores").update({b : bv1})
