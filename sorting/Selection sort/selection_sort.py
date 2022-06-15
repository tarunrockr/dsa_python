# ---------------------- Selection Sort --------------------#

# Unsorted list to be sorted
lst = [5, 3, 1, 9, 8, 2, 4, 7]
print("Unsorted list: ",lst)

# n is the number of elements in the list
n = len(lst)

# Process: we divide intial list into sorted list(blank list) and unsorted list(current list)
# In every round we pick minimum element from the unsorted list and swap it with the first element in unsorted list
# Now we include this first sorted element from unsorted list into sorted list.
  

# ---------- Start ---------- #

def selection_sort(lst):
	for i in range(0, n-1):

		# Initially setting the min with the index of first element in unsorted Array(list)
		min = i 

		# Findout the minimum element from the unsorted list 
		for j in range(i+1, n):

			if lst[j] <  lst[min]:
				min = j

		# If this index is different then replace this with the first element in unsorted list
		if min != i:
			# Swaping the minimun value with the starting element in unsorted Array(list)
			lst[min], lst[i] = lst[i], lst[min] 


# ---------- End ---------- #

selection_sort(lst)
print("Sorted list: ",lst)