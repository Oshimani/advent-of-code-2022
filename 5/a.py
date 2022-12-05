def get_stack(lines: list, index: int):
    stack = []
    for line in lines:
        stack.append(line[index * 4 + 1])
    stack = stack[::-1]
    stack = list(filter(lambda x: x != " ", stack))
    return stack


def get_instruction(line: str):
    segments = line.split(" ")
    return {
        "count": int(segments[1]),
        "from": int(segments[3]),
        "to": int(segments[5][:-1]),
    }


def process_instruction(instruction: dict):
    to = instruction["to"] - 1
    from_ = instruction["from"] - 1
    cargo = stacks[from_][-instruction["count"] :]
    stacks[to] += cargo
    stacks[from_] = stacks[from_][:-instruction["count"]]


def print_stacks(stacks: list):
    print("Stacks:")
    for index, stack in enumerate(stacks):
        print(f"{index+1}: {stack}")


lines = []
stacks = []
instructions = []
with open("./5/input.txt") as f:

    # get stacks
    while True:
        line = f.readline()
        # print(line)
        lines.append(line)
        if line == "\n":
            lines.pop()
            lines.pop()
            break
    stacks = [get_stack(lines, i) for i in range(0, 9)]
    # print(stacks)

    # get instructions
    while True:
        line = f.readline()
        # print(line)
        if line == "\n" or line == "":
            break
        instructions.append(get_instruction(line))

print_stacks(stacks)
for instruction in instructions:
    # print(instruction)
    process_instruction(instruction)
print_stacks(stacks)

output =""
for stack in stacks:
    output+=stack[-1]
print(output)