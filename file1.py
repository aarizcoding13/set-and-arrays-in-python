my_set = {1 , 2 , 3}
print(my_set)
# 1) Create a set `my_set` containing integers {1, 2, 3}

# and print the set.

# 2) Create a set `my_set` containing mixed data types:
tup1 = {1.0,"hello" , (1 , 2 , 3)}
print(tup1)

# a) a float (1.0)

# b) a string ("Hello")

# c) a tuple (1, 2, 3)

# and print the set.

# 3) Create a set `my_set` with duplicate values {1, 2, 3, 4, 3, 2}.
my_set = {1 , 2 , 3 , 4 , 3 , 2}
print(my_set)
# (Sets automatically remove duplicates.)

# Print the set to show only unique elements.

# 4) Create a set from a list using `set([...])`:
a = set([1 , 2 , 3 , 2])
print(a,"\n") 
# a) Convert the list [1, 2, 3, 2] into a set.

# b) Print the set and a newline.

# 5) Create a set `num_set` from the list [0, 1, 3, 4, 5]
num_set = set([0 , 1 , 3 , 4 , 5])
print(num_set)
num_set.pop()
print(num_set)
# and print it as the original set.

# 6) Remove an element from the set using `pop()`:

# a) `pop()` removes a random/first element depending on internal ordering.

# b) Print the set after removal.