def cut_rod_recursive_with_cuts(length, benefit):
    """
    Recursive function to calculate the maximum benefit from cutting a rod
    and the cuts that produce this benefit.

    :param length: The total length of the rod
    :param benefit: A list where benefit[i] represents the benefit of cutting the rod at length i+1
    :return: A tuple containing the list of maximum benefits, the cuts to achieve it, and execution time
    """
    best_cut=0
    def helper(n):
        if n == 0:
            return 0
        max_val = float('-inf')
        best_cut = 0
        for i in range(1, n + 1):
            current_val = helper(n - i) + helper(i-1)
            if max_val < current_val:
                max_val = current_val
                best_cut = i
        return max_val

    # Start measuring time
    import time
    start_time = time.time()

    # Stop measuring time
    end_time = time.time()
    time_req = end_time - start_time

    return helper(length), best_cut, time_req
