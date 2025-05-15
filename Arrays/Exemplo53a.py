# Exemplo 53a - função enumerate
l = [4, 7, 13, 17]
x = 0
print("\nMétodo tradicional")
for e in l: # construção tradicional do loop com for
    print("[%d] - %d" %(x, e))
    x += 1
print("\nMétodo com enumerate")
for x,e in enumerate(l): # construção com enumerate
    print("[%d] - %d" %(x, e))
    x += 1
