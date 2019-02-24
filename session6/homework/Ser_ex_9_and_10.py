def get_even_list(lists):
    new_list = []
    for i in lists:
        if i%2 == 0:
            new_list.append(i)
    return new_list

a = [1,2,3,4,5,6,7,8]
t = get_even_list(a)
print(t)

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
