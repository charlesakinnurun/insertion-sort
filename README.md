<h1 align="center">Insertion Sort</h1>

## Overview

**Insertion Sort** is a simple and intuitive sorting algorithm that works the way you might sort playing cards in your hand.

It builds the final sorted array one element at a time, inserting each new element into its correct position among the already-sorted elements.

It is known for being:

* ✅ Easy to understand and implement
* ✅ Efficient for small or nearly sorted datasets
* ✅ Stable sorting algorithm
* ❌ Inefficient for large datasets


<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ How Insertion Sort Works

1. Assume the first element is already sorted.
2. Take the next element and compare it with the previous ones.
3. Shift larger elements to the right.
4. Insert the element into its correct position.
5. Repeat until the list is sorted.

---

### Example Walkthrough

Sort this list:

```
[8, 3, 5, 2]
```

Step-by-step:

```
[8] | 3 5 2      → insert 3 before 8 → [3, 8, 5, 2]
[3, 8] | 5 2     → insert 5 between → [3, 5, 8, 2]
[3, 5, 8] | 2    → insert 2 at start → [2, 3, 5, 8]
```

Final result:

```
[2, 3, 5, 8]
```

---

## ⏱️ Time & Space Complexity

| Case                       | Time Complexity |
| -------------------------- | --------------- |
| Best Case (already sorted) | O(n)            |
| Average Case               | O(n²)           |
| Worst Case                 | O(n²)           |

Space Complexity: O(1) (in-place)

---

## 🧠 Python Implementation

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key in correct position
        arr[j + 1] = key

    return arr


# Example usage
numbers = [8, 3, 5, 2]
print(insertion_sort(numbers))
# Output: [2, 3, 5, 8]
```

---

## 🧪 Example Runs

### Example 1

Input:

```
[7, 4, 1, 9]
```

Output:

```
[1, 4, 7, 9]
```

### Example 2

Input:

```
[5, 2, 9, 1, 5, 6]
```

Output:

```
[1, 2, 5, 5, 6, 9]
```

---

## 👍 Advantages

* Simple and easy to implement
* Works well for small datasets
* Efficient for nearly sorted lists
* Stable sorting algorithm
* In-place (no extra memory needed)

---

## 👎 Disadvantages

* Slow for large datasets
* Performs many shifts when data is unsorted
* Much less efficient than O(n log n) algorithms

---

## 📌 When to Use Insertion Sort

Use Insertion Sort when:

* Sorting small arrays
* The list is nearly sorted
* Memory usage must be minimal
* Simplicity is more important than speed

---

## 🏁 Summary

Insertion Sort is a straightforward algorithm that is excellent for teaching sorting concepts and handling small or nearly sorted data. While not suitable for large datasets, its simplicity and stability make it useful in many practical scenarios.
