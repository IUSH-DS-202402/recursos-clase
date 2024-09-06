########################
# Programa original
########################

for i in range(0,5):
    print(f"Iteración #{i}")


########################
# Paso #1
########################
i = 0
if i < 5:
    print(f"Iteración #{i}")
    i = i + 1


########################
# Paso #2
########################

def recorre(i):
    if i < 5:
        print(f"Iteración #{i}")
        recorre(i + 1)


#######

i = 0
if i < 5:
    print(f"Iteración #{i}")
    i = i + 1

########################
# Paso #3
########################

def recorre(i):
    if i < 5:
        print(f"Iteración #{i}")
        recorre(i + 1)

#######

i = 0
recorre(i)