import csv
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

class Sahm():
	def __init__(self, li):
		self.date = li[0]
		self.first = li[1]
		self.high = li[2]
		self.low = li[3]
		self.close = li[4]



c = []
s = []
with open('../ghadir.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:
		s.append(row[6])
		del row[0:2]
		del row[4:]
		c.append(row)

	del c[0]
	del s[0]
#  c ---> [<DTYYYYMMDD>, <FIRST>, <HIGH>, <LOW>, <CLOSE>]

labels = ['FIRST', 'HIGH', 'LOW', 'CLOSE']


c = np.array(c)
c = c.astype(float)

s = np.array(s)
s = s.astype(float)

plt.subplot(1, 2, 1)
plt.boxplot(c, labels = labels, showfliers=False)

plt.subplot(1, 2, 2)
plt.boxplot(s, showfliers=False)
plt.title('vol')

plt.show()