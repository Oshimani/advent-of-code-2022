# A
# read file
elfs = []
with open("./1/input.txt", "r") as f:
    lines = f.readlines()

    elf = []
    for line in lines:
        print(line)
        if line == "\n":
            # elf is done
            elfs.append(elf)
            elf = []
        else:
            # put item in elf's bag
            line = line[:-1]
            elf.append(int(line))
    print(elfs)


def get_max():
    # [index, value]
    max = [-1, -1]
    elf: list
    for index, elf in enumerate(elfs):
        elf_sum = sum(elf)
        if elf_sum > max[1]:
            max[1] = elf_sum
            max[0] = index
    print(f"Elf {max[0]} has the most items with {max[1]} calories")
    return max


max1 = get_max()

# B
elfs.pop(max1[0])
max2 = get_max()

elfs.pop(max2[0])
max3 = get_max()

print(max1[1] + max2[1] + max3[1])