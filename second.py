#!/usr/bin/python3
import sys
import matplotlib.pyplot as plt
import csv


def estim(t0, t1, mil):
	return t1 * mil + t0

def train(mileage, price):
	t0 = 0.0
	t1 = 0.0
	tt0 = 1.0
	tt1 = 1.0
	sum0 = 0.0
	sum1 = 0.0
	l = len(mileage)
	print(l)
	learningRate = 0.01
	print("ICI ON A = ", sum([(estim(t0, t1, mileage[i]) - price[i]) for i in range(l)]))
	while abs(tt0) > 0.001 and abs(tt1) > 0.001:
		for i in range(l):
			sum0 += (estim(t0, t1, mileage[i]) - price[i])
			sum1 += (sum0 * mileage[i])


		tt0 = learningRate * sum0 / l
		tt1 = learningRate * sum1 / l

		print(tt0, tt1)

		t0 -= tt0
		t1 -= tt1


	while(abs(tt0) > 0.001 and abs(tt1) > 0.001):
		sum0 = sum([self._h(self.data_set[i][0] + self.scaled_min) - self.data_set[i][1] for i in range(len(self.data_set))])
		sum1 = sum([(self._h(self.data_set[i][0] + self.scaled_min) - self.data_set[i][1]) * self.data_set[i][0] for i in range(len(self.data_set))])
		tt0 = learningRate * sum0 / len(self.data_set)
		tt1 = learningRate * sum1 / len(self.data_set)
		self.theta0 -= tmp_theta0
		self.theta1 -= tmp_theta1

	print(t0, t1)
	print(estim(-1.4165536138106417e+293, -1.808206190753816e+299, 250000))

def display(mileage, price, lineMileage, linePrice):
	print(linePrice)
	plt.plot(mileage, price, 'ro', lineMileage, linePrice, 'g-')
	plt.ylabel('Price')
	plt.xlabel('Mileage')
	plt.show()

def main():
	dataFileToOpen = "data.csv"
	data = []
	try:
		with open(dataFileToOpen, 'r') as f:
			reader = csv.reader(f)
			data = list(reader)
	except Exception as e:
		exit(e)
	if data[0] == ['km', 'price']:
		data.remove(data[0])
	for d in data:
		for i, val in enumerate(d):
			try:
				d[i] = float(val)
			except Exception as e:
				exit(e)
	mileage = [x[0] for x in data]
	price = [x[1] for x in data]
	if len(mileage) != len(price):
		exit("Missing information for price or mileage.")
	train(mileage, price)

if __name__ == '__main__':
	main()
