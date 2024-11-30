
# Rod Cutting Algorithms and Comparative Analysis

This project includes implementations of different rod-cutting algorithms and a comparative runtime analysis tool. Each script processes a rod-cutting problem defined in an input file provided as a command-line argument.

## File Descriptions

1. **`CUT_ROD.py`**  
   Implements the recursive solution for the rod-cutting problem.

2. **`BOTTOM_UP_CUT_ROD.py`**  
   Implements the bottom-up dynamic programming approach to solve the rod-cutting problem.

3. **`EXTENDED_BOTTOM_UP_CUT_ROD.py`**  
   An extended version of the bottom-up dynamic programming approach that also keeps track of cuts to achieve maximum benefit.

4. **`comp_analysis.py`**  
   Compares runtime performance across all algorithms (`CUT_ROD.py`, `BOTTOM_UP_CUT_ROD.py`, and `EXTENDED_BOTTOM_UP_CUT_ROD.py`) until the runtime difference between `CUT_ROD.py` and `BOTTOM_UP_CUT_ROD.py` exceeds 60 seconds. This file imports the above python files and uses their `<file_name>_calc_benefit` function to calculate the benefir and runtime.

5. **`sample_input.txt`**  
   A sample input file containing the problem definition.  
   Format:
   - First line: Length of the rod (`N`).
   - Second line: Space-separated prices for each length (up to `N`).

## How to Run the Scripts

### Dependencies

The scripts require Python 3.x. Ensure that all files are in the same directory for seamless execution.

### Steps

1. **Prepare the Input File**

   The input file (e.g., `sample_input.txt`) must be formatted as follows:

   ```
   <Rod Length>
   <Price 1> <Price 2> <Price 3> ... <Price N>
   ```

2. **Run Individual Algorithms**

   You can run each algorithm by providing the input file name as a command-line argument:

   #### `CUT_ROD.py`
   ```bash
   python CUT_ROD.py sample_input.txt
   ```

   #### `BOTTOM_UP_CUT_ROD.py`
   ```bash
   python BOTTOM_UP_CUT_ROD.py sample_input.txt
   ```

   #### `EXTENDED_BOTTOM_UP_CUT_ROD.py`
   ```bash
   python EXTENDED_BOTTOM_UP_CUT_ROD.py sample_input.txt
   ```

3. **Perform Comparative Runtime Analysis**

   To compare the runtime of the algorithms, run the `comp_analysis.py` file using the following command:

   ```bash
   python comp_analysis.py
   ```

   The script will compare runtimes across all three files by creating its own dataset. It will start with a rod length of 1, incrementing the rod length by 1 and generating the benefit array with random integers.

### Output

Each script will generate the following output:

- The maximum benefit.
- The cuts made to achieve the benefit (only for `EXTENDED_BOTTOM_UP_CUT_ROD.py`).
- The runtime of the algorithm.

The comparative analysis script will output the runtime for all algorithms and stop when the time difference between `CUT_ROD.py` and `BOTTOM_UP_CUT_ROD.py` exceeds 60 seconds.

### Notes

- Ensure all Python scripts and the input file are in the same directory.
- If the input format is incorrect or the file does not exist, the script will display an appropriate error message.
