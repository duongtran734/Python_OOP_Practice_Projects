
class Car:

    def __init__(self, year, make, model, color, fuel_type):
        self._year = year
        self._make = make
        self._model = model
        self._color = color
        self._fuel = fuel_type

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self,year):
        self._year = year

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self,make):
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self,model):
        self._model = model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self,fuel_type):
        self._fuel = fuel_type


    def show(self):
        print(f"Year: {self.year}\n"
              f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Color: {self.color}\n"
              f"Fuel Type: {self.fuel}\n")

    # Methods
    # Check if vehicle require maintenance
    def maintenance_require(self):
        return self.year <= 2000



if __name__ == "__main__":
    vehicle1 = Car(2000, "Toyota", "Highlander", "Red", "Gas")
    vehicle1.show()
    print(vehicle1.maintenance_require())
