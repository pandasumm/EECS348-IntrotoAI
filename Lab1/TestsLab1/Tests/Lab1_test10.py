import student_code as sc


def init_map(map_array):
	testmap = []
	for ms in map_array:
		ms_arr = []
		for c in ms:
			ms_arr.append(int(c))
		testmap.append(ms_arr)
	return testmap

def print_map (testmap):
	for lst in testmap:
		print lst
		print '\n'

def check_map_equal (map1, map2):
	flag = True
	for i in range(len(map1)):
		for j in range(len(map1[0])):
			if map1[i][j] != map2[i][j]:
				flag = False
	return flag

def check_score_equal(score1, score2):
	flag = True
	keys1 = score1.keys()
	keys2 = score2.keys()
	if set(keys1) == set(keys2):
		for k in keys1:
			if score1[k] != score2[k]:
				flag = False
	else:
		flag = False
	return flag


def main():
	dis_map = {'Campus': {'Campus': 0, 'Whole_Food': 3, 'Beach': 5, 'Cinema': 5, 'Lighthouse': 1, 'Ryan Field': 2, 'YWCA':12},
				'Whole_Food': {'Campus': 3,  'Whole_Food': 0, 'Beach': 3, 'Cinema': 3, 'Lighthouse': 4, 'Ryan Field': 5, 'YWCA':8},
				'Beach': {'Campus': 5,  'Whole_Food': 3, 'Beach': 0, 'Cinema': 8, 'Lighthouse': 5, 'Ryan Field': 7, 'YWCA':12,},
				'Cinema': {'Campus': 5,  'Whole_Food': 3, 'Beach': 8, 'Cinema': 0, 'Lighthouse': 7, 'Ryan Field': 7, 'YWCA':2},
				'Lighthouse': {'Campus': 1, 'Whole_Food': 4, 'Beach': 5, 'Cinema': 7, 'Lighthouse': 0, 'Ryan Field': 1, 'YWCA':15},
				'Ryan Field': {'Campus': 2, 'Whole_Food': 5, 'Beach': 7, 'Cinema': 7, 'Lighthouse': 1, 'Ryan Field': 0, 'YWCA':12},
				'YWCA': {'Campus': 12, 'Whole_Food': 8, 'Beach': 12, 'Cinema': 2, 'Lighthouse': 15, 'Ryan Field': 12, 'YWCA':0}}
	time_map4 = {'Campus': {'Campus': None, 'Whole_Food': 12, 'Beach': 3, 'Cinema': None, 'Lighthouse': 1, 'Ryan Field': None, 'YWCA': None},
				'Whole_Food': {'Campus': 4,  'Whole_Food': None, 'Beach': 4, 'Cinema': 13, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
				'Beach': {'Campus': 4,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
				'Cinema': {'Campus': None,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': 2},
				'Lighthouse': {'Campus': 1, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': 1, 'YWCA': None},
				'Ryan Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 2, 'Ryan Field': None, 'YWCA': 17},
				'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 3, 'Lighthouse': None, 'Ryan Field': 5, 'YWCA': None}}
	student_score4 = sc.a_star_search(dis_map,time_map4, 'Campus', 'Cinema')
	gold_score4 = {'Ryan Field': {'YWCA': 21, 'Lighthouse': 11}, 'Whole_Food': {'Beach': 19, 'Campus': 16, 'Cinema': 20}, 'Lighthouse': {'Ryan Field': 9, 'Campus': 7}, 'Beach': {'Whole_Food': 10, 'Campus': 12}, 'Campus': {'Lighthouse': 8, 'Beach': 11, 'Whole_Food': 15}}
	if check_score_equal(student_score4,gold_score4):
		print "pass A* search for time map4"
	else:
		print "Fail A* search for time map4"
		exit(1)
	exit(0)

if __name__== "__main__":
	main()