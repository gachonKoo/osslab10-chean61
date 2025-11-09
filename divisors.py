import sys
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
