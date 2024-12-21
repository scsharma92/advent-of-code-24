ALLOWED_POS_DIFFS = {1, 2, 3}
ALLOWED_NEG_DIFFS = {-1, -2, -3}


def main():
    "Loads the input file and checks it for correctness."
    output = load_and_tag_input_file("input.txt", part=1)
    p1_is_correct, p1_safe_count = score_output(output, index=-2, n_correct=680)
    print(f"Part1: {p1_is_correct} Safe scores: {p1_safe_count}.")

    p2_is_correct, p2_safe_count = score_output(output, index=-1, n_correct=710)
    print(f"Part2: {p2_is_correct} Safe scores: {p2_safe_count}.")


def score_output(output, index, n_correct) -> tuple[str, int]:
    """Checks the flags for correctness. Assumes a total of 1_000."""
    length = len(output)
    if length != 1_000:
        raise ValueError(f"Length of output is {length}, not 1_000.")
    safety_indicators = [i[index] for i in output]
    if set(safety_indicators).union({0, 1}) != {0, 1}:
        raise ValueError("Some safety indicators are not 0 or 1.")
    safe_count = sum(safety_indicators)
    is_correct = "Correct!" if safe_count == n_correct else "Incorrect :(."
    return is_correct, safe_count


def tag_elements_part1(elements: list[int]) -> int:
    """
    Takes in a list of elements and scores it according to the part.

    For part 1, if any of the elements violate the constraint of all ascending
    or all descending in intervals of 1, 2, or 3, then add a 0 to elements.
    Otherwise, add a 1 to elements.
    """
    fails = 0
    # Compute the first diff to set the direciton.
    start_diff = elements[0] - elements[1]
    # If the first comparison fails, abandon the rest of the comparisons.
    if abs(start_diff) not in ALLOWED_POS_DIFFS:
        return 0
    # Set the direction to multiply against the diffs, starting left to right.        
    start_dir = 1 if start_diff > 0 else -1
    # Iterate through the remaining diffs, one less than total length.
    for i in range(1, len(elements)-1):
        diff = (elements[i] - elements[i+1]) * start_dir
        # If any of the comparisons fail, exit.
        if diff not in ALLOWED_POS_DIFFS:
            return 0
    return 1


def tag_elements_part2(elements: list[int]) -> int:
    """
    Takes in a list of elements and scores it according to part 2 rules.

    For part 2, the constraint is still that the elements should all be
    ascending or descending in intervals of 1, 2, or 3. But this time,
    there is a tolerance of a single element. So if we can satisfy the constraint
    by removing only a single element from the list, then it passes.
    """
    # Check the diffs for the list as a whole. 
    diffs = [elements[i] - elements[i+1] for i in range(len(elements)-1)]
    # If the diffs are valid, return 1.
    if set(diffs).issubset(ALLOWED_POS_DIFFS) or set(diffs).issubset(ALLOWED_NEG_DIFFS):
        return 1
    # Try skipping each element in elements and if any of those partial diffs pass,
    # everything passes, since we are allowing a tolerance of a single bad value.
    for i in range(len(elements)):
        partial_elements = elements[:i] + elements[i+1:]
        partial_diffs = [partial_elements[i] - partial_elements[i+1]
                         for i in range(len(partial_elements)-1)]
        if set(partial_diffs).issubset(ALLOWED_POS_DIFFS) or set(partial_diffs).issubset(ALLOWED_NEG_DIFFS):
            return 1
    return 0



def load_and_tag_input_file(fn: str, part=1) -> list[list[int]]:
    """
    Reads in the input data and returns it as a list of lists of ints.
    The last element is 1 for safe or 0 for unsafe.
    """
    all_elements = []
    with open(fn, "r") as f: 
        for line in f.readlines():
            # Set fails to 0 to start for each line.
            fails = 0
            # Parse the elements from each line as a list.
            elements = [int(i) for i in line.replace("\n", "").split(" ")]
            # Apply the labels for part 1
            elements.append(tag_elements_part1(elements))
            # Apply the labels for part 2
            elements.append(tag_elements_part2(elements[0: -1]))
            all_elements.append(elements)
    return all_elements
if __name__ == "__main__":
    main()
