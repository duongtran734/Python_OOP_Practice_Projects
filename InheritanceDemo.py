class Robot:
    self_destruction = False

    def __init__(self, name, year, model):
        self.name = name
        self.year = year
        self.model = model

    def talk(self):
        print(f"Hello I am {self.name} , I was created in {self.year}. My model is {self.model}")


# Sub class from Robot
class CarRobot(Robot):
    num_wheels = 4


    def run(self):
        print(f"Robot {self.name} is Running.")

# Sub class from robot
class PlaneRobot(Robot):
    num_wings = 2
    #dont need init method here since its the same as parent class, it will call the Robot __init__ instead
    def fly(self):
        print(f'Robot {self.name} is Flying.')


if __name__ == '__main__':
    carRobot = CarRobot("Carl", 1999, "X")
    planeRobot = PlaneRobot("Falcon", 2010, "XI")

    # Method from subclass
    carRobot.run()
    # Call method from parent class
    carRobot.talk()
    # Check if CarRobot is a subclass of Robot class
    print(issubclass(CarRobot, Robot))

    # Plane robot can fly but cannot run
    planeRobot.fly()
    # PlaneRobot can use methods from Robot class but no from CarRobot class
    planeRobot.talk()
    # Class variable in subclass
    print(planeRobot.num_wings)
    # Subclass can Access parent class class variable
    print(planeRobot.self_destruction)

