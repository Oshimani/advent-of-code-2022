def test_unique(input: list):
    i = 0
    j = 1
    while i < len(input):
        while j < len(input):
            if input[i] == input[j]:
                return False
            j += 1
        i += 1
        j = i + 1
    return True


line: str
with open("./6/input.txt") as f:
    line = f.read()
    line = line[:-1]
input = [char for char in line]

for index, char in enumerate(input):
    if index + 4 > len(input):
        print("Not found")
        break
    sub = input[index : index + 14]

    result = test_unique(sub)
    if result == True:
        print(f"Found at index {index+14}")
        break
