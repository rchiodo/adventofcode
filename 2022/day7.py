from collections import deque

from pkg_resources import ResolutionError
from read_input import read_input
import re

lines = read_input("input7.txt")
lines.reverse() # bottom up so it's like a stack
commands = deque(lines)

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self._size = size
    def __repr__(self) -> str:
        return f"{self.name} (file, size={self.size()})"
    def size(self) -> int:
        return self._size

class Directory:
    def __init__(self, name: str, children: "list[Directory | File]" = [], parent: "Directory | None" = None):
        self.name = name
        self.children = children
        self.parent = parent

    def __repr__(self) -> str:
        return f"{self.name} (dir, size={self.size()})"
    
    def size(self) -> int:
        return sum([c.size() for c in self.children])

def read_command_output(commands: deque[str]) -> list[str]:
    result: list[str] = []
    while not commands[0].startswith("$"):
        result.append(commands.pop())
    return result

def handle_cd(args: str, currentDirectory: Directory) -> Directory:
    change = args.strip()
    result: Directory = currentDirectory
    match change:
        case '/':
            while result.parent != None:
                result = result.parent
        
        case '..':
            result = result.parent if result.parent != None else result

        case _:
            result = next(filter(lambda c : c.name == change and isinstance(c, Directory), result.children)) # type: ignore
    
    return result

command_pattern = r"\$\s+(\w+)\s*(.*)"
dir_pattern = r"((?P<dir>dir)|(?P<size>\d+))\s+(?P<name>\w+)"

directories: list[Directory] = []

currentDirectory = Directory('/')
rootDirectory = currentDirectory

while len(commands) > 0:
    command = commands.pop()
    command_match = re.match(command_pattern, command)
    dir_match = re.match(dir_pattern, command)
    if command_match != None:
        match command_match[1]:
            case 'cd':
                currentDirectory = handle_cd(command_match[2], currentDirectory)
    elif dir_match != None:
        dir_group = dir_match.group("dir")
        size_group = dir_match.group("size")
        name_group = dir_match.group("name")
        if dir_group != None:
            currentDirectory.children.append(Directory(name_group, [], currentDirectory))
        elif size_group != None:
            currentDirectory.children.append(File(name_group, int(size_group)))

def dirs_less_than_100k(children: list[Directory | File]):
    for c in children:
        if isinstance(c, Directory):
            if c.size() < 100000:
                yield c
            yield from dirs_less_than_100k(c.children)

dirs_100k = list(dirs_less_than_100k(rootDirectory.children))

total_size = rootDirectory.size()

free_space = 70000000 - total_size

minimum_dir_size = 30000000 - free_space

def dir_greater_than_minimum(children: list[Directory | File], bestCandidate: Directory) -> Directory:
    for c in children:
        if isinstance(c, Directory):
            if bestCandidate.size() > c.size() and c.size() >= minimum_dir_size:
                bestCandidate = c
            bestCandidate = dir_greater_than_minimum(c.children, bestCandidate)
    return bestCandidate 

best = dir_greater_than_minimum(rootDirectory.children, rootDirectory)

print(best.size())


