from EXTENDED_BOTTOM_UP_CUT_ROD import extended_bottom_up_cut_rod_calc_benefit as extended_bottom_up_cut_rod
from CUT_ROD import cut_rod_calc_benefit as cut_rod
from BOTTOM_UP_CUT_ROD import bottom_up_cut_rod_calc_benefit as bottom_up_cut_rod

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
        
        print(f"\nCurrent rod length : {n}")
        rod_sizes.append(n)
        array.append(random.randint(1,2*i+1))
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
        # print("\nComparison:")
        # print(f"CUT_ROD Execution Time: {time1:.6f} secs")
        # print(f"BOTTOM_UP_CUT_ROD Execution Time: {time2:.6f} secs")
        # print(f"EXTENDED_BOTTOM_UP_CUT_ROD Execution Time: {time3:.6f} secs")

        time1_list.append(time1)
        time2_list.append(time2)
        time3_list.append(time3)
        print(f"\nTime difference between CUT ROD and BOTTOM UP CUT ROD runtime : {(time1 - time2):.6f} secs")
        if (time1 - time2) > 60.0:
            print("Breaking the loop...")
            break

        n = n+1
    
    print("\n********* Comparison Results (in secs) **********\n")
    print("| Rod Length | CUT ROD Runtime | BOTTOM UP CUT ROD Runtime | EXTENDED BOTTOM UP CUT ROD Runtime |")
    print("|---------------------------------------------------------------------------------------------- |")
    for i in range(0,n):
        print(f"| {i+1:<10} | {time1_list[i]:<15.6f} | {time2_list[i]:<25.6f} | {time3_list[i]:<34.6f} |")

    print("|---------------------------------------------------------------------------------------------- |")

    print(f"\nThe length of rod when runtime difference between CUT ROD and BOTTOM UP CUT ROD is greater than 60 secs is {n}")

    # Create subplots for four different graphs
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # Graph 1: CUT_ROD Runtime vs Rod Length
    axs[0, 0].plot(rod_sizes, time1_list, label="CUT_ROD Runtime", marker='o', color='blue')
    axs[0, 0].set_title("CUT_ROD Runtime vs Rod Length")
    axs[0, 0].set_xlabel("Rod Length")
    axs[0, 0].set_ylabel("Runtime (seconds)")
    axs[0, 0].grid()
    axs[0, 0].legend()

    # Graph 2: BOTTOM_UP_CUT_ROD Runtime vs Rod Length
    axs[0, 1].plot(rod_sizes, time2_list, label="BOTTOM_UP_CUT_ROD Runtime", marker='o', color='orange')
    axs[0, 1].set_title("BOTTOM_UP_CUT_ROD Runtime vs Rod Length")
    axs[0, 1].set_xlabel("Rod Length")
    axs[0, 1].set_ylabel("Runtime (seconds)")
    axs[0, 1].grid()
    axs[0, 1].legend()

    # Graph 3: EXTENDED_BOTTOM_UP_CUT_ROD Runtime vs Rod Length
    axs[1, 0].plot(rod_sizes, time3_list, label="EXTENDED_BOTTOM_UP_CUT_ROD Runtime", marker='o', color='green')
    axs[1, 0].set_title("EXTENDED_BOTTOM_UP_CUT_ROD Runtime vs Rod Length")
    axs[1, 0].set_xlabel("Rod Length")
    axs[1, 0].set_ylabel("Runtime (seconds)")
    axs[1, 0].grid()
    axs[1, 0].legend()

    # Graph 4: CUT_ROD and BOTTOM_UP_CUT_ROD Runtime vs Rod Length
    axs[1, 1].plot(rod_sizes, time1_list, label="CUT_ROD Runtime", marker='o', color='blue')
    axs[1, 1].plot(rod_sizes, time2_list, label="BOTTOM_UP_CUT_ROD Runtime", marker='o', color='orange')
    # axs[1, 1].plot(rod_sizes, time3_list, label="EXTENDED_BOTTOM_UP_CUT_ROD Runtime", marker='o', color='green')
    axs[1, 1].set_title("All Runtimes vs Rod Length")
    axs[1, 1].set_xlabel("Rod Length")
    axs[1, 1].set_ylabel("Runtime (seconds)")
    axs[1, 1].grid()
    axs[1, 1].legend()

    # Adjust layout for better spacing
    plt.tight_layout()
    plt.show()