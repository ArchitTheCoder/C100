class Car(object):
    def __init__(self, model, color, company, speedLimit):
         self.color = color
         self.model = model
         self.company = company
         self.speedLimit = speedLimit
        
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

    def accelerate(self):
        print("Car is accelerating")

honda = Car("A2-41", "silver", "Honda", 120)
honda.start()
honda.accelerate()
honda.stop()