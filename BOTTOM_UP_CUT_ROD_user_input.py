import time

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
        # Input the total length of the rod
        n = int(input("Enter the length of the rod: "))

        # Input the benefit values for each cut
        array = input(f"Enter the benefit for each cut - {n} integers separated by space: ").split()
        array = [int(x) for x in array if x.strip()]  # Handle multiple spaces and convert to integers

        # Check if the input benefit array length matches the rod length
        if len(array) != n:
            print(f"Error: Expected {n} integers, but got {len(array)}.")
        else:
            # Call the function to calculate maximum benefit and cuts
            sol, algo_time = bottom_up_cut_rod_calc_benefit(n, array)

            print("\n******* RETULTS **********")
            # Print the maximum benefit
            print(f"The maximum benefit is {sol[n]}")

            # Calculate and print the execution time
            print(f"The algorithm took {algo_time:.6f} secs to execute.\n")

    except ValueError:
        # Handle invalid input errors
        print("Error: Please enter valid integers only.")
