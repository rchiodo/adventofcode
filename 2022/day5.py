from typing import NoReturn
from read_input import read_input
import re

lines = read_input("input5.txt")

def splitLines(lines: list[str]) -> list[list[str]]:
    result = [[]]
    resultIndex = 0
    for l in lines:
        if l.lstrip().startswith('1'):
            result.append([l])
            result.append([])
            resultIndex = 2
        else:
            result[resultIndex].append(l)
    
    return result
    

def createStacks(stackLines: list[str], stackCount: int) -> list[list[str]]:
    result = [list() for i in range(0, stackCount)]
    for line in reversed(stackLines):
        for j in range(0, stackCount):
            pos = (j * 4) + 1
            char = line[pos]
            if char != ' ':
                result[j].append(line[pos])
    
    return result

split = splitLines(lines)
stackCount = int(split[1][0].rstrip().split(' ')[-1])

def applyMove(moveLine: str, stacks: list[list[str]]) -> None:
    pattern = r"move (\d+) from (\d+) to (\d+)"
    match = re.match(pattern, moveLine)
    if match is not None:
        quantity = int(match[1])
        fromIndex = int(match[2]) - 1
        toIndex = int(match[3]) - 1
        fromStack = stacks[fromIndex]
        toStack = stacks[toIndex]
        fromStackQuantity = min(len(fromStack), quantity)
        toStack.extend(fromStack[-fromStackQuantity:])
        stacks[fromIndex] = fromStack[:-fromStackQuantity]



stacks = createStacks(split[0], stackCount)
moves = split[2]

for m in moves:
    applyMove(m, stacks)

top = [s[-1] for s in stacks]

print(f"Top of all stacks: {''.join(top)}")
