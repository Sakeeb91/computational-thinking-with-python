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
            # Setup: add project root so we can import shared helpers across notebooks.
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
            - Look for **Show/hide** sections; click to reveal extra guidance or answers when you feel stuck.
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
                \"\"\"Remove sentinel values and convert the rest to floats to keep only usable data in original order.\"\"\"
                # TODO: implement following the step-by-step hint above
                raise NotImplementedError


            def running_totals(numbers):
                \"\"\"Carry a running sum across the loop so each position shows progress so far.\"\"\"
                # TODO: implement using an accumulator pattern
                raise NotImplementedError


            def count_vowels(text):
                \"\"\"Count vowels case-insensitively to practice simple string scanning.\"\"\"
                # TODO: implement using lowercase text and a small vowel set
                raise NotImplementedError
            """
        ),
        md_cell(
            """
            ### Checkpoint — get quick wins

            Run the next cell. Each `[PASS]` is a dopamine hit. If something fails, reread the hint and add a `print` to see intermediate values.
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
        md_cell(
            """
            ### Interview warm-up (click to reveal answers)

            <details>
            <summary>How would you describe a function to someone new to code?</summary>
            A named mini-machine: you give it inputs, it performs steps, and hands back an output. Good functions do one clear job.
            </details>

            <details>
            <summary>When would you choose a <code>for</code> loop over <code>while</code>?</summary>
            Use a <code>for</code> loop when you know the collection or number of steps ahead of time; use <code>while</code> for open-ended repetition until a condition changes.
            </details>

            <details>
            <summary>Why convert text to lowercase before counting vowels?</summary>
            To make the check case-insensitive, so 'A' and 'a' are both counted without duplicating logic.
            </details>
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
                \"\"\"Split tasks into equally sized chunks so work can be batched without changing order.\"\"\"
                # TODO: implement using slicing in a step loop
                raise NotImplementedError


            def simulate_robot(commands):
                \"\"\"Translate direction letters into x/y moves to track the robot's final position.\"\"\"
                # TODO: implement with simple if/elif updates to x and y
                raise NotImplementedError


            def estimate_timeline(steps):
                \"\"\"Separate serial work from parallel work so time adds correctly (serial sum + longest parallel block).\"\"\"
                # TODO: implement by tracking serial_time and parallel_times
                raise NotImplementedError
            """
        ),
        md_cell(
            """
            ### Checkpoint — run and reflect

            Run the next cell to see passes/fails. If something breaks, add a quick `print` inside your function to see what's happening before and after each branch.
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
        md_cell(
            """
            ### Interview warm-up (click to reveal answers)

            <details>
            <summary>What does decomposition mean in problem solving?</summary>
            Breaking a big, fuzzy problem into small, crisp steps you can solve and test independently.
            </details>

            <details>
            <summary>How do you decide between <code>if/elif/else</code> and a lookup table (dict)?</summary>
            Use <code>if/elif/else</code> for a few simple branches; use a dict mapping keys to actions/data when you have many cases and want quick lookups.
            </details>

            <details>
            <summary>Why track parallelizable vs non-parallelizable work separately?</summary>
            Because overlapping tasks shouldn't be double-counted; splitting them lets you add serial time and only the longest parallel block once.
            </details>
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
                \"\"\"Use a dict for O(1) lookups so we find a pair adding to target in one pass.\"\"\"
                # TODO: implement using the seen dictionary pattern
                raise NotImplementedError


            def word_frequencies(text):
                \"\"\"Normalize case/punctuation, then count words to show how preprocessing simplifies logic.\"\"\"
                # TODO: implement by lowercasing, stripping punctuation, and counting
                raise NotImplementedError


            def merge_sorted(left, right):
                \"\"\"Walk both sorted lists with indices to build a single sorted output in linear time.\"\"\"
                # TODO: implement with two-pointer merge logic
                raise NotImplementedError
            """
        ),
        md_cell(
            """
            ### Checkpoint — test and tune

            The next cell runs quick checks. If a test fails, print intermediate variables (like your dictionary or indices) to see where your reasoning differs from the expected behavior.
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
        md_cell(
            """
            ### Interview warm-up (click to reveal answers)

            <details>
            <summary>Why does a dict-based two-sum check run in O(n)?</summary>
            Each lookup and insert in a dict is expected O(1), so you pass through the list once.
            </details>

            <details>
            <summary>How would you handle punctuation and case when counting words?</summary>
            Normalize first: lowercase the text, strip or replace punctuation with spaces, then split and count.
            </details>

            <details>
            <summary>How can you merge two sorted lists without resorting to full re-sort?</summary>
            Walk both lists with indices, always taking the smaller next item; this is linear time because you never backtrack.
            </details>
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
                \"\"\"Recursively open nested lists so all ints appear in order in a single list.\"\"\"
                # TODO: implement using recursion and list extension
                raise NotImplementedError


            def count_paths(rows, cols):
                \"\"\"Use the idea 'paths from above + paths from left' to count ways across the grid.\"\"\"
                # TODO: implement with recursion (optional memo) or DP table
                raise NotImplementedError


            def path_exists(grid, start, goal):
                \"\"\"Search the grid (DFS/BFS) avoiding walls and revisits to see if start can reach goal.\"\"\"
                # TODO: implement with a stack/queue and visited set
                raise NotImplementedError
            """
        ),
        md_cell(
            """
            ### Checkpoint — trace your recursion/search

            Run the next cell. If something fails, add prints to show arguments at each recursive call or the contents of your stack/queue to see where the exploration goes.
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
        md_cell(
            """
            ### Interview warm-up (click to reveal answers)

            <details>
            <summary>What is the base case in a recursive function?</summary>
            A stopping condition that returns a direct answer without further recursion, preventing infinite descent.
            </details>

            <details>
            <summary>How do you avoid revisiting nodes in a DFS/BFS?</summary>
            Keep a `visited` set; mark nodes as visited when you add them to the stack/queue so you never enqueue the same position twice.
            </details>

            <details>
            <summary>Why might memoization help in the grid paths problem?</summary>
            Many subproblems repeat (same `rows, cols`), so caching previous answers avoids exponential re-computation.
            </details>
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
                \"\"\"Apply Kahn's algorithm: peel off indegree-0 nodes to produce a valid ordering or detect a cycle.\"\"\"
                # TODO: implement with indegree tracking and a queue
                raise NotImplementedError


            def shortest_path_grid(grid, start, goal):
                \"\"\"Use BFS layers to find the minimum steps from start to goal in an unweighted grid.\"\"\"
                # TODO: implement with a queue and visited set
                raise NotImplementedError


            def schedule_by_deadline(tasks):
                \"\"\"Greedily sort by deadline (then duration) to produce a reasonable execution order quickly.\"\"\"
                # TODO: implement with a two-key sort and return names
                raise NotImplementedError
            """
        ),
        md_cell(
            """
            ### Checkpoint — verify ordering and paths

            Run the next cell. If something fails, print your indegree table for topo sort or the queue contents for BFS to see where logic diverges.
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
        md_cell(
            """
            ### Interview warm-up (click to reveal answers)

            <details>
            <summary>How do you detect a cycle in topological sorting?</summary>
            If you process nodes with indegree 0 and the final ordering has fewer nodes than the graph, a cycle prevented some nodes from ever reaching indegree 0.
            </details>

            <details>
            <summary>Why does BFS give shortest path length in an unweighted grid?</summary>
            BFS explores in layers by distance; the first time you reach the goal is guaranteed to be the minimum number of steps.
            </details>

            <details>
            <summary>What is a greedy choice in scheduling by deadline?</summary>
            Always pick the available task with the earliest deadline (and shorter duration on ties) to minimize lateness locally, which leads to a good global order here.
            </details>
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
                \"\"\"Monte Carlo: sample points, count hits inside quarter-circle, and scale by 4 for a pi estimate.\"\"\"
                # TODO: implement using the hint steps and random.random()
                raise NotImplementedError


            def rolling_mean(window, values):
                \"\"\"Maintain a small sliding window so each output is the average of the most recent values.\"\"\"
                # TODO: implement by adding/removing values as you iterate
                raise NotImplementedError


            def conversion_lift(visitors):
                \"\"\"Count conversions per variant, compute rates, then report lift (rate_B - rate_A).\"\"\"
                # TODO: implement with basic counters and safe division
                raise NotImplementedError
            """
        ),
        md_cell(
            """
            ### Checkpoint — sanity-check randomness and metrics

            Run the next cell. If something fails, print sample counts or the running window to see whether your math aligns with the intended formulas.
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
        md_cell(
            """
            ### Interview warm-up (click to reveal answers)

            <details>
            <summary>Why set a random seed in simulations?</summary>
            It makes results repeatable so you can debug and compare runs reliably.
            </details>

            <details>
            <summary>How would you explain a rolling mean to a stakeholder?</summary>
            It's the average of the most recent N values, updating as new data arrives, which smooths noise while staying up to date.
            </details>

            <details>
            <summary>What is conversion lift?</summary>
            The difference in conversion rates between variant B and A; a positive lift means B outperforms A.
            </details>
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
