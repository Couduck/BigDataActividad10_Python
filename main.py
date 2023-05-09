import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Las variables a utilizar fueron las siguientes:\n")
print("Publisher: Nombre del publicante del juego\n")
print("NA_Sales: Ventas de un videojuego dentro del mercado estadounidense (Numérica)\n")
print("EU_Sales: Ventas de un videojuego dentro del mercado europeo (Numérica)\n")
print("JP_Sales: Ventas de un videojuego dentro del mercado japonés (Numérica)\n")
print("Other_Sales: Ventas de un videojuego en los demás mercados (Numérica)\n")
print("Global_Sales: Ventas de un videojuego en los demás mercados (Numérica)\n")

datos = pd.read_csv('vgsales.csv', header = 0)
datosFiltrados=datos[(datos["Rank"]) <= 100]
datosFiltrados=datosFiltrados[["Publisher", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]]

sns.pairplot(datosFiltrados, hue="Publisher")
plt.show()