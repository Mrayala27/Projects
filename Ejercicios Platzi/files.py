file = open('./text.txt')
for line in file:
    print(line)
file.close()

with open('./text.txt') as file:
    for line in file:
        print(line)