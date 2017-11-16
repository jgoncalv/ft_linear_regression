#!/usr/bin/python3
import sys
import matplotlib.pyplot as plt
import pandas as pd

def normalize(lstX, x):
	return (x - min(lstX)) / (max(lstX) - min(lstX))

def denormalize(lstX, x):
	return (x * (max(lstX) - min(lstX)) + min(lstX))

def gradient_descent(x, y, learningRate, length, iteration):
	t0 = 0
	t1 = 0
	loss_history = []
	t0_history = []
	t1_history = []
	for j in range(0, iteration):
		tt0 = 0
		tt1 = 0
		for i in range(0, length):
			tt0 += ((t1 * x[i] + t0) - y[i])
			tt1 += (((t1 * x[i] + t0) - y[i]) * x[i])
		t0 = t0 - (learningRate * (tt0 / length))
		t1 = t1 - (learningRate * (tt1 / length))
		loss_history.append(cost_func(length, t0, t1, x, y))
		t0_history.append(t0)
		t1_history.append(t1)
	return t0, t1, t0_history, t1_history, loss_history

def cost_func(length, t0, t1, x, y):
    total_error = 0
    for i in range(0, length):
        total_error += (y[i] - (t1 * x[i] + t0)) ** 2
    return total_error / float(length)

def display(data, t0, t1, t0_history, t1_history, loss_history):

	linex = [min(data.km), max(data.km)]
	liney = []
	for m in linex:
		m = t1 * normalize(data.km, m) + t0
		price = denormalize(data.price, m)
		liney.append(price)	

	plt.figure(1)
	plt.plot(data.km, data.price, 'ro', linex, liney, 'g-')
	plt.ylabel('Price')
	plt.xlabel('Mileage')
	plt.figure(2)
	plt.plot(loss_history, 'bo')
	plt.ylabel('loss')
	plt.xlabel('iteration')
	plt.figure(3)
	plt.plot(t0_history, 'bo')
	plt.ylabel('t0')
	plt.xlabel('iteration')
	plt.figure(4)
	plt.plot(t1_history, 'bo')
	plt.ylabel('t1')
	plt.xlabel('iteration')

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
	x = (data.km - minMileage) / (maxMileage - minMileage)
	y = (data.price - minPrice) / (maxPrice - minPrice)

	iteration = 1000
	learningRate = 0.1
	length = len(data)

	t0, t1, t0_history, t1_history, loss_history = gradient_descent(x, y, learningRate, length, iteration)

	with open('theta.csv', 'w') as f:
		string = str("t0,t1\n{},{}\n".format(t0, t1))
		f.write(string)
	
	display(data, t0, t1, t0_history, t1_history, loss_history)

if __name__ == '__main__':
	main()
