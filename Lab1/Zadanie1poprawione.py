import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.tan(x)

def df_exact(x):
    return 1.0 + np.tan(x)**2

def d2f_exact(x):
    cos_x = np.cos(x)
    return 2.0 * np.sin(x) / (cos_x**3)

def d3f_exact(x):
    cos_x = np.cos(x)
    sin_x = np.sin(x)
    return (2.0 * cos_x**2 + 6.0 * sin_x**2) / (cos_x**4)

x = 1.0
exact = df_exact(x)
eps = np.finfo(float).eps

M1 = np.abs(d2f_exact(x))
h_min_th_1 = 2.0 * np.sqrt(eps / M1)

M2 = np.abs(d3f_exact(x))
h_min_th_2 = np.cbrt(3.0 * eps / M2)

k_vals = np.arange(0, 17)
h_vals = 10.0**(-k_vals)

err_1_vals = []
err_2_vals = []

err_method_1_vals = []
err_num_1_vals = []

min_err_1 = float('inf')
h_min_emp_1 = 0.0

min_err_2 = float('inf')
h_min_emp_2 = 0.0

print(f"{'k':<5} {'h':<20} {'Blad_wzor(1)':<25} {'Blad_wzor(3)':<25}")

for k, h in zip(k_vals, h_vals):
    df_fw = (f(x + h) - f(x)) / h
    err_1 = np.abs(df_fw - exact)
    err_1_vals.append(err_1)
    
    err_method_1 = M1 * h / 2.0
    err_num_1 = 2.0 * eps / h
    err_method_1_vals.append(err_method_1)
    err_num_1_vals.append(err_num_1)
    
    if err_1 < min_err_1:
        min_err_1 = err_1
        h_min_emp_1 = h
        
    df_cd = (f(x + h) - f(x - h)) / (2.0 * h)
    err_2 = np.abs(df_cd - exact)
    err_2_vals.append(err_2)
    
    if err_2 < min_err_2:
        min_err_2 = err_2
        h_min_emp_2 = h
        
    print(f"{k:<5} {h:<20.1e} {err_1:<25.16e} {err_2:<25.16e}")

print("\n--- WZOR (1) Roznica progresywna ---")
print(f"h_min (empiryczne):  {h_min_emp_1}")
print(f"h_min (teoretyczne): {h_min_th_1}")
print(f"Minimalny blad E(h_min): {min_err_1}")

print("\n--- WZOR (3) Roznica centralna ---")
print(f"h_min (empiryczne):  {h_min_emp_2}")
print(f"h_min (teoretyczne): {h_min_th_2}")
print(f"Minimalny blad E(h_min): {min_err_2}")

print("\n--- POROWNANIE ---")
if min_err_2 < min_err_1:
    print("Metoda roznic centralnych (wzor 3) jest dokladniejsza.")
else:
    print("Metoda roznic progresywnych (wzor 1) jest dokladniejsza.")

plt.figure(figsize=(10, 6))
plt.loglog(h_vals, err_1_vals, 'o-', label='Blad obliczeniowy E(h) - wzor (1)')
plt.loglog(h_vals, err_method_1_vals, '--', label='Blad metody (wzor 1)')
plt.loglog(h_vals, err_num_1_vals, ':', label='Blad numeryczny (wzor 1)')
plt.loglog(h_vals, err_2_vals, 's-', label='Blad obliczeniowy E(h) - wzor (3)')

plt.axvline(h_min_emp_1, color='blue', alpha=0.3, linestyle='--', label=f'h_min emp (1) = {h_min_emp_1:.1e} (Blad: {min_err_1:.2e})')
plt.axvline(h_min_emp_2, color='orange', alpha=0.5, linestyle='--', label=f'h_min emp (3) = {h_min_emp_2:.1e} (Blad: {min_err_2:.2e})')

plt.xlabel('Krok h')
plt.ylabel('Wartosc bezwzgledna bledu')
plt.title('Bledy przyblizenia pochodnej f(x) = tan(x) w punkcie x = 1')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.show()