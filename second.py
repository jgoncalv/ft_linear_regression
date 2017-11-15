#!/usr/bin/python3
import sys
import matplotlib.pyplot as plt
import pandas as pd


def estim(t0, t1, mil):
	return t1 * mil + t0

def normalize(lstX, x):
	return (x - min(lstX)) / (max(lstX) - min(lstX))

def train(mileage, price):
	t0 = 0.0
	t1 = 0.0
	tt0 = 1.0
	tt1 = 1.0
	l = len(mileage)
	learningRate = 0.01
	while abs(tt0) > 0.1 and abs(tt1) > 0.1:
		# on calcule les sommes
		sum0 = sum([estim(t0, t1, normalize(mileage, mileage[i])) - price[i] for i in range(l)])
		sum1 = sum([(estim(t0, t1, normalize(mileage, mileage[i])) - price[i]) * normalize(mileage, mileage[i]) for i in range(l)])

		tt0 = learningRate * sum0 / l
		tt1 = learningRate * sum1 / l

		print(tt0, tt1)

		t0 -= tt0
		t1 -= tt1

	return t0, t1

	print(t0, t1)
	print(estim(-1.4165536138106417e+293, -1.808206190753816e+299, 250000))

def display(mileage, price, lineMileage, linePrice):
	print(linePrice)
	plt.plot(mileage, price, 'ro', lineMileage, linePrice, 'g-')
	plt.ylabel('Price')
	plt.xlabel('Mileage')
	plt.show()

def main():
	data = []
	try:
		data = pd.read_csv("data.csv", dtype = "float")
	except Exception as e:
		exit(e)
	minPrice = min(data.price)
	maxPrice = max(data.price)
	minMileage = min(data.km)
	maxMileage = max(data.km)
	mileage = (data.km - minMileage) / (maxMileage - minMileage)
	price = (data.price - minPrice) / (maxPrice - minPrice)
	t0, t1 = train(mileage, price)

if __name__ == '__main__':
	main()
