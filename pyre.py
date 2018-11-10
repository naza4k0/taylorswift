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

    def g_round(self, a, b):
        av = self.pyre.child("users").child("scores").child(a).get().val()
        bv = self.pyre.child("users").child("scores").child(b).get().val()

        e_a = 1/(1+10**((bv-av)/400))
        e_b = 1/(1+10**((av-bv)/400))

        av1 = av + 10*(1-e_a) 
        bv1 = bv - 10*e_b
        
        self.pyre.child("users").child("scores").update({a : av1})
        self.pyre.child("users").child("scores").update({b : bv1})

    def g_name(self, a):
        return self.pyre.child("users").child("names").child(a).get().val()

    def g_photo(self, a):
        return self.pyre.child("users").child("photos").child(a).get().val()
    
    def g_rating(self):
        data = []
        for i in range(self.pyre.child("users").child("number").child(0).get().val()):
            data.append(self.pyre.child("users").child("scores").child(i).get().val())
        maxim = []
        for i in range(5):
            a = max(data)
            b = data.index(a)
            data[b] = 0
            maxim.append(b)
        return maxim

    def g_text_upload(self, a):
        c = self.pyre.child("users").child("number").child(0).get().val()
        self.pyre.child("users").child("names").child(c).set(a)
       
    def g_photo_upload(self, a):
        c = self.pyre.child("users").child("number").child(0).get().val()
        self.pyre.child("users").child("scores").child(c).set(1000)
        self.pyre.child("users").child("photos").child(c).set(a)
        self.pyre.child("users").child("number").update({0: c+1})
   
    def g_number(self):
        return self.pyre.child("users").child("number").child(0).get().val()

    def g_score(self, a):
        return self.pyre.child("users").child("scores").child(a).get().val()

    def g_updater(self):
        for i in range(self.pyre.child("users").child("number").child(0).get().val()):
            self.pyre.child("users").child("scores").update({i: 1000})

    def g_link(self, a):
        xstr = lambda s: s or ""
        link = xstr(self.pyre.child("users").child("links").child(a).get().val())
        if link:
            link = '   🔹<a href="' + a +'">Instagram</a>🔹'
        return link


    def g_admin_rating(self):
        data = []
        for i in range(self.pyre.child("users").child("number").child(0).get().val()):
            data.append(self.pyre.child("users").child("scores").child(i).get().val())
        maxim = []
        for i in range(self.pyre.child("users").child("number").child(0).get().val()):
            a = max(data)
            b = data.index(a)
            data[b] = 0
            maxim.append(b)
        return maxim