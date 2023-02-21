class segitiga:
	def __init__(self, alas, tinggi):
		self.alas=alas
		self.tinggi=tinggi
		
	def get_luas(self):
		return 0.5 * self.alas * self.tinggi
		
segitiga1= segitiga(5, 10)
segitiga2= segitiga(10, 20)
segitiga3= segitiga(20, 40)

print('Luas Segitiga1 : ', segitiga1.get_luas())
print('Luas Segitiga2 : ', segitiga2.get_luas())
print('Luas Segitiga3 : ', segitiga3.get_luas())