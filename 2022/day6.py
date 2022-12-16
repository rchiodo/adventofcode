from read_input import read_input

line = read_input("input6.txt")[0]

def find_unique(length: int): 
    for i in range(length, len(line)-1):
        unique = set(line[i-length:i])
        if len(unique) == length:
            return i

print(f"First start of packet marker: {find_unique(4)}")
print(f"First start of message marker: {find_unique(14)}")

