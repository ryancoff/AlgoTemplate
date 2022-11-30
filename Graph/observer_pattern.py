class Config:
    def __init__(self, observers = []):
        self.observers = observers
        
    def get_all_observers(self):
        return self.observers
    
    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        
    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass
        
    def notify(self, modifier = None):
        for observer in self.get_all_observers():
            if observer != modifier:
                observer.update(self)
        
class Core(Config):
    def __init__(self, id = 0):
        Config.__init__(self)
        self._id = id
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        self.notify()
        
#Observer
class User:
    def update(self, config):
        print("Config id: {} has been updated".format(config._id))


def main():
    c1 = Core(5)

    u1 = User()
    u2 = User()

    c1.attach(u1)
    c1.attach(u2)
    c1.id = 10
    c1.id = 20
    
main()
#Config id: 10 has been updated
#Config id: 10 has been updated