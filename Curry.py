#curry: pasar parcialmente valores (variables)
def sum(x):
    def sum_y(y):
        return x + y
    return sum_y

print(sum(5)(4))

#add5 me sirve para reutilizarlo.
add5 = sum(5)
print(add5(4))

