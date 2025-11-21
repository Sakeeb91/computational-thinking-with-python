Computational Thinking with Python
==================================

This repository is a two-week, notebook-driven curriculum to practice computational thinking with Python. The path is divided into beginner, intermediate, and advanced tracks, each with clear tasks and validation tests inside the notebooks so learners get immediate feedback.

Quick start
-----------
- Install Python 3.10+.
- Create a virtual environment: `python -m venv .venv && source .venv/bin/activate` (Windows: `.venv\\Scripts\\activate`).
- Install tools: `pip install -r requirements.txt`.
- Launch Jupyter: `jupyter lab` or `jupyter notebook`, then open the notebooks in `notebooks/`.
- Each notebook has TODOs to fill in and a "Run tests" cell; keep running it until all checks pass.

Project layout
--------------
- `notebooks/beginner/` — on-ramp to Python, decomposition, and control flow.
- `notebooks/intermediate/` — data structures, complexity intuition, recursion, and search.
- `notebooks/advanced/` — algorithm design, graphs, experimentation, and evaluation.
- `utils/validation.py` — lightweight helpers used by tests inside notebooks.
- `scripts/create_notebooks.py` — regenerates the notebook files if you want to tweak content programmatically.
- `requirements.txt` — minimal tools for running the notebooks.

Two-week plan (suggested pace)
------------------------------
Each day is scoped to 60–90 focused minutes. Stretch if you need more practice.

- Day 1: Set up environment; run through `beginner/01_python_basics.ipynb`.
- Day 2: Finish basics; rerun tests; short reflection on habits.
- Day 3: `beginner/02_decomposition_control.ipynb` (decomposition, control flow, small simulations).
- Day 4: Extend Day 3 tasks or create a mini kata; journal on abstraction choices.
- Day 5: `intermediate/01_data_structures_complexity.ipynb` (lists, dicts, big-O reasoning).
- Day 6: Add your own test cases to the same notebook; measure simple timing with `%timeit`.
- Day 7: `intermediate/02_recursion_search.ipynb` (recursion patterns, search in grids).
- Day 8: Refactor solutions for clarity; compare recursive vs iterative trade-offs.
- Day 9: `advanced/01_algorithm_design.ipynb` (graph search, topological ordering).
- Day 10: Add edge cases; sketch alternative approaches.
- Day 11: `advanced/02_experiments_evaluation.ipynb` (simulation, streaming, experiment design).
- Day 12: Build a mini project by remixing functions from prior notebooks.
- Day 13: Write a short blog-style recap of what you learned; re-run all tests.
- Day 14: Final review, tighten code, and document your personal heuristics.

Notebook conventions
--------------------
- Every notebook starts with a short overview and a setup cell that imports `utils.validation`.
- Tasks include structured TODOs; write your code below the prompt.
- A dedicated "Run tests" cell checks your work. Tests are intentionally small so you can add more cases as you learn.
- Feel free to duplicate a notebook (e.g., `01_python_basics_solutions.ipynb`) to preserve your first attempt.

Extending the curriculum
------------------------
- Add a new notebook following the naming convention `XX_topic.ipynb`.
- Reuse `utils.validation` or extend it with custom assertions.
- Consider pairing each new task with at least one design reflection: what was decomposed, what was abstracted away, and why.

Happy learning, and keep iterating until all validations are green!
