with open("test.txt") as input:
    asteroidMap = [line.split(",") for line in input.read().splitlines()]

print(asteroidMap)


""" with open("test.txt") as f:
    content = f.read()
    c = list(content)
asteroidMap = []
for i in range(len(c)):
    asteroidMap.append(c[i].rstrip('\n').split(','))
print(asteroidMap[0][0]) """