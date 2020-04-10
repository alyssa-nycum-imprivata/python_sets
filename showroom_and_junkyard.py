showroom = set()

showroom.add("civic")
showroom.add("beetle")
showroom.add("cherokee")
showroom.add("camry")

# print(showroom)
print(len(showroom))

# showroom.add("civic")
# print(showroom)

showroom.update({"accord", "corolla"})

# print(showroom)

showroom.discard("beetle")

print(showroom)

junkyard = {"accord", "camry", "cherokee", "jetta", "rabbit", "rangler"}

print(junkyard)

cars_in_common = junkyard.intersection(showroom)

print(cars_in_common)

showroom = showroom.union(junkyard)

# print(showroom)

showroom.discard("rabbit")

print(showroom)


