"""Unit tests for xml_utils module."""
# ruff: noqa: S101
# pylint: disable=I1101,W0621,R0903

import datetime
from enum import Enum

import pytest
from lxml import etree

from hamyar_paygah.utils.xml_utils import (
    get_bool,
    get_enum_from_boolean_flags,
    get_integer,
    get_text,
    get_time,
)


class TestEnum(Enum):
    """Test enum."""

    FIRST = "FirstFlag"
    SECOND = "SecondFlag"
    THIRD = "ThirdFlag"


@pytest.fixture
def xml_document() -> etree._Element:
    """Outputs a sample xml response."""
    xml = """
    <root xmlns:a="http://example.com/schema">
        <a:text_valid>hello</a:text_valid>
        <a:text_dash>-</a:text_dash>
        <a:text_hash>#</a:text_hash>
        <a:empty></a:empty>
        <a:integer_pure>42</a:integer_pure>
        <a:integer_mixed>abc123xyz</a:integer_mixed>
        <a:integer_zero>0</a:integer_zero>
        <a:true_lower>true</a:true_lower>
        <a:true_upper>TRUE</a:true_upper>
        <a:true_mixed>TrUe</a:true_mixed>
        <a:true_spaced>   true   </a:true_spaced>
        <a:false_value>false</a:false_value>
        <a:time_valid>12:30:45</a:time_valid>
        <a:time_spaced>   08:05:09   </a:time_spaced>
        <a:time_invalid_format>12-30-45</a:time_invalid_format>
        <a:time_invalid_value>25:99:99</a:time_invalid_value>
    </root>
    """
    return etree.fromstring(xml)


@pytest.fixture
def namespaces() -> dict[str, str]:
    """Outputs a sample namespace."""
    return {"a": "http://example.com/schema"}


@pytest.mark.parametrize(
    ("tag", "expected"),
    [
        ("text_valid", "hello"),  # normal case
        ("missing", None),  # element does not exist
        ("text_dash", None),  # "-"
        ("text_hash", None),  # "#"
        ("empty", None),  # element.text is None
    ],
)
def test_get_text(
    xml_document: etree._Element,
    namespaces: dict[str, str],
    tag: str,
    expected: str | None,
) -> None:
    """Tests the get_text function without custom prefix."""
    assert get_text(xml_document, tag, namespaces) == expected


def test_get_text_with_custom_prefix() -> None:
    """Tests the get_text function with custom prefix."""
    xml = """
    <root xmlns:b="http://example.com/schema">
        <b:valid>world</b:valid>
    </root>
    """
    document = etree.fromstring(xml)
    namespaces = {"b": "http://example.com/schema"}

    assert get_text(document, "valid", namespaces, prefix="b") == "world"


@pytest.mark.parametrize(
    ("tag", "expected"),
    [
        ("integer_pure", 42),  # direct int conversion
        ("integer_mixed", 123),  # regex fallback
        ("text_valid", None),  # no digits present
        ("empty", None),  # element.text is None
        ("missing", None),  # element does not exist
        ("integer_zero", 0),  # valid zero value
    ],
)
def test_get_integer(
    xml_document: etree._Element,
    namespaces: dict[str, str],
    tag: str,
    expected: int | None,
) -> None:
    """Tests the get_integer function."""
    assert get_integer(xml_document, tag, namespaces) == expected


@pytest.mark.parametrize(
    ("tag", "expected"),
    [
        ("true_lower", True),
        ("true_upper", True),
        ("true_mixed", True),
        ("true_spaced", True),
        ("false_value", False),
        ("integer_pure", False),
        ("text_valid", False),
        ("empty", False),  # element.text is None
        ("missing", False),  # element does not exist
    ],
)
def test_get_bool(
    xml_document: etree._Element,
    namespaces: dict[str, str],
    tag: str,
    *,
    expected: bool,
) -> None:
    """Tests the get_bool function."""
    assert get_bool(xml_document, tag, namespaces) is expected


@pytest.mark.parametrize(
    ("tag", "expected"),
    [
        ("time_valid", datetime.time(12, 30, 45)),
        ("time_spaced", datetime.time(8, 5, 9)),
        ("time_invalid_format", None),
        ("time_invalid_value", None),
        ("empty", None),
        ("missing", None),
    ],
)
def test_get_time(
    xml_document: etree._Element,
    namespaces: dict[str, str],
    tag: str,
    expected: datetime.time | None,
) -> None:
    """Tests the get_time function."""
    assert get_time(xml_document, tag, namespaces) == expected


@pytest.mark.parametrize(
    ("xml", "expected"),
    [
        # No flags set
        (
            """
            <root xmlns:a="http://example.com/schema"></root>
            """,
            None,
        ),
        # Single true flag
        (
            """
            <root xmlns:a="http://example.com/schema">
                <a:FirstFlag>true</a:FirstFlag>
            </root>
            """,
            TestEnum.FIRST,
        ),
        # Multiple flags true → last enum member wins (THIRD)
        (
            """
            <root xmlns:a="http://example.com/schema">
                <a:FirstFlag>true</a:FirstFlag>
                <a:ThirdFlag>true</a:ThirdFlag>
            </root>
            """,
            TestEnum.THIRD,
        ),
        # Explicit false values ignored
        (
            """
            <root xmlns:a="http://example.com/schema">
                <a:FirstFlag>false</a:FirstFlag>
                <a:SecondFlag>true</a:SecondFlag>
            </root>
            """,
            TestEnum.SECOND,
        ),
        # All false → None
        (
            """
            <root xmlns:a="http://example.com/schema">
                <a:FirstFlag>false</a:FirstFlag>
                <a:SecondFlag>false</a:SecondFlag>
            </root>
            """,
            None,
        ),
    ],
)
def test_get_enum_from_boolean_flags(
    xml: str,
    expected: TestEnum | None,
    namespaces: dict[str, str],
) -> None:
    """Tests the get_enum_from_boolean_flags function."""
    document = etree.fromstring(xml)
    result = get_enum_from_boolean_flags(document, namespaces, TestEnum)
    assert result == expected
