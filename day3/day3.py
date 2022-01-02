def solution1():
    with open("day3/input.txt", "r") as file:
        list1 = file.read().splitlines()

        binary_string = ""
        for i in range(12):
            zero, one = 0, 0
            for x in list1:
                if x[i] == "1":
                    one += 1
                else:
                    zero += 1

            binary_string += "1" if one > zero else "0"

        gamma = int(binary_string, base=2)
        epsilon = gamma ^ 0b111111111111
        result = gamma * epsilon

        return f"Gamma = {gamma}, Epsilon = {epsilon}. Result = {result}"


def solution2(input: str, bits: int):
    with open("day3/" + input, "r") as file:
        oxygen = file.read().splitlines()
        co2 = oxygen

        i = 0
        while len(oxygen) > 1:
            zero, one = 0, 0
            for x in oxygen:
                if x[i] == "1":
                    one += 1
                else:
                    zero += 1
            keep = "0" if zero > one else "1"

            oxygen = [x for x in oxygen if x[i] == keep]

            i += 1

        i = 0
        while len(co2) > 1:
            zero, one = 0, 0
            for x in co2:
                if x[i] == "1":
                    one += 1
                else:
                    zero += 1
            keep = "1" if one < zero else "0"

            co2 = [x for x in co2 if x[i] == keep]

            i += 1

        result = int(oxygen[0], base=2) * int(co2[0], base=2)
    return (oxygen[0], co2[0], result)


print(solution2("input.txt", 12))
