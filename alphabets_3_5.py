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

	u_inv = get_inverted_vector(u)

	u_risky = {
		'a': 2,
		'b': 2,
		'c': 2,
		'd': 2,
		'e': 2,
		'f': 2}
	u_risky = collections.OrderedDict(sorted(u_risky.items()))

	for i in range(0, 64):
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

		print_info(u, v, v_risky, v_inv)

		check_faults(v, v_risky, v_inv, 3)

		print("\n")

		increment_u(u)

	return


def print_info(u, v, v_r, v_i):
	print("U: ")
	print_vector(u)
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