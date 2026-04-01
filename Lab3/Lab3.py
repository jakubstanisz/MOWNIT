import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

t = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980], dtype=float)
y = np.array([76212168, 92228496, 106021537, 123202624, 132164569, 151325798, 179323175, 203302031, 226542199], dtype=float)

V1 = np.vander(t, increasing=True)
V2 = np.vander(t - 1900, increasing=True)
V3 = np.vander(t - 1940, increasing=True)
V4 = np.vander((t - 1940) / 40, increasing=True)

cond1 = np.linalg.cond(V1)
cond2 = np.linalg.cond(V2)
cond3 = np.linalg.cond(V3)
cond4 = np.linalg.cond(V4)

print(f"Baza 1: {cond1}")
print(f"Baza 2: {cond2}")
print(f"Baza 3: {cond3}")
print(f"Baza 4: {cond4}")

c4 = np.linalg.solve(V4, y)

def horner(coeffs, x):
    result = coeffs[-1]
    for i in range(len(coeffs) - 2, -1, -1):
        result = result * x + coeffs[i]
    return result

t_eval = np.arange(1900, 1991, 1)
x_eval = (t_eval - 1940) / 40
y_eval = horner(c4, x_eval)

plt.figure(figsize=(10, 6))
plt.plot(t_eval, y_eval, label="Wielomian interpolacyjny", color="blue")
plt.scatter(t, y, color="red", zorder=5, label="Węzły interpolacji")
plt.title("Interpolacja populacji USA")
plt.xlabel("Rok")
plt.ylabel("Populacja")
plt.legend()
plt.grid(True)
plt.show()

x_1990 = (1990 - 1940) / 40
y_1990_ext = horner(c4, x_1990)
y_1990_true = 248709873

error_1990 = np.abs(y_1990_ext - y_1990_true) / y_1990_true
print(f"Wynik ekstrapolacji (1990): {y_1990_ext:.0f}")
print(f"Błąd względny: {error_1990:.4%}")

poly_lagrange = lagrange(t, y)
y_lagrange_eval = poly_lagrange(t_eval)

def divided_differences(x_nodes, y_nodes):
    n = len(y_nodes)
    coef = np.zeros([n, n])
    coef[:,0] = y_nodes
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x_nodes[i+j] - x_nodes[i])
    return coef[0, :]

def newton_poly(coef, x_nodes, x_val):
    n = len(x_nodes) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x_val - x_nodes[n - k]) * p
    return p

coef_newton = divided_differences(t, y)
y_newton_eval = newton_poly(coef_newton, t, t_eval)

y_rounded = np.round(y / 1000000) * 1000000
c4_rounded = np.linalg.solve(V4, y_rounded)

print("Współczynniki oryginalne:", c4)
print("Współczynniki po zaokrągleniu:", c4_rounded)

y_1990_rounded_ext = horner(c4_rounded, x_1990)
error_1990_rounded = np.abs(y_1990_rounded_ext - y_1990_true) / y_1990_true

print(f"Błąd względny po zaokrągleniu: {error_1990_rounded:.4%}")

t2 = np.array([1965, 1970, 1980, 1985, 1990, 1991], dtype=float)
y2 = np.array([17769, 24001, 25961, 34336, 29036, 33417], dtype=float)
t2_pred = np.array([1962, 1977, 1992], dtype=float)
y2_true = np.array([12380, 27403, 32059], dtype=float)

cs_not_a_knot = CubicSpline(t2, y2, bc_type='not-a-knot')
cs_natural = CubicSpline(t2, y2, bc_type='natural')
cs_clamped = CubicSpline(t2, y2, bc_type='clamped')

y2_pred_nak = cs_not_a_knot(t2_pred)
y2_pred_nat = cs_natural(t2_pred)
y2_pred_clam = cs_clamped(t2_pred)

poly2_lagrange = lagrange(t2, y2)
y2_pred_lagrange = poly2_lagrange(t2_pred)

err_nak = np.abs(y2_pred_nak - y2_true) / y2_true
err_nat = np.abs(y2_pred_nat - y2_true) / y2_true
err_clam = np.abs(y2_pred_clam - y2_true) / y2_true
err_lag = np.abs(y2_pred_lagrange - y2_true) / y2_true

print("Błędy względne dla poszczególnych metod:")
print(f"Splajn 'not-a-knot': {err_nak}")
print(f"Splajn naturalny: {err_nat}")
print(f"Splajn 'clamped': {err_clam}")
print(f"Wielomian Lagrange'a: {err_lag}")

plt.figure(figsize=(10, 6))


t2_dense = np.linspace(1965, 1991, 300)

# wykresy splajnów
plt.plot(t2_dense, cs_not_a_knot(t2_dense), label="not-a-knot")
plt.plot(t2_dense, cs_natural(t2_dense), label="natural")
plt.plot(t2_dense, cs_clamped(t2_dense), label="clamped")

# wielomian Lagrange'a
plt.plot(t2_dense, poly2_lagrange(t2_dense), linestyle="--", label="Lagrange")

# punkty danych
plt.scatter(t2, y2, color="black", zorder=5, label="Dane")

# punkty predykcji
plt.scatter(t2_pred, y2_true, color="red", label="Wartości rzeczywiste")

plt.title("Interpolacja produkcji cytrusów we Włoszech")
plt.xlabel("Rok")
plt.ylabel("Produkcja")
plt.legend()
plt.grid(True)

plt.savefig("wykres_cytrusy.png", dpi=300)
plt.show()