#Esta función es lazy, porque no me va regresando todo, sino que para luego de cada iteración.
#Utilizando next, puedo hacer que la función siga hasta que yo quiera. 
def lazy_func(n):
    for i in range(n):
        yield i
x = lazy_func(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
