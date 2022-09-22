sc = lambda a: a + 15
print(sc(10))

sc = lambda x, y: x * y
print(sc(6, 8))


def myfunction(n):
    return lambda a: a * n


double = myfunction(2)
print(double(15))

triple = myfunction(3)
print(triple(15))

quadruple = myfunction(4)
print(quadruple(15))

quintuple = myfunction(5)
print(quintuple(15))

lst = [("English", 88), ("Science", 90), ('Maths', 97), ('Social sciences', 82)]
print("original list of tuples: ", lst)

lst.sort(key=lambda x: x[1])
print(lst)

dst = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
       {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
       {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

dst = sorted(dst, key=lambda x: x["color"])
print(dst)


fruits = "apple pear cucumber mango grape water_melon".split()
print(max(fruits))
print(min(fruits))
print(min(fruits, key=len))
print(max(fruits, key=lambda x: x[-1]))
print(max(fruits, key=lambda x: x[-3:]))
print(sorted(fruits, reverse=True))


