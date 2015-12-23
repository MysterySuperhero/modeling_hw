import collections
from tools import *

__author__ = 'dmitri'


def main():
	u = {
		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0,
		'e': 0,
		'f': 0}
	u = collections.OrderedDict(sorted(u.items()))

	v = {
		'g': 0,
		'h': 0,
		'i': 0,
		'j': 0,
		'k': 0,
		'l': 0,
		'm': 0}
	v = collections.OrderedDict(sorted(v.items()))

	prev = v.copy()

	initialization(u)

	iterations(u, v, prev)

	print("Steady vector: ", end="")
	print_vector(v)

	return


def initialization(u):
	print("Please, input (a, b, c, d, e, f): ")

	for x in u.items():
		print(str(x[0]) + ": ", end="")
		u[x[0]] = input()
	return


def iterations(u, v, prev):
	iteration_os(u, v, prev)
	print_info(u, v, prev)
	while v != prev:
		prev = v.copy()
		v = iteration_os(u, v, prev)
		print_info(u, v, prev)
	return


def print_info(u, v, prev):
	print("Iteration: \n")
	print("U vector: ", end="")
	print_vector(u)
	print("\n")
	print("Previous V vector: ", end="")
	print_vector(prev)
	print("\n")
	print("V vector: ", end="")
	print_vector(v)
	print("\n")
	print("\n")
	return


main()
