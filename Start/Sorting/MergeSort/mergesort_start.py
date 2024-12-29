# Example file for Programming Foundations: Algorithms by Joe Marini
# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid] # left half of the array
        rightarr = dataset[mid:] # right half of the array

        # TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]: # if the left array value is less than the right array value
                dataset[k] = leftarr[i] # set the dataset value to the left array value
                i += 1
            else:
                dataset[k] = rightarr[j] # set the dataset value to the right array value
                j += 1
            k += 1

        # TODO: if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # TODO: if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


# test the merge sort with data
print(items)
mergesort(items)
print(items)
