__author__ = 'dmitri'

disjunction = [[0, 1, 2, 3, 4],
               [1, 1, 1, 1, 1],
               [2, 1, 2, 2, 2],
               [3, 1, 2, 3, 2],
               [4, 1, 2, 2, 4]]

conjunction = [[0, 0, 0, 0, 0],
               [0, 1, 2, 3, 4],
               [0, 2, 2, 2, 2],
               [0, 3, 2, 3, 2],
               [0, 4, 2, 2, 4]]

invertion = [1, 0, 2, 4, 3]

errors_three = {
	'020': 'static',
	'121': 'static'}

errors_five = {
	'020': 'static',
	'121': 'static',
	'021': 'dynamic',
	'120': 'dynamic'}


def invert(param):
	return invertion[param]


def g(b, c):
	return invert(conjunction[int(b)][int(c)])


def h_os(c, d, l):
	return invert(conjunction[conjunction[int(c)][int(d)]][int(l)])


def h(c, d):
	return invert(conjunction[int(c)][(d)])


def i(a, g):
	return invert(conjunction[int(a)][int(g)])


def j(h, e):
	return invert(conjunction[int(h)][int(e)])


def k(i, j):
	return conjunction[int(i)][int(j)]


def l(j, f):
	return invert(conjunction[int(j)][int(f)])


def m(k, l):
	return invert(disjunction[int(k)][int(l)])


def iteration_os(u, v, prev):
	v['g'] = g(u['b'], u['c'])
	v['h'] = h_os(u['c'], u['d'], prev['l'])
	v['i'] = i(u['a'], prev['g'])
	v['j'] = j(prev['h'], u['e'])
	v['k'] = k(prev['i'], prev['j'])
	v['l'] = l(prev['j'], u['f'])
	v['m'] = m(prev['k'], prev['l'])
	return v


def print_vector(v):
	for x in v.items():
		print(str(x[0]) + ": " + str(x[1]) + ", ", end="")
	return
