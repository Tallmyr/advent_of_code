def solution1(input="inputs", bits=12):
    with open(input + "/day3.txt", "r") as file:
        list1 = file.read().splitlines()

        binary_string = ""
        for i in range(bits):
            zero, one = 0, 0
            for x in list1:
                if x[i] == "1":
                    one += 1
                else:
                    zero += 1

            binary_string += "1" if one > zero else "0"

        mask = 31 if bits == 5 else 4095

        gamma = int(binary_string, base=2)

        epsilon = int(gamma ^ mask)
        result = gamma * epsilon

        return (gamma, epsilon, result)


def solution2(input="inputs"):
    with open(input + "/day3.txt", "r") as file:
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

        r_oxygen = int(oxygen[0], base=2)
        r_co2 = int(co2[0], base=2)
        result = r_oxygen * r_co2
    return (r_oxygen, r_co2, result)
