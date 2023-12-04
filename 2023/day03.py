"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""


def get_input():
    import os
    with open(f"{os.path.basename(__file__)[:-3]}.txt") as f:
        return f.read().splitlines()


def solve_part1(in_data):
    # data is a grid with origin at top left
    grid_w = len(in_data[0])
    grid_h = len(in_data)
    schematic_sum = 0

    def is_in_bounds(x, y):
        return 0 <= x < grid_w and 0 <= y < grid_h

    def is_symbol(c):
        return not str(c).isdigit() and c != '.'

    for y, row_data in enumerate(in_data):
        for x, c in enumerate(row_data):
            if is_symbol(c):
                # If it's a symbol, we check the surrounding grid cells for digits
                visited = set()  # Store visited grid cells so we don't re-consider them

                def get_digit(pn_x, pn_y):
                    digit = 0
                    if (pn_x, pn_y) in visited:
                        return 0

                    if is_in_bounds(pn_x, pn_y):
                        pn_c = in_data[pn_y][pn_x]
                        if pn_c.isdigit():
                            # Found a digit! Grow selection to get the entire digit
                            selection_l = pn_x
                            digit_str = ""

                            # First grow left
                            while True:
                                if not is_in_bounds(selection_l, pn_y):
                                    break
                                digit_c = in_data[pn_y][selection_l]
                                if not digit_c.isdigit():
                                    break
                                selection_l -= 1

                            # Then from the first character of the digit grow right to assemble the digit
                            while True:
                                if not is_in_bounds(selection_l + 1, pn_y):
                                    break
                                selection_l += 1
                                digit_c = in_data[pn_y][selection_l]
                                if not digit_c.isdigit():
                                    break
                                digit_str += in_data[pn_y][selection_l]
                                visited.add((selection_l, pn_y))

                            digit = int(digit_str)
                    return digit

                directions = [(x - 1, y - 1), (x + 0, y - 1), (x + 1, y - 1),   # top
                              (x - 1, y + 0), (x + 1, y + 0),                   # sides
                              (x - 1, y + 1), (x + 0, y + 1), (x + 1, y + 1)]   # bottom

                digits = [get_digit(x, y) for (x, y) in directions]    # bottom
                schematic_sum += sum(digits)
    return schematic_sum


def solve_part2(in_data):
    # data is a grid with origin at top left
    grid_w = len(in_data[0])
    grid_h = len(in_data)
    gear_ratio_sum = 0

    def is_in_bounds(x, y):
        return 0 <= x < grid_w and 0 <= y < grid_h

    def is_symbol(c):
        return not str(c).isdigit() and c != '.'

    for y, row_data in enumerate(in_data):
        for x, c in enumerate(row_data):
            if is_symbol(c):
                # If it's a symbol, we check the surrounding grid cells for digits
                visited = set()  # Store visited grid cells so we don't re-consider them

                def get_digit(pn_x, pn_y):
                    digit = 0
                    if (pn_x, pn_y) in visited:
                        return 0

                    if is_in_bounds(pn_x, pn_y):
                        pn_c = in_data[pn_y][pn_x]
                        if pn_c.isdigit():
                            # Found a digit! Grow selection to get the entire digit
                            selection_l = pn_x
                            digit_str = ""

                            # First grow left
                            while True:
                                if not is_in_bounds(selection_l, pn_y):
                                    break
                                digit_c = in_data[pn_y][selection_l]
                                if not digit_c.isdigit():
                                    break
                                selection_l -= 1

                            # Then from the first character of the digit grow right to assemble the digit
                            while True:
                                if not is_in_bounds(selection_l + 1, pn_y):
                                    break
                                selection_l += 1
                                digit_c = in_data[pn_y][selection_l]
                                if not digit_c.isdigit():
                                    break
                                digit_str += in_data[pn_y][selection_l]
                                visited.add((selection_l, pn_y))

                            digit = int(digit_str)
                    return digit

                digits = []
                directions = [(x - 1, y - 1), (x + 0, y - 1), (x + 1, y - 1),   # top
                              (x - 1, y + 0), (x + 1, y + 0),                   # sides
                              (x - 1, y + 1), (x + 0, y + 1), (x + 1, y + 1)]   # bottom

                # This time we simply discard the symbol if there is more than 2 digits surrounding the symbol.
                for (dir_x, dir_y) in directions:
                    part_val = get_digit(dir_x, dir_y)
                    if part_val != 0:   # Assuming there is no 0 part number
                        digits.append(part_val)

                if len(digits) == 2:
                    gear_ratio_sum += digits[0] * digits[1]
    return gear_ratio_sum


if __name__ == "__main__":
    data = get_input()

    result = solve_part1(data)
    print(f"Results part 1: {result}")

    result = solve_part2(data)
    print(f"Results part 2: {result}")
