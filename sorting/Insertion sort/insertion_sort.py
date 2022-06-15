# ---------------------- Inserion Sort --------------------#

# Unsorted list to be sorted
lst = [5, 3, 1, 9, 8, 2, 4, 7]
print("Unsorted list: ",lst)

# n is the number of elements in the list
n = len(lst)


# In insertion sort we divide main array(list) into two sublist. 
# 1st is sorted list by taking 1st element(0 th index element) of array(list)
# 2nd is unsorted array(list) by taking remaining elements(from 1st index to last index) of array(list)
# In each round we pick first element from array(list) and insert in sorted array(list) at appropriate place

# ---------- Start ---------- #

def insertion_sort(lst):
	for i in range(1, n):

		# temp is the element that need to be insert in the sorted array(list)
		temp = lst[i]

		# j is the last element of sorted list
		j    = i-1

		# While loop will continue to run until we reach at the end of loop or find a element which is less than temp element 
		while j >= 0 and lst[j] > temp :

			lst[j+1] = lst[j]
			j -= 1

		# Insert the temp at the appropriate index
		lst[j+1] = temp

# ---------- End ---------- #

insertion_sort(lst)
print("Sorted list: ",lst)


