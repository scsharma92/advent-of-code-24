def main():
    "Loads the input file and checks it for correctness."
    all_scores = load_and_score_input_file("input.txt")
    safety_indicators = [i[-1] for i in all_scores]
    safe_count = sum(safety_indicators)
    unsafe_count = len(safety_indicators) - safe_count
    is_correct = "Correct!" if safe_count == 680 and unsafe_count == 320 else "Incorrect :(."
    print(f"{is_correct} Safe scores: {safe_count}. Unsafe scores: {unsafe_count}")

def load_and_score_input_file(fn: str) -> list[list[int]]:
    """
    Reads in the input data and returns it as a list of lists of ints.
    The last element is 1 for safe or 0 for unsafe.
    """
    all_elements = []
    allowed_abs_diffs = [1, 2, 3]
    with open(fn, "r") as f: 
        for line in f.readlines():
            # Parse the elements from each line as a list.
            elements = [int(i) for i in line.replace("\n", "").split(" ")]
            # Compute the first diff to set the direction.
            start_diff = elements[0] - elements[1]
            # If the first comparison fails, abandon the rest of the comparisons.
            if abs(start_diff) not in allowed_abs_diffs:
                elements.append(0)
                all_elements.append(elements)
                continue
            # Set the direction to multiply against the diffs, starting left to right.
            start_dir = 1 if start_diff > 0 else -1
            # Iterate through the remaining diffs, one less than total length.
            for i in range(1, len(elements)-1):
                # Set passed to 1 for each line. Change to 0 later is something fails.
                passed = 1
                diff = (elements[i] - elements[i+1]) * start_dir
                # If any of the comparisons fail, exit.
                if diff not in allowed_abs_diffs:
                    elements.append(0)
                    passed = 0
                    break
            if passed == 1:
                elements.append(1)
            all_elements.append(elements)
    return all_elements
if __name__ == "__main__":
    main()
