from read_input import read_input

lines = read_input("input.txt")
    

class Elf:
    def __init__(self: "Elf", lines: list[int]):
        self.calories = sum(lines)
        
    def __repr__(self: "Elf") -> str:
        return f"Elf : {self.calories}"
    
elves: list[Elf] = []
current = []

for l in lines:
    if len(l) > 1:
        current.append(int(l))
    elif len(current) > 0:
        elves.append(Elf(current))
        current = []

inorder = sorted(elves, key=lambda e: e.calories, reverse=True)

print("Highest calories:")
print(inorder[0].calories)
print("Combined calories of top 3")
print(inorder[0].calories + inorder[1].calories + inorder[2].calories)
