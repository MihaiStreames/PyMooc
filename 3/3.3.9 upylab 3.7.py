pari = int(input())
tirage = int(input())

print(10 * (((tirage != 0) & ((tirage <= 10) ^ tirage ^ pari), (tirage ^ pari) & 1)[pari <= 14] << 1, (tirage == pari) * 12)[pari <= 12])