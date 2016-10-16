lst = input("What's the list?\n")
lst = lst.replace(",", "")
lst = lst.replace(" ", ", ")

lst = list(eval(lst))
og = list(lst)
lst = sorted(lst)
s = statistics

def mean():
	return sum(lst) / len(lst)

def standev():
	avg = mean()
	sum = 0
	for num in lst:
		sum += (num - avg) ** 2
	sum /= len(lst)
	return sum **.5

def variance():
	return standev()**2

def quartile(n):
	return lst[int((len(lst) - 1) * n)]

def median():
	assert(s.median_low(lst) == quartile(.5))
	return quartile(.5)

def rng():
	return max(lst) - min(lst)

def rms():
	sum = 0
	for num in lst:
		sum += num*num
	sum /= len(lst)
	return sum**.5

def lq():
	return quartile(.25)

def uq():
	return quartile(.75)

print("\n")
print("Sorted Data: " + str(lst))
print("standev: " + str(round(standev(), 3)))
print("variance: " + str(round(variance(), 3)))
print("rms: " + str(round(rms(), 3)))
print("range: " + str(round(rng(), 3)))
print("mean: " + str(round(mean(), 3)))
m = mean()
sd = standev()
print("Z-Score: " + str([round(((x - m) / sd), 3) for x in og]))
print("\n")
print("5 number summary for box plot")
print("-----------------")
print("min: " + str(min(lst)))
print("lq: " + str(lq()))
print("median: " + str(median()))
print("uq: " + str(uq()))
print("max: " + str(max(lst)))
