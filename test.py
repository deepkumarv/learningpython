class Loc(object):
    def __init__(self,**kwargs):
        self.add(**kwargs)
    def add(self, **kwargs):
        self.__dict__.update(kwargs)
        
l = Loc()
kwargs={"a":3}


l.add(**kwargs)
kwargs={"b":3}
l.add(**kwargs)
print(l.__dict__)
name:str
name='pradeep'
print(type(name))
print('%({name})s'.format(name='pk'))