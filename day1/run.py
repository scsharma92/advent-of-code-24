def main():
    """
    Reads in the file and computes the pair-wise distance between the two lists
    as detailed in README.md.
    """
    l1, l2 = read_file_as_lists('input.txt')
    dist = 0
    # The lists are sorted in read_file_as_lists.
    for num1, num2 in zip(sorted(l1), sorted(l2)):
        sub_dist = abs(num1 - num2)
        dist += sub_dist
    correct_answer = 2_815_556
    if dist == correct_answer:
        print("Correct Answer.")
    else:
        print(f"Wrong Answer: {dist}. Correct Answer: {correct_answer}.") 

def read_file_as_lists(fn: str) -> (list[int], list[int]):
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

if __name__ == "__main__":
    main()
