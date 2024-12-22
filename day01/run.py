def main():
    """
    Reads in the file and computes the pair-wise distance (part1) and similarity scores (part2)
    between the two lists as detailed in README.txt.
    """
    l1, l2 = read_file_as_lists('input.txt')
    dist = 0
    # The lists are sorted in read_file_as_lists.
    for num1, num2 in zip(sorted(l1), sorted(l2)):
        sub_dist = abs(num1 - num2)
        dist += sub_dist
    correct_answer = 2_815_556
    if dist == correct_answer:
        print(f"Part 1: Correct Answer! {dist}.")
    else:
        print(f"Part 1: Wrong Answer: {dist}. Correct Answer: {correct_answer}.") 
    # Part 2:
    correct_similarity = 23_927_637
    similarity = compute_similarity(l1, l2)
    if similarity == correct_similarity:
        print(f"Part 2: Correct Answer! {similarity}.")
    else:
        print(f"Part 2: Wrong Answer: {similarity}. Correct Answer: {correct_similarity}.")


def read_file_as_lists(fn: str) -> tuple[list[int], list[int]]:
    """
    Reads the input file, assuming a structure like:
        123   321\n
    And returns it as a tuple of two sorted lists of ints.
    """
    l1 = []
    l2 = []
    with open(fn, 'r') as f:
        for line in f:
            p1, p2 = line.split('   ')
            l1.append(int(p1))
            l2.append(int(p2.replace('\n', '')))
    return l1, l2


def compute_similarity(l1: list[int], l2: list[int]) -> int:
    """
    Computes the similarity score as defined in README.txt.
    Counts the number of times each value of l1 exists in l2 and sums the total.
    """
    similarity = 0
    ss = {}
    for num in l1:
        if num not in ss:
            l2_count = len([n for n in l2 if n == num])
            ss[num] = l2_count 
        similarity += num*ss[num]
    return similarity


if __name__ == "__main__":
    main()
