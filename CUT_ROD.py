import time
import sys
def cut_rod_calc_benefit(length, benefit):
    """
    Recursive function to calculate the maximum benefit from cutting a rod
    and the cuts that produce this benefit.

    :param length: The total length of the rod
    :param benefit: A list where benefit[i] represents the benefit of cutting the rod at length i+1
    :return: An integer containing maximum benefit
    """
    start_time = time.time()
    def helper(n):
        if n == 0:
            return 0
        max_val = float('-inf')
        for i in range(1, n + 1):
            current_val = benefit[i - 1] + helper(n-i)
            if max_val < current_val:
                max_val = current_val        
        return max_val
    solu=helper(length)
    end_time = time.time()
    algo_time = end_time - start_time
    return solu, algo_time

if __name__ == "__main__":
    try:
        # Check if a filename is provided as a command-line argument
        if len(sys.argv) != 2:
            print("Error: Please provide the input filename as a command-line argument.")
            sys.exit(1)

        filename = sys.argv[1]

        # Read the file content
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Parse the file content
        n = int(lines[0].strip())  # First line: length of the rod
        array = list(map(int, lines[1].strip().split()))  # Second line: space-separated prices

        print("Contents of the file:")
        print(f"Length of the rod {n}")
        print(f"Benefit Array {array}")

        # Check if the input benefit array length matches the rod length
        if len(array) != n:
            print(f"Error: Expected {n} integers, but got {len(array)}.")
        else:
            # Call the function to calculate maximum benefit and cuts
            sol, algo_time = cut_rod_calc_benefit(n, array)

            