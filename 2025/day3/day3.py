def part2():
    rows = open("input.txt", "r").readlines()
    
    joltages = []
    for row in rows:
        nums = list(row)
        num_list = []
        for i in range(12):
            char = max(nums[0:len(nums)-12+i])
            nums = nums[nums.index(char)+1:]
            num_list.append(char)

        joltages.append(int("".join(num_list)))
    
    print(sum(joltages))

def part1():

    return

if __name__ == "__main__":
    part1()
    part2()
