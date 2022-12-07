from read_input import read_input

lines = read_input("input3.txt")

line_length_tuples = [(x, int(len(x) /2) , len(x)) for x in lines]

buckets = [(t[0][0:t[1]], t[0][t[1]:t[2]]) for t in line_length_tuples]

priority_sum = 0

for b in buckets:
    already_found = set()
    for c in b[0]:
        if c in b[1] and not c in already_found:
            already_found.add(c)
            if c >= 'A' and c <= 'Z':
                priority_sum += ord(c) - ord('A') + 27
            else:
                priority_sum += ord(c) - ord('a') + 1


print("Dupe priority sum is " + str(priority_sum))