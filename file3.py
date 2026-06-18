import array as arr
num = arr.array("i", [1,3,5,3,7,9,3])
print("the original array is " +str(num))
print("number of occurrences of the number 3 in the said array is " +str(num.count(3)))

num.reverse()
print(str(num))
