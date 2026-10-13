n = int(input("Enter outer row: "))

for i in range(-(n - 1), n):
    for j in range(-(n - 1), n):
        print(max(abs(i), abs(j)) + 1, end=" ")
    print()