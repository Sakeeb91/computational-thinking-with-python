"""
Lightweight validation helpers for the notebooks.

Usage inside a notebook:

    from utils.validation import check_equal, check_true, summary, reset
    reset()
    check_equal("example", my_func(2), 4)
    summary()
"""

_results = {"passed": 0, "failed": 0}


def reset() -> None:
    """Reset counters so each run gives a clean summary."""
    _results["passed"] = 0
    _results["failed"] = 0


def _record(ok: bool) -> None:
    key = "passed" if ok else "failed"
    _results[key] += 1


def check_equal(name: str, actual, expected, hint: str = "") -> None:
    """Assert that actual == expected and record the result."""
    if actual == expected:
        _record(True)
        print(f"[PASS] {name}")
    else:
        _record(False)
        msg = f"[FAIL] {name}: expected {expected!r}, got {actual!r}"
        if hint:
            msg += f" | Hint: {hint}"
        raise AssertionError(msg)


def check_true(name: str, condition: bool, hint: str = "") -> None:
    """Assert that a boolean condition is true."""
    if condition:
        _record(True)
        print(f"[PASS] {name}")
    else:
        _record(False)
        msg = f"[FAIL] {name}: condition is false"
        if hint:
            msg += f" | Hint: {hint}"
        raise AssertionError(msg)


def summary() -> None:
    """Print a short test summary and raise if any failures occurred."""
    total = _results["passed"] + _results["failed"]
    if _results["failed"] == 0:
        print(f"All {total} tests passed. Keep going!")
    else:
        fail = _results['failed']
        passed = _results['passed']
        raise AssertionError(f"{fail} of {total} tests failed (passed: {passed}). Fix code and retry.")
