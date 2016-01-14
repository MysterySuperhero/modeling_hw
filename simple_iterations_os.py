from tools import *
from schemes import print_scheme_os
__author__ = 'dmitri'


def main():
	# проинициализируем векторы U и V
	# т.е. векторы входных и остальных переменных соответственно
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

	# вектор предыдущих значений остальных переменных
	prev = v.copy()

	# просим пользователя задать вектор входных значений
	initialization(u)

	# запустим итерационный цикл
	result = iterations(u, v, prev)

	# удалось получить установившееся состояние?
	if result == 0:
		print("Steady vector: ", end="")
		print_vector(v)
	else:
		print("Can't get steady vector!")

	return


# фукнция ввода вектора входных значений
def initialization(u):
	print_scheme_os()
	print("Please, input (a, b, c, d, e, f): ")

	for x in u.items():
		print(str(x[0]) + ": ", end="")
		u[x[0]] = input()
	return


# функция, получения установишегося состояния
def iterations(u, v, prev):
	iteration_os(u, v, prev)
	print_info(u, v, prev)
	steps_count = 0
	while (v != prev) and (steps_count < 30):
		prev = v.copy()
		v = iteration_os(u, v, prev)
		print_info(u, v, prev)
		steps_count += 1
	return 0 if steps_count != 30 else 1


# вывод на экран информации об итерации
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
