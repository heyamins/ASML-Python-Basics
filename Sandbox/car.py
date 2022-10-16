class Car:

    CLASS_NAME = 'Car'
    VERSION = '1.0'

    @staticmethod
    def class_name():
        return Car.CLASS_NAME

    @staticmethod
    def get_version():
        return Car.VERSION

    @staticmethod
    def calculate_usage(amount_of_gas, number_of_kilometers):
        return number_of_kilometers / amount_of_gas

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage
        self._started = False

    def info(self):
        print( f'This great {self._color} {self._make} {self._model} as driven {self._mileage}km.' )
        if self._started:
            print( f'The engine is still running.')

    def __str__(self):
        return f'Car: {self._color} {self._make} {self._model} mileage: {self._mileage}km.'

    def __repr__(self):
        return f"Car('{self._make}', '{self._model}', '{self._color}')"

    def drive(self, km):
        if self._started:
            self._mileage += km
        else:
            print('Please start your car first.')

    def start(self):
        self._started = True

    def stop(self):
        self._started = False

    def __del__(self):
        print('The car has been demolished. Too bad.')



    
# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown')

    my_car.start()
    my_car.drive(200)

    print(my_car)

    print(Car.class_name())

#    del my_car

