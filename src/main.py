import time

def insertion_sort(arr):
    """
    Performs an Insertion Sort on the provided list

    Insertion  Sort works similarly to the way you sort playing cards in your hands
    The array is virtually split into a sorted and unsorted part
    Values from the unsorted part are picked and placed at the correct position
    in the sorted part
    """

    n = len(arr)

    # We start from the second element (index 1) because a single element (index 0)
    # is considered sorted by default

    for i in range(1, n):

        # Key is the element we are currently trying to place in the sorted portion

        key = arr[i]

        # Initialize "j" to be the index of the element just before the key
        # This is where we start comparing the key against the sorted portion

        j = i - 1

        print(f"Step {i}: Picking key {key}")
        visualize_state(arr, i, j + 1)


        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        # This creates the "hole" where  the key will eventually be inserted

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # Shift the element to the right
            j -= 1 # Move pointer to the left

            # Show the shifting process
            visualize_state(arr,i,j+1, highlight_key=False)


        # Place the key into its final sorted postion for this position
        arr[j + 1] = key

        print(f"Result after step {i}:")
        visualize_state(arr,i,j+1, final_pos=True)




def visualize_state(arr, current_idx, active_idx, highlight_key=True, final_pos=False):
    """
    An illustration helper to show the array state in the console.
    Legend:
    [#] : The element currently being moved/sorted (Key)
    | | : Sorted portion boundary
    """
    output = []
    for idx, val in enumerate(arr):
        if idx == active_idx and not final_pos:
            output.append(f"[{val}]") # Highlight moving element
        elif idx <= current_idx:
            output.append(f" {val} ") # Sorted/Processed part
        else:
            output.append(f"({val})") # Unprocessed part
            
    print("  " + " ".join(output))
    # Simple ASCII bar chart visualization
    max_val = max(arr) if arr else 1
    for level in range(max_val, 0, -1):
        line = "    "
        for val in arr:
            if val >= level:
                line += " █ "
            else:
                line += "   "
        print(line)
    print("    " + "---" * len(arr))




def run_examples():
    """
    Demonstrates Insertion Sort with different types of data.
    """
    examples = {
        "Random List": [12, 11, 13, 5, 6],
        "Already Sorted": [1, 2, 3, 4, 5],
        "Reverse Sorted": [9, 7, 5, 3, 1],
        "Duplicate Elements": [4, 2, 4, 3, 1]
    }
    
    for name, data in examples.items():
        print("="*40)
        print(f"TEST CASE: {name}")
        print(f"Original: {data}")
        print("="*40)
        
        test_list = data.copy()
        insertion_sort(test_list)
        
        print(f"\nFinal Sorted List: {test_list}\n")

if __name__ == "__main__":
    # Illustration of the Logic:
    # -------------------------
    # Initial: [12, 11, 13, 5, 6]
    # 1. Key=11. 11 < 12? Yes. Shift 12 right. Insert 11. -> [11, 12, 13, 5, 6]
    # 2. Key=13. 13 < 12? No. Stay.                       -> [11, 12, 13, 5, 6]
    # 3. Key=5.  5 < 13? Yes. 5 < 12? Yes. 5 < 11? Yes.   -> [5, 11, 12, 13, 6]
    # 4. Key=6.  6 < 13? Yes. 6 < 12? Yes. 6 < 11? Yes.   -> [5, 6, 11, 12, 13]

    run_examples()