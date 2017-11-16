#!/usr/bin/python3
import sys
import pandas as pd



def main():
	data = []
	t0 = 0
	t1 = 0
	try:
		data = pd.read_csv("data.csv", dtype = "float")
	except Exception as e:
		exit(e)

	try:
		theta = pd.read_csv("theta.csv")
		t0 = float(theta.t0)
		t1 = float(theta.t1)
	except:
		t0 = 0
		t1 = 0

	mileage = input("Please enter a mileage :\n")
	try:
		mileage = float(mileage)
		mileage = (mileage - min(data.km)) / (max(data.km) - min(data.km))
	except Exception as e:
		exit(e)

	print("Estimate price :")
	price = t1 * mileage + t0
	price = price * (max(data.price) - min(data.price)) + min(data.price)
	print(price)


if __name__ == '__main__':
	main()
