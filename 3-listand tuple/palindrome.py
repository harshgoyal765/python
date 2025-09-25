list1=[1,2,1]
#list2=[1,2,3]

copy_list = list1.copy()  # Creating a shallow copy of the list
copy_list.reverse()

if(copy_list == list1):
    print("list are palindrome")
else:
    print("list are not palindrome")
