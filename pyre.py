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

    def g1_round(self, a, b, c):
        av = self.pyre.child("id_g").child(c).child(a).get().val()
        bv = self.pyre.child("id_g").child(c).child(b).get().val()

        e_a = 1/(1+10**((bv-av)/400))
        e_b = 1/(1+10**((av-bv)/400))

        av1 = av + 10*(1-e_a) 
        bv1 = bv - 10*e_b
        
        self.pyre.child("id_g").child(c).update({a : av1})
        self.pyre.child("id_g").child(c).update({b : bv1})

    
    def g_photo(self, a):
        return self.pyre.child("users").child("photos").child(a).get().val()

    def g_name(self, a):
        return self.pyre.child("users").child("names").child(a).get().val()
    
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

    def gid_rating(self, a):
        data = []
        for i in range(self.pyre.child("users").child("number").child(0).get().val()):
            data.append(self.pyre.child("id_g").child(a).child(i).get().val())
        maxim = []
        for i in range(5):
            a = max(data)
            b = data.index(a)
            data[b] = 0
            maxim.append(b)
        return maxim

    def g_text_upload(self, a):
        c = self.pyre.child("musers").child("number").child(0).get().val()
        self.pyre.child("musers").child("names").child(c).set(a)
        
    def g_link_upload(self, a):
        c = self.pyre.child("musers").child("number").child(0).get().val()
        self.pyre.child("musers").child("links").child(c).set(a)
       
    def reg_check(self, a, l, m, n):
        xstr = lambda s: s or ""
        b = xstr(self.pyre.child("id_g").child("reg").child(a).get().val())
        if b == "":
            for i in range(self.pyre.child("users").child("number").child(0).get().val()):
                self.pyre.child("id_g").child(a).child(i).set(1000)
            self.pyre.child("id_g").child("reg").child(a).set(l + " " + m + " " + n)
            return 2
        elif b == 1:
            self.pyre.child("id_g").child("reg").child(a).set(l + " " + m + " " + n)
            return 1
        else:
            return 0

    def g_photo_upload(self, a):
        c = self.pyre.child("musers").child("number").child(0).get().val()
        self.pyre.child("musers").child("scores").child(c).set(1000)
        self.pyre.child("musers").child("photos").child(c).set(a)
        for i in self.pyre.child("mid_g").child("reg").get().each():
            self.pyre.child("mid_g").child(i.key()).child(c).set(1000)
        self.pyre.child("musers").child("number").update({0: c+1})

    def g_number(self):
        return self.pyre.child("users").child("number").child(0).get().val()

    def g_score(self, a):
        return self.pyre.child("users").child("scores").child(a).get().val()
        
    def g_link(self, a):
        xstr = lambda s: s or ""
        link = xstr(self.pyre.child("users").child("links").child(a).get().val())
        c = self.pyre.child("users").child("names").child(a).get().val()
        if link:
            b = '<a href="' + link +'">' + c + '</a>'
        else:
            b = c
        return b

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

    def m_round(self, a, b):
        av = self.pyre.child("musers").child("scores").child(a).get().val()
        bv = self.pyre.child("musers").child("scores").child(b).get().val()

        e_a = 1/(1+10**((bv-av)/400))
        e_b = 1/(1+10**((av-bv)/400))

        av1 = av + 10*(1-e_a) 
        bv1 = bv - 10*e_b
        
        self.pyre.child("musers").child("scores").update({a : av1})
        self.pyre.child("musers").child("scores").update({b : bv1})

    def m1_round(self, a, b, c):
        av = self.pyre.child("mid_g").child(c).child(a).get().val()
        bv = self.pyre.child("mid_g").child(c).child(b).get().val()

        e_a = 1/(1+10**((bv-av)/400))
        e_b = 1/(1+10**((av-bv)/400))

        av1 = av + 10*(1-e_a) 
        bv1 = bv - 10*e_b
        
        self.pyre.child("mid_g").child(c).update({a : av1})
        self.pyre.child("mid_g").child(c).update({b : bv1})

    
    def m_photo(self, a):
        return self.pyre.child("musers").child("photos").child(a).get().val()

    def m_name(self, a):
        return self.pyre.child("musers").child("names").child(a).get().val()
    
    def m_rating(self):
        data = []
        for i in range(self.pyre.child("musers").child("number").child(0).get().val()):
            data.append(self.pyre.child("musers").child("scores").child(i).get().val())
        maxim = []
        for i in range(5):
            a = max(data)
            b = data.index(a)
            data[b] = 0
            maxim.append(b)
        return maxim

    def mid_rating(self, a):
        data = []
        for i in range(self.pyre.child("musers").child("number").child(0).get().val()):
            data.append(self.pyre.child("mid_g").child(a).child(i).get().val())
        maxim = []
        for i in range(5):
            a = max(data)
            b = data.index(a)
            data[b] = 0
            maxim.append(b)
        return maxim

    def mreg_check(self, a, l, m, n):
        xstr = lambda s: s or ""
        b = xstr(self.pyre.child("mid_g").child("reg").child(a).get().val())
        if b == "":
            for i in range(self.pyre.child("musers").child("number").child(0).get().val()):
                self.pyre.child("mid_g").child(a).child(i).set(1000)
            self.pyre.child("mid_g").child("reg").child(a).set(l + " " + m + " " + n)
            return 2
        elif b == 1:
            self.pyre.child("mid_g").child("reg").child(a).set(l + " " + m + " " + n)
            return 1
        else:
            return 0

    def m_number(self):
        return self.pyre.child("musers").child("number").child(0).get().val()

    def m_score(self, a):
        return self.pyre.child("musers").child("scores").child(a).get().val()

    def m_link(self, a):
        xstr = lambda s: s or ""
        link = xstr(self.pyre.child("musers").child("links").child(a).get().val())
        c = self.pyre.child("musers").child("names").child(a).get().val()
        if link:
            b = '<a href="' + link +'">' + c + '</a>'
        else:
            b = c
        return b

    def m_admin_rating(self):
        data = []
        for i in range(self.pyre.child("musers").child("number").child(0).get().val()):
            data.append(self.pyre.child("musers").child("scores").child(i).get().val())
        maxim = []
        for i in range(self.pyre.child("musers").child("number").child(0).get().val()):
            a = max(data)
            b = data.index(a)
            data[b] = 0
            maxim.append(b)
        return maxim
