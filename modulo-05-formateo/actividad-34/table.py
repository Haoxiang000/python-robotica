ultrasonidos = 40
infrarrojos = 12
Luz = 7

ultrasonidos_barra = "#" * (ultrasonidos // 5)

infrarrojos_barra = "#" * (infrarrojos // 5)

Luz_barra = "#" * (Luz // 5)

print(f"ultrasonidos {ultrasonidos:.1f}cm", ultrasonidos_barra)

print(f"infrarrojos {infrarrojos:.1f}cm", infrarrojos_barra)

print(f"Luz {Luz:.1f}cm", Luz_barra)