import matplotlib.pyplot as plt

# Datos
cities = ["Berlin", "Boston", "Chicago", "London", "NYC", "Paris", "Valencia"]
years = ["2018", "2019", "2021", "2022", "2023", "2024"]
data = [
    [30.2, 30.1, 27.6, 33.1, 33.5, 34.3],
    [45.0, 44.9, 48.4, 42.6, 42.9, 42.9],
    [46.3, 46.4, 45.5, 46.9, 46.6, 46.0],
    [40.9, 41.8, 40.2, 41.6, 41.5, 42.4],
    [42.0, 42.4, 45.5, 44.4, 44.4, 44.5],
    [24.1, 26.0, 21.3, 24.5, 25.7, 27.3],
    [17.1, 18.7, 15.9, 19.2, 20.6, 21.7]
]

# Gráfica
plt.figure(figsize=(10, 6))
for i, city in enumerate(cities):
    plt.plot(years, data[i], marker='o', label=city)

# Estilo
plt.title("Evolución del % de Participación Femenina (2018-2024)")
plt.xlabel("Año")
plt.ylabel("% de Participación Femenina")
plt.legend()
plt.grid(True)
plt.show()