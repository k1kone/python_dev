class A:
	def __init__(self):
		self.x = 10
		self.y = 20
		self.z = 30

a = A()

print(a.x, a.y, a.z, sep=' : ')


class B(A):
	def __init__(self):
		self.h = 40
		super().__init__()
	def sss(self):
		return self.x + self.y

b = B()
print(b.x, b.y, b.z, b.h, b.sss(), sep=' : ')
