
print("=== PROGRAM MENENTUKAN BILANGAN PRIMA ===")

n = int(input("Masukkan sebuah bilangan: "))

if n <= 1:
    print(n, "bukan bilangan prima")
else:
    prima = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prima = False
            break

    if prima:
        print(n, "adalah bilangan prima")
    else:
        print(n, "bukan bilangan prima")