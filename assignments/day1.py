def solution1(input):
    with open(input + "/day1.txt", "r") as file:
        list1 = file.read().splitlines()

        increases = 0

        for i, x in enumerate(list1[1:]):
            if int(x) > int(list1[i]):
                increases += 1

        return increases


def solution2(input):
    with open(input + "/day1.txt", "r") as file:
        list1 = file.read().splitlines()

        increases = 0

        for i, x in enumerate(list1):
            try:
                blocka = int(x) + int(list1[i + 1]) + int(list1[i + 2])
                blockb = int(list1[i + 1]) + int(list1[i + 2]) + int(list1[i + 3])

                if blocka < blockb:
                    increases += 1
            except IndexError:
                print("Out of lines!")

        return increases
