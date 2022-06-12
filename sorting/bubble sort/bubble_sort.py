# ---------------------- Bubble Sort --------------------#

# Unsorted list to be sorted
lst = [5, 3, 1, 9, 8, 2, 4, 7]
print("Unsorted list: ",lst)

# n is the number of elements in the list
n = len(lst)


# --- Start --- #
def bubble_sort(lst):
	# for n number of elements there is need n-1 comparisions to sort the list (last remaining element will always be in sorted order)
	for i in range(0, n-1):
		# In each comparision the largest element will pop out in right side so number of comparision will reduce in round so (n-1)-i
		for j in range(0, n-1-i):
			# Swaping the values if lst[j] > lst[j+1]

			# # Swap way 1
			# if lst[j] > lst[j+1]:
			# 	temp     = lst[j]
			# 	lst[j]   = lst[j+1]
			# 	lst[j+1] = temp

			# Swap way 2
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1]  = lst[j+1], lst[j]

# --- End --- #

bubble_sort(lst)
print("Sorted list: ",lst)

