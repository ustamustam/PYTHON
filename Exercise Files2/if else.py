n = 5
if n % 2 == 1:
    print("Weird")
else:
    if n in range(2, 5):
        print("Not Weird")
    if n in range(6, 20):
        print("Weird")
    if n >= 20:
        print("Not Weird")
