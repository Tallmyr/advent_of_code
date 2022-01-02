from assignments import day1, day2, day3
from prettytable import PrettyTable

table = PrettyTable(["Task", "Result 1", "Result 2", "Result 3", "Final Result"])

# Day 1
table.add_row(["Day 1 Solution 1", "0", "0", "0", day1.solution1()])
table.add_row(["Day 1 Solution 2", "0", "0", "0", day1.solution2()])

# Day 2 S1
one, two, three = day2.solution1()
table.add_row(["Day 2 Solution 1", one, two, "0", three])

# Day 2 S2
one, two, three = day2.solution2()
table.add_row(["Day 2 Solution 2", one, two, "0", three])

# Day 3 S1
one, two, three = day3.solution1()
table.add_row(["Day 3 Solution 1", one, two, "0", three])

# Day 3 S2
one, two, three = day3.solution2()
table.add_row(["Day 3 Solution 2", one, two, "0", three])


print(table)
