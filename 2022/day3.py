from read_input import read_input

lines = read_input("input3.txt")

indices = [index * 3 for index in range(0, int(len(lines) / 3))]

groups = [lines[x:x+3] for x in indices]

def find_common(group: list[str]) -> str:
    return set(group[0]).intersection(group[1], group[2]).pop()

def priority(c: str):
    if c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1


group_badges = [find_common(g) for g in groups]

priority_sum = sum([priority(b) for b in group_badges])

print("Priority sum is " + str(priority_sum))