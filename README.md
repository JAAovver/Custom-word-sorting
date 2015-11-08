# Custom-word-sorting

Sort a list of words by two features: the numeric sum of the constituent letters and in the event of a tie, alphabetical. Both are sorted in reverse order.

This function returns the numeric sum of letters:

```
def getnumKey(item):
	return sum([(ord(elem)-96) for elem in item])
```

This function returns a unique number for each word (in this case of length guaranteed to be < 8) corresponding to its alphabetical ordering:

```
def getstrKey(item):
	pow26 = [1,0.038461538464,0.0014792899408284023,5.689576695493855e-05,2.1882987290360982e-06,8.416533573215762e-08,3.2371282973906776e-09,1.2450493451502607e-10]
	numstr = 0
	for i in range(len(item)):
		numstr+=(ord(item[i])-96)*pow26[i]
	return numstr
```

I defined pow26 rather than calculating pow(26,x) to save on time, and used the for loop rather than list comprehension because I found it to be faster in this case. 

The function below applies the two sorting functions to a list of words.

```
def myfunc(names):
	sizes = [getnumKey(name) for name in names]
	lexes = [getstrKey(name) for name in names]
	info = zip(names,sizes,lexes)
	info.sort(key = lambda x : (-x[1], -x[2]))
	return [infos[0] for infos in info]
```




