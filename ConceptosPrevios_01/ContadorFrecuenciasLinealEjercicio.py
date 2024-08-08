max_pepitas = int(input())
max_cubitos = int(input())

num_pepitas = 1
num_cubitos = 1

num_figuras = 0
while (num_pepitas <= max_pepitas):
    num_figuras += 1
    num_pepitas += 1

while(num_cubitos <= max_cubitos):
    num_figuras += 1
    num_cubitos += 1

print(f"En total conté {num_figuras} figuras")