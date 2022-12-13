from read_input import read_input

lines = read_input("input4.txt")

pairs = [x.split(',') for x in lines]

def parseRange(elf: str)-> set:
    split = elf.split('-')
    start = int(split[0])
    end = int(split[1])
    return set(range(start,end+1))

ranges = [[parseRange(p[0]), parseRange(p[1])] for p in pairs]

total_contains = 0

for r in ranges:
    if len(r[0].intersection(r[1])) > 0:
        total_contains += 1


print(f"Total intersects: {total_contains}")