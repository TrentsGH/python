
class vect(list):
    def __init__(self,*x):
        if x:
            try:
                super().__init__(*x)
            except:
                super().__init__(x)
        else:
            super().__init__([])
        self.n = len(self)

    def __neg__(self):
        ans = []
        for i in self:
            ans.append(-i)
        return vect(ans)
    
    def __add__(self,x):
        ans = []
        if type(x) not in (int,float,str,dict):
            for i in range(self.n):
                ans.append(self[i]+x[i])
        elif type(x) in (int,float):
            for i in range(self.n):
                ans.append(self[i]+x)
        return vect(ans)
    def __mul__(self,x):
        ans = []
        if type(x) not in (int,float,str,dict):
            for i in range(self.n):
                ans.append(self[i]*x[i])
        elif type(x) in (int,float):
            for i in range(self.n):
                ans.append(self[i]*x)
        return vect(ans)
    def __pow__(self,x):
        ans = []
        if type(x) not in (int,float,str,dict):
            for i in range(self.n):
                ans.append(self[i]**x[i])
        elif type(x) in (int,float):
            for i in range(self.n):
                ans.append(self[i]**x)
        return vect(ans)

    def __radd__(self,x):
        return self.__add__(x)
    def __sub__(self,x):
        return self.__add__(-x)
    def __rsub__(self,x):
        return -self.__sub__(x)
    def __rmul__(self,x):
        return self.__mul__(x)

def linspace(a,b,n):
    dx = (b-a)/(n-1)
    ans = []
    for i in range(n):
        ans.append(a+i*dx)
    return vect(ans)