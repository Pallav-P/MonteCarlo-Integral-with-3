import numpy as np


#Second fundamnetal theorem of calculus for multivariable itegrations is
# avg(r) = 1/((x2-x1)(y2-y1)(z2-z1)) * integral(r(x,y,z), (x1,x2), (y1,y2), (z1,z2))

class FunctionIntegral:
	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0
	z1 = 0
	z2 = 0

	num_samples = 10000


	def __init__(self, x1, x2, y1, y2, z1, z2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.z1 = z1
		self.z2 = z2	

	def function(self, x,y,z):
		return x * y * z

	def set_num_samples(self, num):
		self.num_samples = num

	def generate_randoms(self, a,b):
		return np.random.uniform(a, b, self.num_samples)

	def calculate_average(self):
		xvals = self.generate_randoms(self.x1, self.x2)
		yvals = self.generate_randoms(self.y1, self.y2)
		zvals = self.generate_randoms(self.z1, self.z2)
		value = 0
		for i in range(self.num_samples):
			value += self.function(xvals[i], yvals[i], zvals[i])
		return value / self.num_samples

	def value(self):
		factor = (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)
		return self.calculate_average() * factor

	def integral(self, num_iterations):
		val = 0;
		for i in range(num_iterations):
			inte = self.value()
			val += inte
			print(f"The value of iteration {i} int is {inte}")

		final_val = val / num_iterations
		print(f"The value of the integral using Monte Carlo Methods {self.num_samples * num_iterations} times is {round(final_val, 4)}")
		return final_val


#Use multiple functions by creating subclasses and by using polymorphism like this
class FunctionOne(FunctionIntegral):
	def function(self, x, y, z):
		return np.sin(x * y * z)



def main():
	inte = FunctionOne(0, 1, 0, 1, 0, 1)
	inte.integral(int(input("Enter number of iterations: ")))
	return




if __name__ == "__main__":
	main()















