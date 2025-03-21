my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1,15)
another_list = [50,60,70]
my_list.extend(another_list)
del my_list[-1]
n = len(my_list)
for i in range(n):  
    swapped = False
    for j in range(0, n - i - 1):  
        if my_list[j] > my_list[j + 1]:  
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]  # Swap elements
            swapped = True
        if not swapped:  # If no swaps occurred, the list is sorted
            break
print(my_list)
print(my_list.index(30))