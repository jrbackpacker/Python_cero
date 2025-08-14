### Loops ###

# For Loop
for i in range(5):
    print(i)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Anidados
for i in range(3):
    for j in range(2):
        print(i, j)
        for k in range(2):
            print(i, j, k)
            print("Fin del bucle anidado")

# break
for i in range(5):
    if i == 3:
        break
    print(i)

# continue
for i in range(5):
    if i == 3:
        continue
    print(i)

    