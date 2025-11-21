"""
Programmatically generate the curriculum notebooks.

Run:
    python scripts/create_notebooks.py
"""

import json
import os
import textwrap
from typing import List, Dict, Any


KERNEL_META = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "pygments_lexer": "ipython3"},
}


def _lines(text: str) -> List[str]:
    cleaned = textwrap.dedent(text).strip("\n")
    return [line + "\n" for line in cleaned.splitlines()]


def md_cell(text: str) -> Dict[str, Any]:
    return {"cell_type": "markdown", "metadata": {}, "source": _lines(text)}


def code_cell(text: str) -> Dict[str, Any]:
    return {
        "cell_type": "code",
        "metadata": {},
        "source": _lines(text),
        "execution_count": None,
        "outputs": [],
    }


def write_notebook(path: str, cells: List[Dict[str, Any]]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    nb = {"cells": cells, "metadata": KERNEL_META, "nbformat": 4, "nbformat_minor": 5}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)
    print(f"Wrote {path}")


def base_setup_cells(title: str, description: str) -> List[Dict[str, Any]]:
    return [
        md_cell(f"# {title}\n\n{description}"),
        code_cell(
            """
            import os
            import sys

            PROJECT_ROOT = os.path.abspath(os.path.join("..", ".."))
            if PROJECT_ROOT not in sys.path:
                sys.path.append(PROJECT_ROOT)

            from utils.validation import check_equal, check_true, summary, reset
            reset()
            """
        ),
        md_cell(
            """
            **How to use this notebook**

            - Read the problem and the step-by-step hints first. They are written for a motivated first-time coder.
            - Write your solution code directly below each TODO, keeping functions short and clear.
            - Run the tests cell; if something fails, re-read the hint and add small `print` checks to see what is happening.
            - When all checks pass, add one or two of your own test cases to prove you really understand it.
            """
        ),
    ]


def beginner_python_basics() -> None:
    cells = base_setup_cells(
        "Beginner 01 — Python Basics",
        "Warm up with Python functions, loops, and conditionals. We keep the math simple and walk through the thought process so you can focus on clear steps.",
    )
    cells += [
        md_cell(
            """
            ### Task 1 — Clean noisy readings

            Write `clean_temperature_readings(readings)` that:
            - Removes sentinel values `None` and `-999`.
            - Converts remaining entries to `float` (strings included).
            - Preserves the original order.

            **Why this matters:** Cleaning messy data is a common first step before any analysis.

            **Step-by-step hint:**
            1) Start an empty list for cleaned values.
            2) Loop over each item; `continue` when you see `None` or `-999`.
            3) Convert the item to float with `float(value)` and append it.
            4) Return the cleaned list at the end.
            """
        ),
        md_cell(
            """
            ### Task 2 — Running totals

            Write `running_totals(numbers)` that returns a list of cumulative sums for the input list.

            **Why this matters:** Accumulating state across a loop is a core pattern.

            **Step-by-step hint:**
            1) Keep a `current_sum = 0`.
            2) Loop through each number, add it to `current_sum`.
            3) Append the latest `current_sum` to an output list each time.
            4) Return the output list.
            """
        ),
        md_cell(
            """
            ### Task 3 — Count vowels

            Write `count_vowels(text)` that counts vowels (`a, e, i, o, u`) in a string ignoring case.

            **Why this matters:** Practicing string processing and basic counting.

            **Step-by-step hint:**
            1) Define a string or set of vowels like `vowels = "aeiou"`.
            2) Convert the input `text` to lowercase.
            3) Loop through characters and add 1 when the character is in `vowels`.
            4) Return the final count.
            """
        ),
        code_cell(
            """
            def clean_temperature_readings(readings):
                \"\"\"Remove sentinel values and convert the rest to floats.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def running_totals(numbers):
                \"\"\"Return cumulative sums for all positions in the list.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def count_vowels(text):
                \"\"\"Count vowels in the given text, ignoring case.\"\"\"
                # TODO: implement
                raise NotImplementedError
            """
        ),
        code_cell(
            """
            reset()
            check_equal(
                "clean_temperature_readings",
                clean_temperature_readings([72.5, None, -999, 70, "68.0"]),
                [72.5, 70.0, 68.0],
            )
            check_equal("running_totals simple", running_totals([1, 2, 3, 4]), [1, 3, 6, 10])
            check_equal("running_totals negatives", running_totals([5, -2, 7]), [5, 3, 10])
            check_equal("count_vowels", count_vowels("Computational Thinking"), 8)
            summary()
            """
        ),
    ]
    write_notebook("notebooks/beginner/01_python_basics.ipynb", cells)


def beginner_decomposition_control() -> None:
    cells = base_setup_cells(
        "Beginner 02 — Decomposition and Control Flow",
        "Turn word problems into small steps with loops and if/else. The prompts walk you through the thinking so you can focus on correctness first.",
    )
    cells += [
        md_cell(
            """
            ### Task 1 — Bucket tasks

            Write `bucket_tasks(tasks, bucket_size)` that splits a list of tasks into consecutive buckets of size `bucket_size`.
            The last bucket may be smaller if there are not enough items.

            **Why this matters:** Splitting lists into chunks is handy for batching work.

            **Step-by-step hint:**
            1) Create an empty list `buckets`.
            2) Use a `for` loop with `range(0, len(tasks), bucket_size)` to step through.
            3) Slice the list: `tasks[i:i + bucket_size]` and append that slice to `buckets`.
            4) Return `buckets`.
            """
        ),
        md_cell(
            """
            ### Task 2 — Simulate a grid robot

            Write `simulate_robot(commands)` that starts at `(0, 0)` and moves one unit per character in `commands`.
            Use `N` (up), `E` (right), `S` (down), `W` (left). Return the final `(x, y)` position.

            **Why this matters:** Translating symbols into state updates is a classic control-flow exercise.

            **Step-by-step hint:**
            1) Start `x = 0`, `y = 0`.
            2) Loop through each character in `commands`.
            3) Use `if/elif` to adjust `x` or `y` depending on the direction.
            4) Return `(x, y)` at the end.
            """
        ),
        md_cell(
            """
            ### Task 3 — Estimate a simple project timeline

            Write `estimate_timeline(steps)` where each step is a dict with keys:
            - `name` (string)
            - `time` (minutes, int)
            - `parallelizable` (bool)

            Rules:
            - Parallelizable steps can overlap; count only the **longest** parallelizable step once.
            - Non-parallelizable steps must happen in sequence; sum their times.
            Return the total minutes required.

            **Why this matters:** Separating serial and parallel work builds intuition for scheduling.

            **Step-by-step hint:**
            1) Initialize `serial_time = 0` and `parallel_times = []`.
            2) Loop through steps: if `parallelizable` is True, append its time to `parallel_times`; otherwise add to `serial_time`.
            3) The parallel block contributes `max(parallel_times)` if any exist, else 0.
            4) Total time is `serial_time + parallel_block_time`.
            """
        ),
        code_cell(
            """
            def bucket_tasks(tasks, bucket_size):
                \"\"\"Split tasks into equally sized buckets (last bucket may be shorter).\"\"\"
                # TODO: implement
                raise NotImplementedError


            def simulate_robot(commands):
                \"\"\"Return the final (x, y) after executing N/E/S/W moves from the origin.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def estimate_timeline(steps):
                \"\"\"Compute total minutes using the parallelization rules described above.\"\"\"
                # TODO: implement
                raise NotImplementedError
            """
        ),
        code_cell(
            """
            reset()
            check_equal("bucket_tasks", bucket_tasks(["a", "b", "c", "d", "e"], 2), [["a", "b"], ["c", "d"], ["e"]])
            check_equal("simulate_robot simple", simulate_robot("NNEESW"), (1, 1))

            schedule = [
                {"name": "fetch data", "time": 10, "parallelizable": True},
                {"name": "clean data", "time": 8, "parallelizable": True},
                {"name": "train model", "time": 25, "parallelizable": False},
                {"name": "evaluate", "time": 5, "parallelizable": True},
            ]
            check_equal("estimate_timeline", estimate_timeline(schedule), 35)
            check_equal("estimate_timeline solo", estimate_timeline([{"name": "solo", "time": 4, "parallelizable": False}]), 4)
            summary()
            """
        ),
    ]
    write_notebook("notebooks/beginner/02_decomposition_control.ipynb", cells)


def intermediate_data_structures() -> None:
    cells = base_setup_cells(
        "Intermediate 01 — Data Structures and Complexity",
        "Work with lists and dictionaries while thinking about efficiency. We give direct hints so you can focus on implementing and noticing patterns.",
    )
    cells += [
        md_cell(
            """
            ### Task 1 — Two-sum indices

            Write `two_sum_indices(nums, target)` that returns a tuple of indices `(i, j)` such that `nums[i] + nums[j] == target` and `i < j`.
            Return `None` if no such pair exists. Aim for better than O(n^2).

            **Why this matters:** Hash maps (dicts) give fast lookups.

            **Step-by-step hint:**
            1) Create an empty dict `seen` mapping number -> index.
            2) Loop over indices and values with `enumerate(nums)`.
            3) For each value `v`, compute `needed = target - v`.
            4) If `needed` is already in `seen`, return `(seen[needed], i)`.
            5) Otherwise store `seen[v] = i`.
            6) If the loop ends, return `None`.
            """
        ),
        md_cell(
            """
            ### Task 2 — Word frequencies

            Write `word_frequencies(text)` that:
            - Treats words case-insensitively.
            - Strips punctuation `. , ! ? ; :`.
            - Returns a dictionary mapping word -> count.

            **Why this matters:** Counting words is a simple but common text-processing task.

            **Step-by-step hint:**
            1) Define a small string of punctuation characters to remove.
            2) Lowercase the text.
            3) Replace each punctuation character with a space (simple and clear).
            4) Split on whitespace to get words.
            5) Loop through words and update counts in a dict.
            """
        ),
        md_cell(
            """
            ### Task 3 — Merge two sorted lists

            Write `merge_sorted(left, right)` that merges two sorted lists into a single sorted list in O(n) time.

            **Why this matters:** Merging is the heart of algorithms like merge sort.

            **Step-by-step hint:**
            1) Keep two indices `i` and `j` starting at 0.
            2) While both lists have remaining items, compare `left[i]` and `right[j]`.
            3) Append the smaller one and advance that index.
            4) When one list is finished, extend with the remainder of the other list.
            """
        ),
        code_cell(
            """
            def two_sum_indices(nums, target):
                \"\"\"Return indices (i, j) of two numbers adding to target, or None.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def word_frequencies(text):
                \"\"\"Return a dict of word counts, case-insensitive and punctuation-free.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def merge_sorted(left, right):
                \"\"\"Merge two sorted lists into one sorted list.\"\"\"
                # TODO: implement
                raise NotImplementedError
            """
        ),
        code_cell(
            """
            reset()
            check_equal("two_sum_indices hit", two_sum_indices([2, 7, 11, 15], 9), (0, 1))
            check_equal("two_sum_indices none", two_sum_indices([1, 2, 3], 7), None)

            check_equal(
                "word_frequencies",
                word_frequencies("Maps map minds; minds map futures."),
                {"maps": 1, "map": 2, "minds": 2, "futures": 1},
            )

            check_equal("merge_sorted simple", merge_sorted([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
            check_equal("merge_sorted duplicates", merge_sorted([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3])
            summary()
            """
        ),
    ]
    write_notebook("notebooks/intermediate/01_data_structures_complexity.ipynb", cells)


def intermediate_recursion_search() -> None:
    cells = base_setup_cells(
        "Intermediate 02 — Recursion and Search",
        "Use recursion to break down nested structures and search a grid. The guidance is explicit so you can concentrate on translating the steps into code.",
    )
    cells += [
        md_cell(
            """
            ### Task 1 — Flatten nested lists

            Write `flatten(nested)` that takes a list containing integers or other lists and returns a single flat list of integers in order.

            **Why this matters:** Recursion lets you handle unknown depth cleanly.

            **Step-by-step hint:**
            1) Create an empty `result` list.
            2) Loop through each item in `nested`.
            3) If the item is an `int`, append it.
            4) If the item is a `list`, recursively flatten it and extend `result` with that.
            5) Return `result`.
            """
        ),
        md_cell(
            """
            ### Task 2 — Count grid paths

            Write `count_paths(rows, cols)` that returns the number of unique paths from the top-left to bottom-right of a grid
            when you can only move **right** or **down**. Use recursion or dynamic programming.

            **Why this matters:** Classic combinatorial thinking; the subproblems repeat.

            **Step-by-step hint (recursive):**
            1) Base case: if `rows == 1` or `cols == 1`, there is only 1 path.
            2) Otherwise, paths = paths from above + paths from left.
            3) Translate that into recursive calls: `count_paths(rows - 1, cols) + count_paths(rows, cols - 1)`.
            4) For speed, you can use a small memo dict (optional for these sizes).
            """
        ),
        md_cell(
            """
            ### Task 3 — Path existence in a maze

            Write `path_exists(grid, start, goal)` where `grid` is a 2D list containing `0` (open) and `1` (wall).
            Return `True` if there is a path from `start` to `goal` moving in 4 directions, else `False`.

            **Why this matters:** Depth-first search (DFS) is a foundational pattern.

            **Step-by-step hint:**
            1) Use a stack or recursion. Create a `visited` set to avoid loops.
            2) Start from `start` and explore neighbors (up, down, left, right) that are inside the grid and open (`0`).
            3) If you reach `goal`, return True.
            4) If you exhaust all options, return False.
            """
        ),
        code_cell(
            """
            def flatten(nested):
                \"\"\"Flatten a nested list of integers while preserving order.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def count_paths(rows, cols):
                \"\"\"Return the number of paths from (0,0) to (rows-1, cols-1) moving only right or down.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def path_exists(grid, start, goal):
                \"\"\"Return True if a path exists in the grid from start to goal using 4-directional moves.\"\"\"
                # TODO: implement
                raise NotImplementedError
            """
        ),
        code_cell(
            """
            reset()
            check_equal("flatten mixed", flatten([1, [2, [3, 4], 5], [6]]), [1, 2, 3, 4, 5, 6])
            check_equal("flatten already flat", flatten([1, 2, 3]), [1, 2, 3])

            check_equal("count_paths 2x3", count_paths(2, 3), 3)
            check_equal("count_paths 3x3", count_paths(3, 3), 6)

            grid1 = [
                [0, 0, 1],
                [1, 0, 0],
                [1, 0, 0],
            ]
            grid2 = [
                [0, 1],
                [1, 0],
            ]
            check_true("path_exists reachable", path_exists(grid1, (0, 0), (2, 2)))
            check_true("path_exists blocked", not path_exists(grid2, (0, 0), (1, 1)))
            summary()
            """
        ),
    ]
    write_notebook("notebooks/intermediate/02_recursion_search.ipynb", cells)


def advanced_algorithm_design() -> None:
    cells = base_setup_cells(
        "Advanced 01 — Algorithm Design and Graphs",
        "Apply graph thinking to ordering problems and shortest paths. Even though this is 'advanced', the hints walk you through the algorithm shapes.",
    )
    cells += [
        md_cell(
            """
            ### Task 1 — Topological sort

            Write `topological_sort(num_nodes, edges)` where nodes are labeled `0..num_nodes-1` and `edges` is a list of `(u, v)` pairs meaning `u` must come before `v`.
            Return a valid ordering list or raise `ValueError` if the graph has a cycle.

            **Why this matters:** Scheduling with dependencies shows up everywhere.

            **Step-by-step hint (Kahn's algorithm):**
            1) Compute indegrees (how many prerequisites) for each node.
            2) Start a queue with all nodes that have indegree 0.
            3) Repeatedly pop from the queue, add to ordering, and reduce indegree of its outgoing neighbors.
            4) If a neighbor's indegree hits 0, push it into the queue.
            5) At the end, if ordering length is num_nodes, return it; else raise `ValueError` for a cycle.
            """
        ),
        md_cell(
            """
            ### Task 2 — Shortest path in a grid

            Write `shortest_path_grid(grid, start, goal)` that returns the length (number of steps) of the shortest path in a 0/1 grid.
            Return `None` if no path exists. Use BFS.

            **Why this matters:** Breadth-first search (BFS) finds shortest paths in unweighted graphs.

            **Step-by-step hint:**
            1) Use a queue storing `(position, distance_so_far)`.
            2) Begin with `start` at distance 0; mark it visited.
            3) Pop from the queue, and if it's the goal, return the distance.
            4) Otherwise, push all open, in-bounds neighbors that are not visited, with distance + 1.
            5) If the queue empties without reaching goal, return `None`.
            """
        ),
        md_cell(
            """
            ### Task 3 — Greedy scheduling by deadlines

            Write `schedule_by_deadline(tasks)` where each task is a dict with keys:
            - `name` (string)
            - `duration` (int)
            - `deadline` (int)

            Use an **earliest deadline first** strategy; on ties, pick the shorter duration first.
            Return an ordered list of task names.

            **Why this matters:** Greedy rules are simple to implement if stated clearly.

            **Step-by-step hint:**
            1) Sort the tasks by deadline ascending, then by duration ascending (two-key sort).
            2) After sorting, return a list of the task names in that order.
            """
        ),
        code_cell(
            """
            def topological_sort(num_nodes, edges):
                \"\"\"Return a topo order for the DAG or raise ValueError on cycles.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def shortest_path_grid(grid, start, goal):
                \"\"\"Return the shortest path length in a 0/1 grid using BFS, or None if unreachable.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def schedule_by_deadline(tasks):
                \"\"\"Order tasks by earliest deadline, breaking ties with shorter duration.\"\"\"
                # TODO: implement
                raise NotImplementedError
            """
        ),
        code_cell(
            """
            reset()

            order = topological_sort(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
            check_true(
                "topological_sort respects edges",
                order.index(0) < order.index(1) and order.index(0) < order.index(2) and order.index(1) < order.index(3) and order.index(2) < order.index(3),
            )

            grid = [
                [0, 0, 0],
                [1, 1, 0],
                [0, 0, 0],
            ]
            check_equal("shortest_path_grid reachable", shortest_path_grid(grid, (0, 0), (2, 2)), 5)
            check_equal("shortest_path_grid blocked", shortest_path_grid([[0, 1], [1, 0]], (0, 0), (1, 1)), None)

            tasks = [
                {"name": "A", "duration": 3, "deadline": 5},
                {"name": "B", "duration": 2, "deadline": 3},
                {"name": "C", "duration": 1, "deadline": 3},
            ]
            check_equal("schedule_by_deadline", schedule_by_deadline(tasks), ["B", "C", "A"])
            summary()
            """
        ),
    ]
    write_notebook("notebooks/advanced/01_algorithm_design.ipynb", cells)


def advanced_experiments_evaluation() -> None:
    cells = base_setup_cells(
        "Advanced 02 — Experiments and Evaluation",
        "Practice simulation, streaming computations, and small evaluators. The steps are spelled out so you can focus on translating math ideas into code.",
    )
    cells += [
        md_cell(
            """
            ### Task 1 — Monte Carlo estimation

            Write `estimate_pi(num_samples, seed=0)` that uses Monte Carlo sampling within the unit square to estimate pi.

            **Why this matters:** Simulations connect randomness to approximate answers.

            **Step-by-step hint:**
            1) Set the random seed for reproducibility.
            2) Loop `num_samples` times: draw `x` and `y` uniformly in [0, 1).
            3) Count how many points land inside the quarter-circle: `x*x + y*y <= 1`.
            4) Fraction inside × 4 ≈ pi.
            """
        ),
        md_cell(
            """
            ### Task 2 — Rolling mean for streams

            Write `rolling_mean(window, values)` that returns a list where each entry is the mean of the last `window`
            values seen so far (or fewer for the first few entries).

            **Why this matters:** Streaming calculations avoid storing everything.

            **Step-by-step hint:**
            1) Keep a sliding window list (or use indices).
            2) As you iterate over `values`, append the new value to the window.
            3) If the window is longer than `window`, remove the oldest item.
            4) Compute the mean of the current window and append it to the output.
            """
        ),
        md_cell(
            """
            ### Task 3 — Simple A/B test metric

            Write `conversion_lift(visitors)` where `visitors` is a list of dicts with keys:
            - `variant` (string: `"A"` or `"B"`)
            - `converted` (bool)

            Return a dict with conversion rates for A and B and the lift (`B - A`).

            **Why this matters:** Turning raw events into metrics is at the heart of experimentation.

            **Step-by-step hint:**
            1) Track totals and conversions for A and B separately.
            2) After counting, rate = conversions / total (guard against divide-by-zero if needed).
            3) Lift = rate_B - rate_A.
            4) Return a dict with keys `rate_A`, `rate_B`, `lift`.
            """
        ),
        code_cell(
            """
            import random


            def estimate_pi(num_samples, seed=0):
                \"\"\"Estimate pi using random sampling inside a unit square.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def rolling_mean(window, values):
                \"\"\"Return a list of rolling means using the last `window` values at each step.\"\"\"
                # TODO: implement
                raise NotImplementedError


            def conversion_lift(visitors):
                \"\"\"Compute conversion rates for A and B and the lift (B - A).\"\"\"
                # TODO: implement
                raise NotImplementedError
            """
        ),
        code_cell(
            """
            reset()
            estimate = estimate_pi(2000, seed=42)
            check_true("estimate_pi reasonable", 3.0 < estimate < 3.3)

            check_equal("rolling_mean small window", rolling_mean(3, [1, 2, 3, 4, 5]), [1.0, 1.5, 2.0, 3.0, 4.0])

            visitors = [
                {"variant": "A", "converted": False},
                {"variant": "A", "converted": True},
                {"variant": "B", "converted": True},
                {"variant": "B", "converted": True},
                {"variant": "B", "converted": False},
            ]
            result = conversion_lift(visitors)
            check_equal("conversion_lift keys", set(result.keys()), {"rate_A", "rate_B", "lift"})
            check_true("conversion_lift values", abs(result["rate_A"] - 0.5) < 1e-9 and abs(result["rate_B"] - (2 / 3)) < 1e-9)
            check_true("conversion_lift lift", abs(result["lift"] - (2 / 3 - 0.5)) < 1e-9)
            summary()
            """
        ),
    ]
    write_notebook("notebooks/advanced/02_experiments_evaluation.ipynb", cells)


def main():
    beginner_python_basics()
    beginner_decomposition_control()
    intermediate_data_structures()
    intermediate_recursion_search()
    advanced_algorithm_design()
    advanced_experiments_evaluation()


if __name__ == "__main__":
    main()
