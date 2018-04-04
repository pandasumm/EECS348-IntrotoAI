input = []
while True:
    line = raw_input()
    if not line:
        break
    line = line.split()
    input.append([int(num) for num in line])
n = len(input)
for col in range(n):
    for row in reversed(range(n)):
        print input[row][col],
    print "\n"
