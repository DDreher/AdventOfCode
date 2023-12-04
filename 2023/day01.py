"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""


def get_input():
    import os
    with open(f"{os.path.basename(__file__)[:-3]}.txt") as f:
        return f.read().splitlines()


def solve_part1(in_data):
    # given test data
    # in_data = [
    #     "1abc2",
    #     "pqr3stu8vwx",
    #     "a1b2c3d4e5f",
    #     "treb7uchet",
    # ]

    summed_digits = 0
    for string in in_data:
        digits = [c for c in string if c.isdigit()]
        summed_digits = summed_digits + int(f"{digits[0]}{digits[-1]}")
    return summed_digits


def solve_part2(in_data):
    # given test data
    # in_data = [
    #     "two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen",
    # ]

    summed_digits = 0
    digits_as_string = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]

    for string in in_data:
        left_digit = ""
        right_digit = ""
        first_index = len(string)
        last_index = 0

        for i, c in enumerate(string):
            if c.isdigit():
                left_digit = c
                first_index = i
                break

        for i, c in enumerate(reversed(string)):
            if c.isdigit():
                right_digit = c
                last_index = len(string) - 1 - i
                break

        for i, s in enumerate(digits_as_string):
            index = string.find(s)
            if index != -1 and index < first_index:
                first_index = index
                left_digit = str(i+1)

        for i, s in enumerate(digits_as_string):
            index = string.rfind(s)
            if index != -1 and index > last_index:
                last_index = index
                right_digit = str(i+1)

        summed_digits += int(f"{left_digit}{right_digit}")

    return summed_digits


if __name__ == "__main__":
    data = get_input()

    result = solve_part1(data)
    print(f"Results part 1: {result}")

    result = solve_part2(data)
    print(f"Results part 2: {result}")
