import sys


def test_args():
    """Test command line arguments"""

    # Test number of arguments
    if len(sys.argv) != 3:
        print("Usage: python3.7 main.py <first-string> <second-string>",
              file=sys.stderr)
        exit(-1)

    # Test length of strings
    if len(sys.argv[1]) != len(sys.argv[2]):
        print("Strings are not the same length", file=sys.stderr)
        exit(-1)


def solve():
    """Solve the problem"""

    first_string = sys.argv[1]
    second_string = sys.argv[2]

    # Strings are the same
    if first_string == second_string:
        return 'Not shifted'

    # Compute shifts
    left_shifted_first_string = [
        first_string[i:] + first_string[:i] for i in range(1, len(first_string))]

    # No solution
    if second_string not in left_shifted_first_string:
        return 'No solution'

    # Compute left shifts number
    left_shifts = left_shifted_first_string.index(second_string) + 1

    # Check if right_shifts < left_shifts
    if len(first_string) - left_shifts < left_shifts:
        return f"Right Shifted By {len(first_string) - left_shifts}"
    else:
        return f"Left Shifted By {left_shifts}"


if __name__ == '__main__':
    """Main function"""

    # Test command line arguments
    test_args()

    # Print solution to stdout
    print(solve())
