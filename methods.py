import pandas as pd


class RA:
    def __init__(self, hour, minute, second):
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = float(second)

    def ra_from_str(string):
        h, m, s, = string.split(' ')
        return RA(h, m, s)
        

    def show(self):
        print(f'{self.hour:02} {self.minute:02} {self.second:0<6}')

    def totalsec(self):
        return self.hour*3600 + self.minute*60 + self.second
    
    def __eq__(a, b):
        return a.totalsec()==b.totalsec()
    
    def __ne__(a, b):
        return a.totalsec()!=b.totalsec()
    
    def __lt__(a, b):
        return a.totalsec()<b.totalsec()
    
    def __le__(a, b):
        return a.totalsec()<=b.totalsec()
    
    def __gt__(a, b):
        return a.totalsec()>b.totalsec()
    
    def __ge__(a, b):
        return a.totalsec()>=b.totalsec()
    

class DEC:
    def __init__(self, grad, minute, second):
        self.grad = int(grad)
        self.minute = int(minute)
        self.second = float(second)
        
    def dec_from_str(string):
        g, m, s, = string.split(' ')
        return DEC(g, m, s)

    def show(self):
        print(f'{self.grad:02} {self.minute:02} {self.second:0<5}')

    def totalsec(self):
        return self.grad*3600 + self.minute*60 + self.second
    
    def __eq__(a, b):
        return a.totalsec()==b.totalsec()
    
    def __ne__(a, b):
        return a.totalsec()!=b.totalsec()
    
    def __lt__(a, b):
        return a.totalsec()<b.totalsec()
    
    def __le__(a, b):
        return a.totalsec()<=b.totalsec()
    
    def __gt__(a, b):
        return a.totalsec()>b.totalsec()
    
    def __ge__(a, b):
        return a.totalsec()>=b.totalsec()
    
class obj:
    def __init__(self, dat):

        self.data = dat
        self.type = dat[116:132]
        self.number = int(dat[:5])
        radec = dat[6:40].split(' ')
        self.ra = RA(radec[0], radec[1], radec[2])
        self.ra_txt = str(radec[0]) +' '+ str(radec[1])+' '+ str(radec[2])
        self.dec = DEC(radec[3], radec[4], radec[5])
        self.dec_txt = str(radec[3]) +' '+ str(radec[4])+' '+ str(radec[5])

        if ' ' not in dat[132:137]:
            self.z = float(dat[132:137])
        else: self.z = float("NaN")


def dataframe(objects):
    number = []
    ra = []
    dec = []
    z = []
    types = []
    ra_obj = []
    dec_obj = []

    for item in objects:
        number.append(item.number)
        ra.append(item.ra_txt)
        dec.append(item.dec_txt)
        z.append((item.z))
        types.append(item.type)
        ra_obj.append(item.ra)
        dec_obj.append(item.dec)

    df = pd.DataFrame({
                'RA': ra, 
                'DEC': dec, 
                'z': z, 
                'type': types},
                #'ra_obj': ra_obj,
                #'dec_obj': dec_obj},
                index = number)
                    
    return df