import time
import sys

def bottom_up_cut_rod_calc_benefit(length, benefit):
    """
    Function to calculate the maximum benefit using Bottom-Up DP approach 
    and the optimal cuts to achieve this benefit.

    :param length: The total length of the rod
    :param benefit: A list where benefit[i] represents the benefit of cutting the rod at length i+1
    :return: A tuple containing the maximum benefit for each length
    """
    start_time = time.time()
    # Array to store the maximum benefit for each rod length
    sol = [0] * (length + 1)

    # Array to store the optimal cut for each length

    # Bottom-Up calculation for each rod length
    for i in range(1, length + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            if max_val < benefit[j - 1] + sol[i - j]:
                max_val = benefit[j - 1] + sol[i - j]
        sol[i] = max_val

    # Stop measuring time
    end_time = time.time()
    algo_time = end_time - start_time
    return sol, algo_time

# Ensuring the main function runs when the script is executed
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
            sol, algo_time = bottom_up_cut_rod_calc_benefit(n, array)

            print("\n******* RESULTS **********")
            # Print th