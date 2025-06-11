import math
print("PROGRAM TO CHECK WHETHER A NUMBER IS PRIME OR NOT")
value = int(input("ENTER A NUMBER TO FIND PRIME: "))
if value < 2:
    ans = "NO"
else:
    is_prime = True
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            is_prime = False
            break

    ans = "YES" if is_prime else "NO"
print(ans)

    
