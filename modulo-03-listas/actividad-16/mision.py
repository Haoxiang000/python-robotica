sensores = ["ultrasonidos", "infrarrojos", "luz"]
distancias = [40, 12, 80]



sensores.append("presencia")
distancias.append(5)



sensores.remove("luz")
distancias.remove(80)

print(len(sensores))
print(len(distancias))

ordenadas = sorted(distancias)

print(ordenadas[0])
print(ordenadas[-1])

print(sensores[0:2])

