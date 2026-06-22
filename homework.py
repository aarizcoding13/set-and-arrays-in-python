setx = {1 , 3 , 4 , 3 , 9}
sety = {2 , 4 , 3 , 4 , 6}


setz = setx.intersection(sety)
print(setz)

setz = setx.union(sety)
print(setz)

setz = setx.difference(sety)
print(setz)

setz = setx.symmetric_difference(sety)
print(setz)