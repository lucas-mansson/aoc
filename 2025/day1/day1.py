def part1():
    with open("input.txt", "r") as f:
        rotations = [i.strip() for i in f.readlines()]

    dial = 50
    res = 0
    for r in rotations:
        direction = r[0]
        nbr = int(r[1:])

        if direction == "L":
            dial = (dial - nbr) % 100
        else:
            dial = (dial + nbr) % 100

        if dial == 0:
            res += 1

    print(res)


def part2():
    with open("input.txt", "r") as f:
        rotations = [i.strip() for i in f.readlines()]

    dial = 50
    res = 0
    for r in rotations:
        print("dial:", dial)
        print(r)
        direction = r[0]
        nbr = int(r[1:])

        if direction == "L":
            for _ in range(nbr):
                dial = (dial - 1) % 100
                if dial == 0:
                    res += 1
        else:
            for _ in range(nbr):
                dial = (dial + 1) % 100
                if dial == 0:
                    res += 1

    print(res)

if __name__ == "__main__":
    #part1()
    part2()
