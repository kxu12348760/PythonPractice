from sort import insertion_sort
from sort import merge_sort

def perform(someFunc, *args):
	print "Calling {0} with args {1}".format(someFunc.__name__, *args)
	print "Result {0}".format(someFunc(*args))

def main(argv = None):
	perform(insertion_sort, [5, 3, 8, 10, 52, 17, 1])
	perform(merge_sort, [5, 3, 8, 10, 52, 17, 1])
	perform(merge_sort, [1])
	perform(merge_sort, [-50, 2, 4, 1000])

if __name__ == "__main__":
	main()
