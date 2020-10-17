from itertools import groupby
print(*[(len(list(val)), int(key)) for key, val in groupby(input())])