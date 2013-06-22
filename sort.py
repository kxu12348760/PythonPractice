# Simple insertion sort
def insertion_sort(array):
	arrayLength = len(array)
	for i in range(1, arrayLength):
		item = array[i]
		j = i - 1
		while j >= 0 and array[j] > item:
			array[j + 1] = array[j]
			j = j - 1
		array[j + 1] = item
	return array

# Iterative bottom-up mergesort
def merge_sort(array):
	mergeLength = 1
	arrayLength = len(array)
	while (mergeLength <= arrayLength):
		if (mergeLength > arrayLength):
			mergeLength = arrayLength
		start = 0
		while (start < arrayLength):
			end = start + mergeLength - 1
			if (end >= arrayLength):
				end = arrayLength - 1
			middle = (start + end) / 2
			merge(array, start, middle, end)
			start = end + 1
		mergeLength *= 2
	return array

# Merge helper function
def merge(someArray, start, middle, end):
	arrayLen = len(someArray)
	if (start < end):
		left = start
		right = middle + 1
		newLength = end - start + 1
		newArray = [0] * newLength
		newArrayIdx = 0
		while (newArrayIdx < newLength):
			leftElm = someArray[left]
			if (right < arrayLen):
				rightElm = someArray[right]
			if (leftElm < rightElm or right > end):
				newArray[newArrayIdx] = leftElm
				left += 1
			else:
				newArray[newArrayIdx] = rightElm
				right += 1
			newArrayIdx += 1
		for i in range(0, newLength):
			someArray[i + start] = newArray[i]


