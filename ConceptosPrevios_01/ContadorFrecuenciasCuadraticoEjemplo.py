n = int(input())                            # 1

for i in range (1,n+1):                     # n+1
    print(f"\nTabla del {i} hasta {n}:")    # n
    for j in range(1,n+1):                  # n(n + 1)
        print(f"{i} * {j} = {i*j}")         # n*n