from tools import *

__author__ = 'dmitri'


def get_nvectors(u, v, prev):
	vec = []
	vv = v.copy()
	for i in range(0, 64):
		prev = v.copy()
		steady_vector(u, v, prev)
		vec.append(v)
		v = vv.copy()
		increment_u(u)

	return vec


def get_fvectors(u, v, prev, key, value=int):
	vec = []
	vv = v.copy()
	for i in range(0, 64):
		prev = v.copy()
		steady_vector(u, v, prev)
		v[key] = value
		prev[key] = value
		vec.append(v)
		v = vv.copy()
		increment_u(u)

	return vec


def init_u():
	u = {
		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0,
		'e': 0,
		'f': 0}
	u = collections.OrderedDict(sorted(u.items()))
	return u


def init_v():
	v = {
		'g': 0,
		'h': 0,
		'i': 0,
		'j': 0,
		'k': 0,
		'l': 0,
		'm': 0}
	v = collections.OrderedDict(sorted(v.items()))
	return v


def find_differences(normal=list, fixed=list):
	x = 0
	while x < len(normal):
		if not comp(normal[x], fixed[x]):
			print("Set number: " + str(x))
		x += 1
	return


def print_vector_collections(collection=list):
	x = 0
	while x < len(collection):
		print(collection[x])
		x += 1
	return


def main():
	u = init_u()
	v = init_v()
	prev = v.copy()

	normal = get_nvectors(u, v, prev)

	u = init_u()
	v = init_v()
	prev = v.copy()

	print("Input line key and it's value: ")
	print("Key: ", end="")
	key = input()
	print("Value: ", end="")
	value = input()

	v[key] = value

	fixed = get_fvectors(u, v, prev, key, int(value))

	find_differences(normal, fixed)

	return


main()
