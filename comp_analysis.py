from EXTENDED_BOTTOM_UP_CUT_ROD import calculate_benefit as extended_bottom_up_cut_rod

def test_runtime(func, n, array):
    """
    Executes the given function and returns the solution, cuts, and execution time.
    :param func: Function to test
    :param n: Rod length
    :param array: Benefit array
    :return: Maximum benefit, cut positions, execution time
    """
    sol, cuts, algo_time = func(n, array)
    return sol, cuts, algo_time

if __name__ == "__main__":
    try:
        # Input the total length of the rod
        n = int(input("Enter the length of the rod: "))
        
        # Input the benefit values for each cut
        array = input(f"Enter the benefit for each cut - {n} integers separated by space: ").split()
        array = [int(x) for x in array if x.strip()]  # Handle multiple spaces and convert to integers
        
        if len(array) != n:
            print(f"Error: Expected {n} integers, but got {len(array)}.")
        else:
            # Test each version
            print("\nTesting CUT_ROD.py...")
            sol1, cuts1, time1 = test_runtime(extended_bottom_up_cut_rod, n, array)
            print(f"CUT_ROD - Maximum Benefit: {sol1[n]}, Execution Time: {time1:.6f} secs")

            print("\nTesting BOTTOM_UP_CUT_ROD.py...")
            sol2, cuts2, time2 = test_runtime(extended_bottom_up_cut_rod, n, array)
            print(f"BOTTOM_UP_CUT_ROD - Maximum Benefit: {sol2[n]}, Execution Time: {time2:.6f} secs")

            print("\nTesting EXTENDED_BOTTOM_UP_CUT_ROD.py...")
            sol3, cuts3, time3 = test_runtime(extended_bottom_up_cut_rod, n, array)
            print(f"EXTENDED_BOTTOM_UP_CUT_ROD - Maximum Benefit: {sol3[n]}, Execution Time: {time3:.6f} secs")

            # Compare the results
            print("\nComparison:")
            print(f"CUT_ROD Execution Time: {time1:.6f} secs")
            print(f"BOTTOM_UP_CUT_ROD Execution Time: {time2:.6f} secs")
            print(f"EXTENDED_BOTTOM_UP_CUT_ROD Execution Time: {time3:.6f} secs")
    except ValueError:
        print("Error: Please enter valid integers only.")