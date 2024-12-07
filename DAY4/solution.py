import re

# poziomo:
input = []
with open("input.txt", 'r') as file:
    for line in file:
        input.append(line.strip())

xmas_list = [re.findall("XMAS", line) for line in input]
xmas_list.extend([re.findall("SAMX", line) for line in input])

# pionowo
columns = ["".join(column) for column in zip(*input)]

xmas_list.extend([re.findall("XMAS", column) for column in columns])
xmas_list.extend([re.findall("SAMX", column) for column in columns])

# na ukos
m = len(input)
n = len(columns)

diag_all = []

# od lewej do prawej
for offset in range(n):
    diag = ""
    for i in range(m):
        if(i+offset < n):
            diag_element = f"{input[i][i+offset]}"
            diag += diag_element
    diag_all.append(diag)
for offset in range(1,m):
    diag = ""
    for i in range(m):
        if(i+offset < m):
            diag_element = f"{input[i+offset][i]}"
            diag += diag_element
    diag_all.append(diag)

# od prawej do lewej
for offset in range(n):
    diag = ""
    for i in range(m):
        if(n-1-offset-i >= 0):
            diag_element = f"{input[i][n-1-offset-i]}"
            diag += diag_element
    diag_all.append(diag)
for offset in range(1,m):
    diag = ""
    for i in range(m):
        if(n-1-offset-i >= 0):
            diag_element = f"{input[i+offset][n-1-i]}"
            diag += diag_element
    diag_all.append(diag)

xmas_list.extend([re.findall("XMAS", diag) for diag in diag_all])
xmas_list.extend([re.findall("SAMX", diag) for diag in diag_all])

# sum all xmas and samx
sum = 0

for list in xmas_list:
    sum += len(list)

print(f"Answer: XMAS appears {sum} times.")
