def solution1():
    with open("day2/input.txt", "r") as file:
        list1 = file.read().splitlines()

        dist, depth = 0, 0

        for x in list1:
            instruct, value = x.split(" ")
            if instruct == "forward":
                dist += int(value)
            elif instruct == "down":
                depth += int(value)
            elif instruct == "up":
                depth -= int(value)
            else:
                raise ValueError(f"Incorrect instruction. Instruction found was: {instruct}")

        return f"Distance: {dist}, Depth: {depth}. Result: {dist * depth}"


def solution2():
    with open("day2/input.txt", "r") as file:
        list1 = file.read().splitlines()

        dist, depth, aim = 0, 0, 0

        for x in list1:
            instruct, value = x.split(" ")
            if instruct == "forward":
                dist += int(value)
                depth += (aim * int(value))
            elif instruct == "down":
                aim += int(value)
            elif instruct == "up":
                aim -= int(value)
            else:
                raise ValueError(f"Incorrect instruction. Instruction found was: {instruct}")

        return f"Distance: {dist}, Depth: {depth}. Result: {dist * depth}"


print(solution2())
