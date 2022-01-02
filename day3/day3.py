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

        return(f"Gamma = {gamma}, Epsilon = {epsilon}. Result = {result}")

print(solution1())
