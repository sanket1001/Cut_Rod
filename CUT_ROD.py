import time
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
            sol, algo_time = cut_rod_calc_benefit(n, array)

            print("\n******* RETULTS **********")
            # Print the maximum benefit
            print(f"The maximum benefit is {sol}")

            # Calculate and print the execution time
            print(f"The algorithm took {algo_time:.6f} secs to execute.\n")

    except ValueError:
        # Handle invalid input errors
        print("E