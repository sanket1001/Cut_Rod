from EXTENDED_BOTTOM_UP_CUT_ROD import calculate_benefit as extended_bottom_up_cut_rod
from CUT_ROD import cut_rod_recursive_with_cuts as cut_rod
from BOTTOM_UP_CUT_ROD import calcBenBU as bottom_up_cut_rod

import random
import matplotlib.pyplot as plt

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
        sol1, time1 = cut_rod(n, array)
        print(f"CUT_ROD - Maximum Benefit: {sol1}, Execution Time: {time1:.6f} secs")

        print("\nTesting BOTTOM_UP_CUT_ROD.py...")
        sol2, time2 = bottom_up_cut_rod(n, array)
        print(f"BOTTOM_UP_CUT_ROD - Maximum Benefit: {sol2[n]}, Execution Time: {time2:.6f} secs")

        print("\nTesting EXTENDED_BOTTOM_UP_CUT_ROD.py...")
        sol3, _, time3 = extended_bottom_up_cut_rod(n, array)
        print(f"EXTENDED_BOTTOM_UP_CUT_ROD - Maximum Benefit: {sol3[n]}, Execution Time: {time3:.6f} secs")

        # Compare the results
        print("\nComparison:")
        print(f"CUT_ROD Execution Time: {time1:.6f} secs")
        print(f"BOTTOM_UP_CUT_ROD Execution Time: {time2:.6f} secs")
        print(f"EXTENDED_BOTTOM_UP_CUT_ROD Execution Time: {time3:.6f} secs")

        time1_list.append(time1)
        time2_list.append(time2)
        time3_list.append(time3)

        if (time1 - time2) > 60.0:
            print("Breaking the loop...")
            break

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