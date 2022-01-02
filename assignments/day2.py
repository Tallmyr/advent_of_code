def solution1(input="inputs"):
    with open(input + "/day2.txt", "r") as file:
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
                raise ValueError(
                    f"Incorrect instruction. Instruction found was: {instruct}"
                )
        result = dist * depth
        return (dist, depth, result)


def solution2(input="inputs"):
    with open(input + "/day2.txt", "r") as file:
        list1 = file.read().splitlines()

        dist, depth, aim = 0, 0, 0

        for x in list1:
            instruct, value = x.split(" ")
            if instruct == "forward":
                dist += int(value)
                depth += aim * int(value)
            elif instruct == "down":
                aim += int(value)
            elif instruct == "up":
                aim -= int(value)
            else:
                raise ValueError(
                    f"Incorrect instruction. Instruction found was: {instruct}"
                )
        result = dist * depth
        return (dist, depth, result)
