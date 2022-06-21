# ---------------------- Merge Sort --------------------#

# Unsorted list to be sorted
lst = [5, 3, 1, 9, 8, 2, 4, 7]
print("Unsorted list: ",lst)
print("-------------------------")

# n is the number of elements in the list
n = len(lst)

# In merge sort we divide whole array(list) into subarray(sublist) on the basis of mid index until we got only one element in each sublist 
# Then we create a sorted list by combining these sublist by using merge function

# Merging the element in sorted order
def merge(arr, lb, mid, ub):    

    left_count  = mid-lb+1
    right_count = ub-mid

	# create temp arrays(list) with the number of element to left and right
    L = [0] * (left_count)
    R = [0] * (right_count)

    # Copying data to both temporary list
    for i in range(0, left_count):
    	L[i] = arr[lb+i]

    for j in range(0, right_count):
    	R[j] = arr[mid+1+j]

    i = 0
    j = 0
    k = lb

    print("Left List for merge:",L)
    print("Left Count: ",left_count)
    print("Right List for merge:",R)
    print("Right Count: ",right_count)

    while i < left_count and j<right_count:

    	if L[i]<=R[j]:
    		arr[k] = L[i]
    		i += 1
    	else:
    		arr[k] = R[j]
    		j += 1
    	k += 1

    if i<left_count :
    	while i<left_count:
    		arr[k] = L[i]
    		i += 1
    		k += 1
    else:
    	while j<right_count:
    		arr[k] = R[j]
    		j += 1
    		k += 1

    print("Main list after merge function operation: ", arr)
    print("-----------")

# Here lb = 'Lower bound' and ub = 'Upper bound'
def merge_sort(arr, lb, ub):
	if lb < ub:
		mid = (lb+ub)//2
		merge_sort(arr, lb, mid)
		merge_sort(arr, mid+1, ub)
		merge(arr, lb, mid, ub)

# ---------- End ---------- #

merge_sort(lst, 0, n-1)
print("Sorted list: ",lst)