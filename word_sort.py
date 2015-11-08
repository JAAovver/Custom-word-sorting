def read_words(words_file):
    return [line[0:3] for line in open(words_file, 'r')]
def getnumKey(item):
	return sum([(ord(elem)-96) for elem in item])
def getstrKey(item):
	pow26 = [1,0.038461538464,0.0014792899408284023,5.689576695493855e-05,2.1882987290360982e-06,8.416533573215762e-08,3.2371282973906776e-09,1.2450493451502607e-10]
	numstr = 0
	for i in range(len(item)):
		numstr+=(ord(item[i])-96)*pow26[i]
	return numstr
def myfunc(names):
	sizes = [getnumKey(name) for name in names]
	lexes = [getstrKey(name) for name in names]
	info = zip(names,sizes,lexes)
	info.sort(key = lambda x : (-x[1], -x[2]))
	return [infos[0] for infos in info]

names = read_words('some_file.txt')

print myfunc(names)
