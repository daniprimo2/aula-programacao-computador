# Exemplo 53b - função enumerate
linguagens = ['Python', 'Java', 'C', 'C++', 'C#', 'JavaScript', 'Vb.net', 'Delphi', 'Cobol', 'Assembler', 'ZPL']
x = 0
print("\nMétodo tradicional")
for e in linguagens: # construção tradicional do loop com for
    print("[%2d] - %s" %(x, e))
    x += 1
print("\nMétodo com enumerate")
for x,e in enumerate(linguagens): # construção com enumerate
    print("[%2d] - %s" %(x, e))
    x += 1
