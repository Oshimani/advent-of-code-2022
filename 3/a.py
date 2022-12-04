def get_rucksack_contents(rucksack: str):
    # split compartments
    left_compartment = rucksack[: len(rucksack) // 2]
    right_compartment = rucksack[len(rucksack) // 2 :]

    return left_compartment, right_compartment


def get_item_in_both_compartments(left_compartment: str, right_compartment: str):
    for item in left_compartment:
        if item in right_compartment:
            return item
    return ""


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
rucksacks = [line[:-1] for line in lines]
sum = 0
for rucksack in rucksacks:
    left_compartment, right_compartment = get_rucksack_contents(rucksack)
    item = get_item_in_both_compartments(left_compartment, right_compartment)
    print(f"Item in both compartments: %s", item)
    item_priority = get_item_priority(item)
    sum += item_priority

print(f"Total priority: {sum}")
