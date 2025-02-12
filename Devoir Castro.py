
#%%
                            #Exo 1
 #Exercice 1
def fib(n):
    a, b = 1, 1
    while b <= n:
        a, b = b, a + b
    return b
print("Fibonacci 75:", fib(75))
print("Fibonacci  50:", fib(50))
print("Fibonacci 100:", fib(100))


# %%
                 #Exo2
import numpy as np

BOS = [2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
MER = [6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]

# Calcul des précipitations totales et moyennes
total_BOS = sum(BOS)
mean_BOS = np.mean(BOS)
total_MER = sum(MER)
mean_MER = np.mean(MER)

# Mois où les précipitations sont supérieures à la moyenne
months_above_mean_BOS = [i + 1 for i, val in enumerate(BOS) if val > mean_BOS]
months_above_mean_MER = [i + 1 for i, val in enumerate(MER) if val > mean_MER]

# Mois où les précipitations de Boston sont inférieures à celles de Seattle
months_BOS_less_MER = [i + 1 for i, (b, m) in enumerate(zip(BOS, MER)) if b < m]

print(f"Total BOS: {total_BOS}, Moyenne BOS: {mean_BOS}")
print(f"Total MER: {total_MER}, Moyenne MER: {mean_MER}")
print(f"Mois > Moyenne BOS: {months_above_mean_BOS}")
print(f"Mois > Moyenne MER: {months_above_mean_MER}")
print(f"Mois BOS < MER: {months_BOS_less_MER}")

# %%

                            #Exo3

import numpy as np
from scipy.stats import norm

def correlation_test(X, Y, r0):
    n = len(X)
    r = np.corrcoef(X, Y)[0, 1]
    Z = 0.5 * np.log((1 + r) / (1 - r))
    Z0 = 0.5 * np.log((1 + r0) / (1 - r0))
    T = (Z - Z0) * np.sqrt(n - 3)
    p_value = 2 * (1 - norm.cdf(abs(T)))
    return r, p_value

# Exemple de données
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

# Tests
r, p0 = correlation_test(X, Y, 0)
print(f"Corrélation: {r}, p-valeur pour r0=0: {p0}")
r, p6 = correlation_test(X, Y, 0.6)
print(f"Corrélation: {r}, p-valeur pour r0=0.6: {p6}")

#%%
                             #Exo 4
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
r = 2
a = 0.05
beta = 1
generations = 30
host_pop = [20]
parasitoid_pop = [2]

# Modèle
for t in range(generations):
    H_next = host_pop[-1] * np.exp(-a * parasitoid_pop[-1]) * r
    P_next = host_pop[-1] * (1 - np.exp(-a * parasitoid_pop[-1])) * beta
    host_pop.append(H_next)
    parasitoid_pop.append(P_next)

# Graphique
time = range(generations + 1)
plt.plot(time, host_pop, label="Hôtes")
plt.plot(time, parasitoid_pop, label="Parasitoïdes")
plt.xlabel("Temps (générations)")
plt.ylabel("Population")
plt.legend()
plt.title("Modèle de Nicholson-Bailey")
plt.show()
# %%