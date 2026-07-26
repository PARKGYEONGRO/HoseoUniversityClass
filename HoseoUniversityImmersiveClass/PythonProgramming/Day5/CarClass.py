class Car:
    def __init__(self,model):
        self.model = model
        self.speed = 0
    
    def accelerate(self):
        self.speed += 10
        print(f'{self.model} 가속! 현재 속도: {self.speed} KM/h')
    
    def brake(self):
        self.speed = 0
        print(f'{self.model} 브레이크! 현재 속도: {self.speed} KM/h')

my_car = Car('아반떼')
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.brake()