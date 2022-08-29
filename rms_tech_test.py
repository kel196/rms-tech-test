import numpy as np
import pandas as pd
import argparse as ap

def validate_grid(grid: np.array, contiguous_integers: int):
    # Check contiguous integer is greater than 0
    if contiguous_integers <= 0:
        raise ValueError("Contiguous integers value must be greater than 0.")
    # Check contiguous integer is an integer
    if type(contiguous_integers) != int:
        raise TypeError("Contiguous integers value must be an integer.")
    # Check grid has no null values
    if pd.isnull(grid).any():
        raise ValueError("Grid contains null value.")
    # Check grid has a numpy has non-number values by converting to float
    try: 
        grid.astype(float)
    except:
        raise TypeError("Grid contains non-numeric values")
    # Check grid is at least 1x1
    if grid.shape[0] < 1 or grid.shape[1] < 1:
        raise ValueError("Grid must be at least 1x1")
    # Check grid is wider than contiguous integer size
    if grid.shape[0] < contiguous_integers or grid.shape[1] < contiguous_integers:
        raise ValueError("Grid must be wider and taller than contiguous integers value.")

def find_different_combinations(grid: np.array, contiguous_integers: int) -> int:
    # Calculate row and column count
    row_count = grid.shape[0]
    col_count = grid.shape[1]
    # Calculate number of combinations for vertical, horizontal, and diagonal windows
    vertical_combos = (row_count - (contiguous_integers - 1)) * col_count # Up and Down 
    horizontal_combos = (col_count - (contiguous_integers - 1)) * row_count # Left and Right
    diagonal_combos = ((row_count - (contiguous_integers - 1)) * (col_count - (contiguous_integers - 1)) * 2) # Top-left to bottom-right and Top-right to bottom-left

    return vertical_combos + horizontal_combos + diagonal_combos

def find_greatest_product_of_contiguous_integers(grid: np.array, contiguous_integers: int) -> int:
    # Calculate row and column count
    row_count = grid.shape[0]
    col_count = grid.shape[1]

    # Temporary variables for holding the current highest product
    max_vert_prod = 0
    max_hori_prod = 0
    max_tl_br_prod = 0
    max_tr_bl_prod = 0

    # Parse through the grid of numbers sequentially
    for i in range(row_count):
        for j in range(col_count):
            # Vertical Product Calculation
            if i < (row_count - contiguous_integers + 1):
                # Vertical Product (up/down)
                vertical_arr = grid[i:i+contiguous_integers,j]
                vertical_prod = np.prod(vertical_arr)

                if vertical_prod > max_vert_prod:
                    max_vert_prod = vertical_prod
            
            # Horizontal Product Calculation
            if j < (col_count - contiguous_integers + 1):
                # Horizontal Product (left/right)
                horizontal_arr = grid[i,j:j+contiguous_integers]
                horizontal_prod = np.prod(horizontal_arr)

                if horizontal_prod > max_hori_prod:
                    max_hori_prod = horizontal_prod

            # Diagonal Products Calculation
            if i < (row_count - contiguous_integers + 1) and j < (col_count - contiguous_integers + 1):
                # Top-Left to Bottom-Right Product
                sub_grid = grid[i:] # Remove the i rows from top
                tl_br_arr = sub_grid.diagonal(offset=j)[:contiguous_integers]
                tl_br_prod = np.prod(tl_br_arr)

                if tl_br_prod > max_tl_br_prod:
                    max_tl_br_prod = tl_br_prod
                
                # Top-Right to Bottom-Left Product
                flip_sub_arr = np.fliplr(sub_grid) # Flip array horizontally and reuse topleft-bottomright logic
                tr_bl_arr = flip_sub_arr.diagonal(offset=j)[:contiguous_integers]
                tr_bl_prod = np.prod(tr_bl_arr)

                if tr_bl_prod > max_tr_bl_prod:
                    max_tr_bl_prod = tr_bl_prod

    # Calculate greatest product out of vertical, horizontal and both diagonals
    max_prod = max(max_vert_prod,max_hori_prod,max_tl_br_prod,max_tr_bl_prod)
    return max_prod

if __name__ == '__main__':
    # Parse through arguments
    parser = ap.ArgumentParser()
    parser.add_argument("filepath", type=str)
    parser.add_argument("--contiguous-integers",type=int,default=3,required=False,)
    args = parser.parse_args()
    
    # Extract arguments from args
    contiguous_integers = args.contiguous_integers
    filepath = args.filepath

    # Read in .csv as a dataframe
    df = pd.read_csv(filepath, header=None) # Use pandas to read in as dataframe as better at handling csvs

    # Convert to a numpy array for calculations
    arr = df.to_numpy()

    # Validate grid and contiguous integers before proceeding with calculations
    validate_grid(arr,contiguous_integers)

    # QUESTION 1 - How many different combinations are there?
    total_combos = find_different_combinations(arr,contiguous_integers)
    print("========== QUESTION 1 ==========")
    print("How many different combinations are there of",contiguous_integers,"adjacent numbers in the same direction (up, down, left, right or diagonally) in the",arr.shape[0],"x",arr.shape[1],"grid?")
    print("Answer:",'{:,}'.format(total_combos))

    # QUESTION 2 - Greatest Product of Contiguous Integers
    greatest_product = find_greatest_product_of_contiguous_integers(arr,contiguous_integers)
    print("========== QUESTION 2 ==========")
    print("What is the greatest product of",contiguous_integers,"adjacent numbers in the same direction (up, down, left, right or diagonally) in the",arr.shape[0],"x",arr.shape[1],"grid?")
    print("Answer:",'{:,}'.format(greatest_product))