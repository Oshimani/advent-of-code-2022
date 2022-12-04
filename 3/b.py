def divide_into_groups_of(elfs: list, group_size: int):
    return [elfs[i : i + group_size] for i in range(0, len(elfs), group_size)]


def get_groups_item(elfs: list):
    for item in elfs[0]:
        if item in elfs[1] and item in elfs[2]:
            return item


def get_item_priority(item: str):
    ascii = ord(item)
    if ascii >= 65 and ascii <= 90:
        return ascii - 64 + 26
    if ascii >= 97 and ascii <= 122:
        return ascii - 96


lines = []
with open("./3/input.txt", "r") as f:
    lines = f.readlines()

# remove \n from end of each line
elfs = [line[:-1] for line in lines]

groups = divide_into_groups_of(elfs, 3)
sum = 0
for group in groups:
    item = get_groups_item(group)
    sum += get_item_priority(item)

print(f"Total priority: {sum}")