from tools import *

__author__ = 'dmitri'


def main():
	print("Choose alphabet: ") # просим пользователя выбрать алфавит
	alphabet = input()

	u_risky = {
		'a': 2,
		'b': 2,
		'c': 2,
		'd': 2,
		'e': 2,
		'f': 2}
	u_risky = collections.OrderedDict(sorted(u_risky.items()))
	if alphabet == 5:
		get_u_risky_5(u_risky)

	modeling(u_risky, alphabet)


def modeling(u_risky, alphabet):
	u = {
		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0,
		'e': 0,
		'f': 0}
	u = collections.OrderedDict(sorted(u.items()))

	for i in range(0, 64):
		u_inv = get_inverted_vector(u)

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
		v_risky = v.copy()
		v_inv = v.copy()

		steady_vector(u, v, prev)
		steady_vector(u_risky, v_risky, prev)
		steady_vector(u_inv, v_inv, prev)

		print_info(u, u_inv, v, v_risky, v_inv)

		check_faults(v, v_risky, v_inv, alphabet)

		print("\n")

		increment_u(u)

	return


def print_info(u, u_inv, v, v_r, v_i):
	print("U: ")
	print_vector(u)
	print("\n")
	print("U inverted: ")
	print_vector(u_inv)
	print("\n")
	print("Normal V: ")
	print_vector(v)
	print("\n")
	print("Risky V: ")
	print_vector(v_r)
	print("\n")
	print("Inverted V: ")
	print_vector(v_i)
	print("\n")
	return


main()
