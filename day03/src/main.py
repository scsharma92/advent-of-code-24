import re

PATTERN = r"mul\(\d{1,3},\d{1,3}\)"

CORRECT_NUMBER_P1 = 182780583
CORRECT_NUMBER_P2 = 90772405

def main():
    input_string = read_input_from_file("input.txt")
    p1_ans = parse_text_part1(input_string)
    if p1_ans != CORRECT_NUMBER_P1:
        raise ValueError(f"{p1_ans} != {CORRECT_NUMBER_P1}")
    print(f"Part 1: Correct, {p1_ans}")

    p2_ans = parse_text_part2(input_string)
    if p2_ans != CORRECT_NUMBER_P2:
        raise ValueError(f"{p2_ans} != CORRCT_NUMBER_P2")
    print(f"Part 2: Correct, {p2_ans}")


def read_input_from_file(fn: str) -> str:
    """Read in the input file and returns the data as a string."""
    with open(fn, "r") as f:
        content = f.read()
    return content


def parse_text_part1(text: str) -> int:
    """
    Takes in an input string, finds the valid substrings for mul(xxx, xxx),
    adds up all the individual values and returns the sum.
    """
    matches = re.findall(PATTERN, text)
    output = 0
    for match in matches:
        num1, num2 = match.replace("mul(", "").replace(")", "").split(",")
        output += int(num1) * int(num2)
    return output


def parse_text_part2(text: str) -> int:
    """
    Takes in an input string, finds the valid substrings for mul(xxx, xxx),
    adds up all the individual values and returns the sum. But this time,
    if there is a don't() in front of the mul(), then do not use it.
    This is counteracted by a do() preceding the mul().
    """
    matches = re.findall(PATTERN, text)
    splits = re.split(PATTERN, text)
    output = 0
    enabled = True
    for _, match in enumerate(matches):
        pre_text = splits[_]
        # Check for any don't()'s that aren't reversed by a do().
        if len(re.findall(r"don't\(\)(?!do\(\))", pre_text)) != 0:
            enabled = False
        # Check for any do()'s that aren't reversed by a don't().
        elif len(re.findall(r"do\(\)(?!don\'t\(\))", pre_text)) != 0:
            enabled = True
        if enabled is True:
            # Remove the mul() wrapping the numbers.
            num1, num2 = match.replace("mul(", "").replace(")", "").split(",")
            output += int(num1) * int(num2)

    return output


if __name__ == "__main__":
    main()
