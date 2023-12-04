"""
--- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

--- Part Two ---

The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
    Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
    Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
    Game 4 required at least 14 red, 3 green, and 15 blue cubes.
    Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""


def get_input():
    import os
    with open(f"{os.path.basename(__file__)[:-3]}.txt") as f:
        return f.read().splitlines()


def solve_part1(in_data):
    bag_r = 12
    bag_g = 13
    bag_b = 14
    sum_valid_indices = 0

    for game_data in in_data:  # e.g. Game 1: 6 green, 3 blue; 3 red, 1 green; 4 green, 3 red, 5 blue
        print(f"Game data: {game_data}")
        is_possible = True

        game_data_substrs = game_data.split(": ")
        game_id = int(game_data_substrs[0][5::])  # split off the "game " at the beginning

        turn_data = game_data_substrs[1].split("; ")  # e.g. ['6 green, 3 blue', '3 red, 1 green', '4 green, 3 red, 5 blue']
        print(f"Turn data: {turn_data}")

        for draw_data in turn_data:  # One draw of the bag, e.g. '6 green, 3 blue'
            print(f"Draw data: {draw_data}")
            count_r = 0
            count_g = 0
            count_b = 0
            draws = draw_data.split(", ")  # e.g. ['6 green', '3 blue']
            for draw in draws:
                count, color = draw.split(" ")
                if color[0] == 'r':
                    count_r += int(count)
                elif color[0] == 'g':
                    count_g += int(count)
                elif color[0] == 'b':
                    count_b += int(count)

            print(f"r: {count_r}, g: {count_g}, b: {count_b}")
            is_possible = count_r <= bag_r and count_g <= bag_g and count_b <= bag_b
            if not is_possible:
                break

        if is_possible:
            sum_valid_indices += game_id

    return sum_valid_indices


def solve_part2(in_data):
    power_sum = 0
    for game_data in in_data:  # e.g. Game 1: 6 green, 3 blue; 3 red, 1 green; 4 green, 3 red, 5 blue
        print(f"Game data: {game_data}")
        required_r = 0
        required_g = 0
        required_b = 0

        game_data_substrs = game_data.split(": ")

        turn_data = game_data_substrs[1].split("; ")  # e.g. ['6 green, 3 blue', '3 red, 1 green', '4 green, 3 red, 5 blue']
        print(f"Turn data: {turn_data}")

        for draw_data in turn_data:  # One draw of the bag, e.g. '6 green, 3 blue'
            print(f"Draw data: {draw_data}")
            draws = draw_data.split(", ")  # e.g. ['6 green', '3 blue']
            for draw in draws:
                count, color = draw.split(" ")
                if color[0] == 'r':
                    required_r = max(int(count), required_r)
                elif color[0] == 'g':
                    required_g = max(int(count), required_g)
                elif color[0] == 'b':
                    required_b = max(int(count), required_b)

        print(f"r: {required_r}, g: {required_g}, b: {required_b}")
        power_sum += required_r * required_g * required_b
    return power_sum


if __name__ == "__main__":
    data = get_input()

    result = solve_part1(data)
    print(f"Results part 1: {result}")

    result = solve_part2(data)
    print(f"Results part 2: {result}")
