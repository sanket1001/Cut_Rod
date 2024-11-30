import time
import sys

def extended_bottom_up_cut_rod_calc_benefit(length, benefit):
    """
    Function to calculate the maximum benefit from cutting a rod
    and the optimal cuts to achieve this benefit.
    
    :param length: The total length of the rod
    :param benefit: A list where benefit[i] represents the benefit of cutting the rod at length i+1
    :return: A tuple containing the maximum benefit for each length, the cuts to achieve them and the time it took to run the algorithm
    """

    # Start measuring time
    start_time = time.time()

    # Array to store the maximum benefit for each rod length
    sol = [-1] * (length + 1)
    sol[0] = 0  # Base case: Benefit for a rod of length 0 is 0
    
    # Array to store the optimal cut for each length
    cuts = [0] * (length + 1)
    
    # Iterating over rod lengths
    for i in range(1, length + 1):
        for j in range(1, i + 1):
            # Check if cutting the rod at length j provides a greater benefit
            if sol[i] < (sol[i - j] + benefit[j - 1]):
                sol[i] = sol[i - j] + benefit[j - 1]
                cuts[i] = j   # Store the cut that gives the maximum benefit

    # Stop measuring time
    end_time = time.time()
    time_req = end_time - start_time    

    return sol, cuts, time_req


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
            # This function returns 3 outputs, the solution array, optimum cuts and time required to run the array
            sol, cuts, algo_time = extended_bottom_up_cut_rod_calc_benefit(n, array)
            
            print("\n******* RETULTS **********")
            # Print the maximum benefit
            print(f"The maximum benefit is {sol[