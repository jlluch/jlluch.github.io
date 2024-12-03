import matplotlib.pyplot as plt

# Datos
cities = ["Berlin", "Boston", "Chicago", "London", "NYC", "Paris", "Valencia"]
years = [2018, 2019, 2021, 2022, 2023, 2024]
data = [
    [40805, 43975, 23102, 34784, 42985, 54095],
    [25832, 26656, 15386, 24835, 26603, 25545],
    [44550, 45866, 26075, 39249, 48246, 51860],
    [40127, 42618, 35928, 40651, 48740, 53878],
    [52704, 53520, 24950, 47683, 51265, 55530],
    [42094, 48031, 27110, 34365, 50780, 53899],
    [19047, 21366, 12667, 21813, 25900, 28183]
]

# Crear la gráfica
plt.figure(figsize=(10, 6))
for i, city in enumerate(cities):
    plt.plot(years, data[i], label=city)

plt.title("Evolución del Número de Finishers en Maratones (2018-2024)", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Número de Finishers", fontsize=12)
plt.legend(title="Ciudad", fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("grafica_finishers18-24.svg")
plt.show()

