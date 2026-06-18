setx = {"green","blue"}
sety = {"blue", "yellow"}


setz = setx.intersection(sety)
print(setz)

setz = setx.union(sety)
print(setz)

setz = setx.difference(sety)
print(setz)

setz = setx.symmetric_difference(sety)
print(setz)