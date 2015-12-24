import collections

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


def iteration(u, v, prev):
    v['g'] = g(u['b'], u['c'])
    v['h'] = h(u['c'], u['d'])
    v['i'] = i(u['a'], prev['g'])
    v['j'] = j(prev['h'], u['e'])
    v['k'] = k(prev['i'], prev['j'])
    v['l'] = l(prev['j'], u['f'])
    v['m'] = m(prev['k'], prev['l'])
    return v


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


def get_inverted_vector(vector=collections.OrderedDict):
    inverted_vector = collections.OrderedDict({})
    for el in vector.items():
        inverted_vector[el[0]] = invertion[el[1]]
    return inverted_vector


def check_faults(v=collections.OrderedDict, v_r=collections.OrderedDict, v_i=collections.OrderedDict, alphabet=int):
    errors = errors_three if alphabet == 3 else errors_five
    keys = v.keys()
    for key in keys:
        s = str(v[key]) + str(v_r[key]) + str(v_i[key])
        if s in errors:
            print(str(errors[s]) + " error " + str(s))
    return


def steady_vector(u, v, prev):
    iteration(u, v, prev)
    steps_count = 0
    while (v != prev) and (steps_count < 30):
        prev = v.copy()
        v = iteration(u, v, prev)
        steps_count += 1
    return 0 if steps_count != 30 else 1


def increment_u(u):
    if u['a'] == 0:
        u['a'] = 1
        return
    else:
        if u['b'] == 0:
            u['b'] = 1
            u['a'] = 0
            return
        else:
            if u['c'] == 0:
                u['c'] = 1
                u['a'] = 0
                u['b'] = 0
                return
            else:
                if u['d'] == 0:
                    u['d'] = 1
                    u['c'] = 0
                    u['a'] = 0
                    u['b'] = 0
                    return
                else:
                    if u['e'] == 0:
                        u['e'] = 1
                        u['d'] = 0
                        u['c'] = 0
                        u['a'] = 0
                        u['b'] = 0
                        return
                    else:
                        if u['f'] == 0:
                            u['f'] = 1
                            u['e'] = 0
                            u['d'] = 0
                            u['c'] = 0
                            u['a'] = 0
                            u['b'] = 0
                            return
