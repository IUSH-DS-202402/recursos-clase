max_pepitas = int(input())                                      # 1

total_pepitas = 0                                               # 1
num_pepitas = 1                                                 # 1
 
while num_pepitas <= max_pepitas:                               # max_pepitas + 1
    print(f"Me he comido {num_pepitas} pepitas de frijol.")     # max_pepitas
    total_pepitas = total_pepitas + num_pepitas                 # max_pepitas
    num_pepitas += 1                                            # max_pepitas

print(f"En total me comí {total_pepitas} pepitas de frijol.")   # 1