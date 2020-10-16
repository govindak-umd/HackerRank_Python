from cmath import phase

complx = complex(input())
x = complx.real
y = complx.imag
mod = (x ** 2 + y ** 2) ** 0.5
print(mod)
phs = phase(complex(x, y))
print(phs)
