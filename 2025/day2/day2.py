def part1():
    with open("input.txt", "r") as f:
        ranges = f.read().split(",")
    
    invalid_ids = []
    for r in ranges:
        r = r.split("-") 
        for i in range(int(r[0]), int(r[1])):
            id = str(i)
            half = len(id) // 2
            if id[0:half] == id[half:]:
                invalid_ids.append(id)

    res = 0
    for id in invalid_ids:
        res += int(id)
    
    print(res)


def is_invalid(id: str):
    for i in range(1, len(id)):
        if is_repeating(id, i):
            return True
    return False

def is_repeating(input: str, size: int) -> bool:
    chunks = [input[i:i+size] for i in range(0, len(input), size)] 
    for i in range(1, len(chunks)):
        if chunks[0] != chunks[i]:
            return False
    return True 

def part2():
    with open("input.txt", "r") as f:
        ranges = f.read().split(",")
   
    invalid_ids = []
    for r in ranges:
        r = r.split("-") 
        for i in range(int(r[0]), int(r[1])):
            if is_invalid(str(i)):
                invalid_ids.append(i)

    res = 0
    for id in invalid_ids:
        res += int(id)

    print(res)
    return

if __name__ == "__main__":
    part2()
