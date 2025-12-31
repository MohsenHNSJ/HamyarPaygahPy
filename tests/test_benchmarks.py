"""Benchmark tests for HamyarPaygahPy.

This module contains performance benchmarks using pytest-codspeed.
These benchmarks measure the performance of core functionality.
"""

import pytest


@pytest.mark.benchmark
def test_import_performance() -> None:
    """Benchmark the import performance of the main package."""
    import HamyarPaygahPy  # noqa: F401


@pytest.mark.benchmark
def test_module_attributes() -> None:
    """Benchmark accessing module attributes."""
    import HamyarPaygahPy

    _ = HamyarPaygahPy.__version__
    _ = HamyarPaygahPy.__title__
    _ = HamyarPaygahPy.__author__


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
    data = [i * 2 for i in range(1000)]
    _ = [x for x in data if x % 4 == 0]
