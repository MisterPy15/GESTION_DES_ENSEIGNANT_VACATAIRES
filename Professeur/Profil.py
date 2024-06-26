import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Données d'entraînement
X_train = np.array([6, 8, 10, 14, 18])
y_train = np.array([7, 9, 13, 17.5, 18])

# Calcul de la variance de X
variance_x = np.var(X_train, ddof=1)

# Calcul de la covariance entre X et y
covariance_xy = np.cov(X_train, y_train)[0][1]

# Calcul du paramètre α
alpha = covariance_xy / variance_x

# Calcul de la moyenne de X et y
mean_x = np.mean(X_train)
mean_y = np.mean(y_train)

# Calcul du paramètre β
beta = mean_y - alpha * mean_x

# Affichage des paramètres
print(f'α : {alpha}')
print(f'β : {beta}')

# Prédiction des prix pour l'ensemble de test
X_test = np.array([8, 9, 11, 16, 12])
y_test = np.array([11, 8.5, 15, 18, 11])
y_pred = alpha * X_test + beta

# Calcul de la somme résiduelle des carrés (RSS)
rss = np.sum((y_test - y_pred) ** 2)
rss = round(rss, 2)
print(f'Somme résiduelle des carrés (RSS) : {rss}')

# Calcul de la somme totale des carrés (SSTot)
sstot = np.sum((y_test - np.mean(y_test)) ** 2)

# Calcul du coefficient de détermination (R-squared)
r_squared = 1 - (rss / sstot)
r_squared = round(r_squared, 2)
print(f'Coefficient de détermination (R-squared) : {r_squared}')

# Affichage des résultats
plt.scatter(X_test, y_test, color='blue', label='Données réelles')
plt.plot(X_test, y_pred, color='red', label='Prédictions du modèle')
plt.xlabel('Tailles en cm')
plt.ylabel('Prix en euros')
plt.title('Régression linéaire: Prix des pizzas en fonction de leur taille')
plt.legend()
plt.show()
