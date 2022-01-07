class Cars(object):
    def __init__(self,name,model,company,color):
        self.name=name
        self.model=model
        self.company=company
        self.color=color
    def start(self):
        print("The car has started")
    def stop(self):
        print("The car has stopped")
    def accelerate(self):
        print("The car has reached maximum speed limit")
    def decrease(self):
        print("The speed has been decreased to 75km/hr")
    def dest(self):
        print("You have reached your destination")
Sonet=Cars("Sonet","Sedan","Kia","White")
print(Sonet.color)
print(Sonet.model)
print(Sonet.company)
print(Sonet.name)
Sonet.start()
Sonet.accelerate()
Sonet.decrease()
Sonet.stop()
Sonet.dest()
