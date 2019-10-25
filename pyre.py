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

    def music_get(self, a):
        return self.pyre.child("music").child(a).get().val()

    def music_upload(self, a):
        c = self.pyre.child("music").child(0).get().val()
        self.pyre.child("music").child(c+1).set(a)
        self.pyre.child("music").child(0).set(c+1)

    def num_get(self):
        return self.pyre.child("music").child(0).get().val()
