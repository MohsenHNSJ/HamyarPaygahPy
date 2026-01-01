"""Benchmark tests for HamyarPaygahPy.

This module contains performance benchmarks using pytest-codspeed.
These benchmarks measure the performance of core functionality.
"""

import pytest


@pytest.mark.benchmark
def test_string_operations() -> None:
    """Benchmark basic string operations.

    This is a placeholder benchmark that demonstrates the setup.
    Real benchmarks should be added as the codebase grows.
    """
    text = "HamyarPaygahPy " * 100
    _ = text.upper()
    _ = text.lower()
    _ = text.split()


@pytest.mark.benchmark
def test_list_comprehension() -> None:
    """Benchmark list comprehension performance.

    This is a placeholder benchmark that demonstrates the setup.
    Real benchmarks should be added as the codebase grows.
    """
    data: list[int] = [i * 2 for i in range(1000)]
    _: list[int] = [x for x in data if x % 4 == 0]
