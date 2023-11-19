# Rosalind INI4: Conditions and Loops
## Given: Two positive integers a and b (a<b<10000).
## Return: The sum of all odd integers from through b, inclusively.

a = 4468
b = 9027

result = 0
for n in range(a,b+1):
    if n % 2 == 1:
        result = result + n
    else:
        continue

print(result)

## My result: 15385440 (correct!)

