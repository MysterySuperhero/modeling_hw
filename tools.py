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
