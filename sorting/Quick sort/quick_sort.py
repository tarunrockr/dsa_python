# ---------------------- Quick Sort --------------------#

# Unsorted list to be sorted
lst = [7, 6, 10, 9, 5, 9, 2, 1, 15, 7]
print("Unsorted list: ",lst)

# n is the number of elements in the list
n = len(lst)

# ---------- Start ---------- #

# Partition method divides a list into to sub list based on pivot element 
# Where one sublist will contain elements less than or equal to pivot element or other sublist will contain elements greater than pivot element
# Here lb = 'Lower bound' and ub = 'upper bound'
def partition(arr, lb, ub):

	# We can take any element as pivot element
	pivot = arr[lb]
	start = lb 
	end   = ub

	while start < end:

		while (arr[start] <= pivot) and (start <= ub):
			start += 1
            # if start will be greter than upper bound index then IndexError can generate
			if start > ub:
				break

		while arr[end] > pivot:
			end -= 1
			# if end will be smaller than lower bound index then IndexError can generate
			if end < lb:
				break

		# swap a[start] and a[end] only when start is less than end
		if start < end:
			arr[start] , arr[end] = arr[end] , arr[start]

	# Swap pivot element with a[end]
	arr[lb] , arr[end] = arr[end] , arr[lb]

	return end


# Quick sort function
def quick_sort(arr, lb, ub):

	if lb < ub:

		pivot_index = partition(arr, lb, ub)
		quick_sort(arr, lb, pivot_index-1)
		quick_sort(arr, pivot_index+1, ub)

# ---------- End ---------- #

quick_sort(lst, 0, n-1)
print("Sorted list: ",lst)