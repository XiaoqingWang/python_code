class CarStore(object):
	def __init__(self):
		self.factory = Factory()

	def order(self, car_type):
		return self.factory.select_car_by_type(car_type)

class Factory(object):
	def select_car_by_type(self, car_type):
		if car_type == "索纳塔":
			return Suonata()
		elif car_type == "名图":
			return Mingtu()
		elif car_type == "ix35":
			return Ix35()


class Car(object):
	def move(self):
		print("车在移动。。。。")
	def music(self):
		print("正在播放音乐。。。。")
	def stop(self):
		print("车在停止。。。")

class Suonata(Car):
	def __init__(self):
		self.__name = "索纳塔"
		super(Suonata, self).__init__()

class Mingtu(Car):
	def __init__(self):
		self.__name == "名图"
		super(Mingtu, self).__init__()

class Ix35(Car):
	def __init__(self):
		self.__name == "IX35"
		super(Ix35, self).__init__()

car_store = CarStore()
car = car_store.order("索纳塔")
car.move()
car.music()
car.stop()
