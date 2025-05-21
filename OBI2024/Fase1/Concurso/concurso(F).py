# OBI2024 - Fase 1
# Concurso

[n, k] = [int(x) for x in input().split()]
vals = [int(x) for x in input().split()]
vals.sort()
print(vals[n - k])