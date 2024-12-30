# Example file for Programming Foundations: Algorithms by Joe Marini
# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # TODO: using the brute force method
    # for i in range(0, len(itemlist)-1):
    #     if (itemlist[i] > itemlist[i+1]):
    #         return False
        
    # return True
    
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1)) # this is a more efficient way to check if a list is sorted. It uses the all() function to check if all the elements in the list are sorted in ascending order. If they are, it will    

print(is_sorted(items1))
print(is_sorted(items2))

