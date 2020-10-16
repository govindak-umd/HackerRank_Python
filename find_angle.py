import math

x = int(input())
y = int(input())
angle = round((math.degrees(math.atan(x / y))))
out = str(angle) + chr(176)
print(out)
