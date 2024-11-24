from EXTENDED_BOTTOM_UP_CUT_ROD import calculate_benefit as extended_bottom_up_cut_rod
import random
import matplotlib.pyplot as plt

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

    # Input the total length of the rod
    n = 1
    
    # Input the benefit values for each cut
    array = []
    rod_sizes = []
    time1_list = []
    time2_list = []
    time3_list = []

    for i in range(1, 100):

        rod_sizes.append(n)
        array.append(random.randint(1,100))
        # Test each version
        print("\nTesting CUT_ROD.py...")
        sol1, _, time1 = test_runtime(extended_bottom_up_cut_rod, n, array)
        print(f"CUT_ROD - Maximum Benefit: {sol1[n]}, Execution Time: {time1:.6f} secs")

        print("\nTesting BOTTOM_UP_CUT_ROD.py...")
        sol2, _, time2 = test_runtime(extended_bottom_up_cut_rod, n, array)
        print(f"BOTTOM_UP_CUT_ROD - Maximum Benefit: {sol2[n]}, Execution Time: {time2:.6f} secs")

        print("\nTesting EXTENDED_BOTTOM_UP_CUT_ROD.py...")
        sol3, _, time3 = test_runtime(extended_bottom_up_cut_rod, n, array)
        print(f"EXTENDED_BOTTOM_UP_CUT_ROD - Maximum Benefit: {sol3[n]}, Execution Time: {time3:.6f} secs")

        # Compare the results
        print("\nComparison:")
        print(f"CUT_ROD Execution Time: {time1:.6f} secs")
        print(f"BOTTOM_UP_CUT_ROD Execution Time: {time2:.6f} secs")
        print(f"EXTENDED_BOTTOM_UP_CUT_ROD Execution Time: {time3:.6f} secs")

        time1_list.append(time1)
        time2_list.append(time2)
        time3_list.append(time3)

        n = n+1

# Plot all runtimes on the same graph for comparison
plt.figure(figsize=(12, 8))

plt.plot(rod_sizes, time1_list, label="CUT_ROD Runtime", marker='o')
plt.plot(rod_sizes, time2_list, label="BOTTOM_UP_CUT_ROD Runtime", marker='o', color='orange')
plt.plot(rod_sizes, time3_list, label="EXTENDED_BOTTOM_UP_CUT_ROD Runtime", marker='o', color='green')

plt.title("Comparison of Runtimes vs Rod Size")
plt.xlabel("Rod Size")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.grid()
plt.show()