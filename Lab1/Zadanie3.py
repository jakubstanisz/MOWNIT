import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    if x == 0:
        return 1.0
    return (np.exp(x) - 1.0) / x

def f2(x):
    y = np.exp(x)
    if y == 1.0:
        return 1.0
    return (y - 1.0) / np.log(y)

def f3(x):
    return 1.0 + x/2.0 + (x**2)/6.0 + (x**3)/24.0

def f4(x):
    if x == 0:
        return 1.0
    return np.expm1(x) / x

k_vals = np.arange(0, 17)
x_vals = 10.0**(-k_vals)

res1 = [f1(x) for x in x_vals]
res2 = [f2(x) for x in x_vals]
res3 = [f3(x) for x in x_vals]
res4 = [f4(x) for x in x_vals]

print(f"{'k':>2} | {'x':>7} | {'Wzor (5)':>12} | {'Wzor (8)':>12} | {'Taylor':>12} | {'expm1':>12}")
print("-" * 75)
for k, x, r1, r2, r3, r4 in zip(k_vals, x_vals, res1, res2, res3, res4):
    print(f"{k:2} | {x:7.1e} | {r1:12.10f} | {r2:12.10f} | {r3:12.10f} | {r4:12.10f}")

plt.figure(figsize=(12, 7))
plt.semilogx(x_vals, res1, 'o-', label='Wzór (5): (exp(x)-1)/x')
plt.semilogx(x_vals, res2, 's--', label='Wzór (8): (y-1)/log(y)')
plt.semilogx(x_vals, res3, 'x:', label='Szereg Taylora (4 wyrazy)')
plt.semilogx(x_vals, res4, 'd-.', label='Funkcja expm1(x)/x', alpha=0.6)

plt.axhline(1.0, color='black', lw=0.5, ls='--')
plt.xlabel('x (skala logarytmiczna)')
plt.ylabel('Wartość f(x)')
plt.title('Porównanie metod obliczania f(x) = (e^x - 1)/x dla małych x')
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.gca().invert_xaxis()
plt.show()