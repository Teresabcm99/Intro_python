coches = {
    "Toyota": {
        "Modelo": "Corolla",
        "Cilindrada": "1.8L",
        "Combustible": "Gasolina"
    },
    "Ford": {
        "Modelo": "Mustang",
        "Cilindrada": "5.0L",
        "Combustible": "Gasolina"
    },
    "Honda": {
        "Modelo": "Civic",
        "Cilindrada": ["1.5L", "1.6L"],
        "Combustible": "Gasolina"
    },
    "Tesla": {
        "Modelo": "Model 3",
        "Cilindrada": "Eléctrico",
        "Combustible": "Eléctrico"
    }
}

# Utilizar el método .values() para obtener todos los valores e imprimirlos
for valores in coches.values():
    for valor in valores.values():
        print(valor)
