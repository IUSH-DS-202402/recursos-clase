subscriptores = int(input())                                  # 1
valorSubscripcion = int(input())                              # 1
tajadaDelGobierno = int(input())                              # 1

totalBruto = subscriptores*valorSubscripcion                  # 1
totalConComision = totalBruto * (1-tajadaDelGobierno/100)     # 1

print(f"Este mes hice {totalConComision} en Twitch")          # 1