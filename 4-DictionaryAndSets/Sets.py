#set are mutable but the elements of a set must be immutable


collection ={1,2,3,4}

print(type(collection))
print(collection)

#for defining empty set use set() not {}
empty_set = set()

#methods of set
set.add(el)
set.remove(el)
set.discard(el)
set.clear()
set.pop()  # removes and returns an arbitrary element