Computational Thinking with Python
==================================

This repository is a two-week, notebook-driven curriculum to practice computational thinking with Python. The path is divided into beginner, intermediate, and advanced tracks, each with clear tasks and validation tests inside the notebooks so learners get immediate feedback.

🚀 Launch in the Cloud (No Installation Required!)
--------------------------------------------------

The fastest way to start learning - click and code in your browser with zero setup:

### Option 1: Binder (Recommended for Quick Start)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Sakeeb91/computational-thinking-with-python/HEAD?urlpath=lab/tree/notebooks/beginner/01_python_basics.ipynb)

Click the badge above to launch an interactive Jupyter environment.

**What to expect:**
- First launch takes 2-3 minutes to build the environment (subsequent launches are faster)
- Everything runs in your browser - no installation needed
- All notebooks and validation tests work perfectly
- ⚠️ **Important:** Your work is NOT saved automatically. Download notebooks before closing!

**Individual notebook launches:**

| Module | Notebook | Launch |
|--------|----------|--------|
| Beginner | 01 - Python Basics | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Sakeeb91/computational-thinking-with-python/HEAD?urlpath=lab/tree/notebooks/beginner/01_python_basics.ipynb) |
| Beginner | 02 - Decomposition & Control Flow | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Sakeeb91/computational-thinking-with-python/HEAD?urlpath=lab/tree/notebooks/beginner/02_decomposition_control.ipynb) |
| Intermediate | 01 - Data Structures & Complexity | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Sakeeb91/computational-thinking-with-python/HEAD?urlpath=lab/tree/notebooks/intermediate/01_data_structures_complexity.ipynb) |
| Intermediate | 02 - Recursion & Search | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Sakeeb91/computational-thinking-with-python/HEAD?urlpath=lab/tree/notebooks/intermediate/02_recursion_search.ipynb) |
| Advanced | 01 - Algorithm Design & Graphs | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Sakeeb91/computational-thinking-with-python/HEAD?urlpath=lab/tree/notebooks/advanced/01_algorithm_design.ipynb) |
| Advanced | 02 - Experiments & Evaluation | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Sakeeb91/computational-thinking-with-python/HEAD?urlpath=lab/tree/notebooks/advanced/02_experiments_evaluation.ipynb) |

### Option 2: Google Colab (For Saving Your Progress)

If you need to save your work across multiple sessions, use Google Colab (requires a free Google account):

1. Go to [Google Colab](https://colab.research.google.com/)
2. Click **File → Open Notebook → GitHub tab**
3. Enter repository: `Sakeeb91/computational-thinking-with-python`
4. Select a notebook to open
5. **Important:** Add this setup cell at the top and run it first:

```python
# Run this cell first to set up the environment
!git clone https://github.com/Sakeeb91/computational-thinking-with-python.git
import sys
sys.path.append('/content/computational-thinking-with-python')
```

6. Now you can run the rest of the notebook normally
7. Your work automatically saves to Google Drive

Quick start (Local Installation)
---------------------------------
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
- **NEW:** Each task now has its own code cell and test cell, giving you immediate feedback after completing each accomplishment!
  - Task 1 → Code → Test → Task 2 → Code → Test → Task 3 → Code → Test
  - This progressive structure helps you build confidence step-by-step
  - You can see your progress clearly (1 of 3 done, 2 of 3 done, etc.)
- Tests are intentionally small so you can add more cases as you learn.
- Feel free to duplicate a notebook (e.g., `01_python_basics_solutions.ipynb`) to preserve your first attempt.

Extending the curriculum
------------------------
- Add a new notebook following the naming convention `XX_topic.ipynb`.
- Reuse `utils.validation` or extend it with custom assertions.
- Consider pairing each new task with at least one design reflection: what was decomposed, what was abstracted away, and why.

Happy learning, and keep iterating until all validations are green!
