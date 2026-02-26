"""Utility functions relate to XML."""

# pylint: disable=I1101
import datetime
import re
from enum import Enum
from typing import TypeVar

from lxml import etree

# E is some kind of Enum, and the return type matches the input enum
E = TypeVar("E", bound=Enum)


def get_text(
    document: etree._Element,
    tag: str,
    namespaces: dict[str, str],
    prefix: str = "a",
) -> str | None:
    """Return the text content of a direct child element.

    Args:
        document: Parent XML element containing the child.
        tag: Child element tag name (without namespace prefix).
        namespaces: Mapping of namespace prefixes to URIs.
        prefix: Namespace prefix used in lookup. Defaults to "a".

    Returns:
        str | None:
            The element text if found and valid. Returns None if
            - The element does not exist.
            - The element text is None.
            - The element text is "-" or "#".
    """
    element: etree._Element | None = document.find(
        path=f"{prefix}:{tag}",
        namespaces=namespaces,
    )

    if element is None:
        return None

    text: str | None = element.text
    # If the text is invalid, return None
    if text in {"-", "#"}:
        return None

    return text


def get_integer(document: etree._Element, tag: str, namespaces: dict[str, str]) -> int | None:
    """Return the integer value of a child element's text content.

    The function retrieves the element text using ``get_text`` and attempts
    to convert it to an integer. If direct conversion fails, it extracts the
    first integer sequence found in the text.

    Args:
        document: Parent XML element containing the child.
        tag: Child element tag name (without namespace prefix).
        namespaces: Mapping of namespace prefixes to URIs.

    Returns:
        int | None:
            The parsed integer if found. Returns `None` if
            - The element does not exist.
            - The element text is None or empty.
            - No integer value can be extracted.
    """
    # Get the text content
    text: str | None = get_text(document, tag, namespaces)

    if text is None:
        return None

    # Strip whitespace
    text = text.strip()

    # If input is empty, return None
    if not text:
        return None

    # Try to extract the number regularly
    try:
        return int(text)
    # If the input is a mix of numbers and alphabets, extract numbers
    except ValueError:
        match = re.search(r"\d+", text)
        return int(match.group()) if match else None


def get_bool(document: etree._Element, tag: str, namespaces: dict[str, str]) -> bool:
    """Return the boolean value of a child element's text content.

    The function retrieves the element text using ``get_text`` and returns
    True only if the text is exactly "true" (case-insensitive).
    All other values, including missing or empty elements, return False.

    Args:
        document: Parent XML element containing the child.
        tag: Child element tag name (without namespace prefix).
        namespaces: Mapping of namespace prefixes to URIs.

    Returns:
        bool:
            True if the element text equals "true" (case-insensitive).
            Otherwise, False.
    """
    # Get the text content
    text: str | None = get_text(document, tag, namespaces)
    return text is not None and text.strip().lower() == "true"


def get_time(
    document: etree._Element,
    tag: str,
    namespaces: dict[str, str],
) -> datetime.time | None:
    """Return the time value of a child element's text content.

    The function retrieves the element text using ``get_text`` and attempts
    to parse it using the format "%H:%M:%S".

    Args:
        document: Parent XML element containing the child.
        tag: Child element tag name (without namespace prefix).
        namespaces: Mapping of namespace prefixes to URIs.

    Returns:
        datetime.time:
            A ``datetime.time`` object if parsing succeeds.
            Returns `None` if:
            - The element does not exist.
            - The element text is None.
            - The text does not match the "%H:%M:%S" format.
    """
    # Get the text content
    text: str | None = get_text(document, tag, namespaces)
    # If time is not provided by server, return None
    if text is None:
        return None

    # Strip whitespace
    text = text.strip()
    if not text:
        return None

    # Else, convert the string to time
    try:
        return datetime.datetime.strptime(text, "%H:%M:%S").time()  # noqa: DTZ007
    except ValueError:
        return None


def get_enum_from_boolean_flags(  # noqa: UP047
    document: etree._Element,
    namespaces: dict[str, str],
    enum_type: type[E],
) -> E | None:
    """Extract an enum member from boolean SOAP flag elements.

    Iterates over all members of ``enum_type`` and evaluates the XML
    element whose tag name matches ``member.value`` using ``get_bool()``.

    If one or more flags evaluate to ``True``, the last matching enum
    member in iteration order is returned. If no flags evaluate to
    ``True``, ``None`` is returned.

    This function assumes that each enum member's value corresponds
    to the XML tag name of a boolean flag element.

    Args:
        document: XML SOAP response element.
        namespaces: Namespace mapping used for XPath lookups.
        enum_type: Enum type whose members map to boolean flag tags.

    Returns:
        E | None:
            The matching enum member, or ``None`` if no flag is set.
    """
    result: E | None = None
    # Iterate through the Enum to find the result
    for member in enum_type:
        if get_bool(document, member.value, namespaces):
            # if it's the correct value, save it
            result = member

    return result
