medidas = [40, 12, 80, 25]

print(len(medidas))
print(medidas[0])
print(medidas[-1])

medidas.append(5)

print(medidas)

medidas.insert(1, 30)

print(medidas)

medidas[0] = 15

print(medidas)

medidas.remove(80)

print(medidas)

ordenadas = sorted(medidas)

print(medidas, ordenadas)
print(ordenadas[0])
print(ordenadas[-1])

print(medidas[1:4])