def divide_into_groups_of(elfs: list, group_size: int):
    return [elfs[i : i + group_size] for i in range(0, len(elfs), group_size)]


def parse_assignment(input: str):
    assignments = input.split("-")
    assignments = [int(assignment) for assignment in assignments]
    return assignments


def print_assignment(assignment: list):
    output = "["
    for n in range(0, 100):
        between = range(assignment[0], assignment[1] + 1)
        output += "X" if n in between else "."
    output += "]"
    print(output)


def print_assignment_group(assignment_group: list):
    print_assignment(assignment_group[0])
    print_assignment(assignment_group[1])


def get_assignments(group: str):
    assignments = group.split(",")

    assignments_1 = parse_assignment(assignments[0])
    assignments_2 = parse_assignment(assignments[1])
    return assignments_1, assignments_2


def check_overlaps(assignments: list):
    assignment_1 = assignments[0]
    assignment_2 = assignments[1]

    if assignment_1[0] >= assignment_2[0]:
        assignment_1, assignment_2 = assignment_2, assignment_1

    if assignment_1[1] >= assignment_2[0]:
        return True
    return False


lines = []
with open("./4/input.txt") as f:
    lines = f.readlines()

groups = [line[:-1] for line in lines]
sum_of_overlaps = 0
for group in groups:
    assignment_group = get_assignments(group)
    print_assignment_group(assignment_group)
    fully_contained = check_overlaps(assignment_group)
    print(f"Overlaps: {fully_contained}")
    print("")
    if fully_contained:
        sum_of_overlaps += 1
print(f"Sum of overlaps: {sum_of_overlaps}")
