#!/usr/bin/python3
import sys

def parse(s):
	tab = s.partition(',')
	if not tab[1]:
		exit("Error: It seems you don't have correctly formated value in theta.txt . t0,t1.")
	try:
		t0 = float(tab[0])
		t1 = float(tab[2])
	except Exception as e:
		exit("Error: {}".format(e))
	return t0, t1

def main():
	fileNameToRead = "theta.txt"
	t0 = 0
	t1 = 0
	try:
		with open(fileNameToRead, 'r') as f:
			s = f.readline()
		t0, t1 = parse(s)
	except Exception as e:
		print("Error: {}\nSo we use t0 = 0 and t1 = 0\n".format(e))
	mileage = input("Please enter a mileage :\n")
	try:
		mileage = float(mileage)
	except Exception as e:
		exit("Error: {}".format(e))
	print("Estimate price :")
	print(t0 + (t1 * mileage))

if __name__ == '__main__':
	main()
