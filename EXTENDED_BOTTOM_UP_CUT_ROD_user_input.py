import time

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
            # This function returns 3 outputs, the solution array, optimum cuts and time required to run the array
            sol, cuts, algo_time = extended_bottom_up_cut_rod_calc_benefit(n, array)
            
            print("\n******* RETULTS **********")
            # Print the maximum benefit
            print(f"The maximum benefit is {sol[n]}")
            
            # Print the sequence of cuts leading to the maximum benefit
            print("Rod cut positions: ", end="")
            i = n
            while i > 0:
                print(f"{cuts[i]} ->", end=" ")
                i = i - cuts[i]
            print("end", end="\n")

            # Calculate and print the execution time
            print(f"The algorithm took {algo_time:.6f} secs to execute.\n")
 
    except ValueError:
        # Handle invalid input errors
        print("Error: Please enter valid integers only.")
