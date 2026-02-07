"""Utility functions relate to XML."""

# pylint: disable=I1101
import datetime
import re
from enum import Enum

from lxml import etree


def get_text(document: etree._Element, tag: str, namespaces: dict[str, str]) -> str | None:
    """Retrieve the text content of a child element by tag.

    Args:
        document (_Element): The parent XML element containing the tag.
        tag (str): The tag name of the child element (without namespace prefix).
        namespaces (dict[str, str]): Namespace mapping for XPath.

    Returns:
        str | None: The text content of the element, or None if not present.
    """
    element: etree._Element | None = document.find(
        path=f"a:{tag}",
        namespaces=namespaces,
    )
    # If element has data, check the data
    if element is not None:
        # If it's invalid, return None
        if element.text == "-":
            return None
        # Else, return data
        return element.text
    # Else, return None
    return None


def get_integer(document: etree._Element, tag: str, namespaces: dict[str, str]) -> int | None:
    """Retrieves the integer content of a child element by tag.

    Args:
        document (etree._Element): The parent XML element containing the tag.
        tag (str): The tag name of the child element (without namespace prefix).
        namespaces (dict[str, str]): Namespace mapping for XPath.

    Returns:
        int | None: The integer value if content is not None, otherwise None.
    """
    result: int | None = None

    # Get the text content
    text: str | None = get_text(document, tag, namespaces)

    # If input is empty, return None
    if not text:
        return result

    # Try to extract the number regularly
    try:
        result = int(text)
    # If the input is a mix of numbers and alphabets, extract numbers
    except ValueError:
        match = re.search(r"\d+", text)
        result = int(match.group()) if match else None

    return result


def get_bool(document: etree._Element, tag: str, namespaces: dict[str, str]) -> bool:
    """Retrieves the boolean content of a child element by tag.

    Args:
        document (etree._Element): The parent XML element containing the tag.
        tag (str): The tag name of the child element (without namespace prefix).
        namespaces (dict[str, str]): Namespace mapping for XPath.

    Returns:
        bool: The boolean value if content is not None, otherwise False.
    """
    # Get the text content
    text: str | None = get_text(document, tag, namespaces)
    # Check if the content is true and return the result
    return text == "true"


def get_time(
    document: etree._Element,
    tag: str,
    namespaces: dict[str, str],
) -> datetime.time | None:
    """Retrieves the time content of a child element by tag.

    Args:
        document (etree._Element): The parent XML element containing the tag.
        tag (str): The tag name of the child element (without namespace prefix).
        namespaces (dict[str, str]): Namespace mapping for XPath.

    Returns:
        datetime.time | None: The time value if content is not None, otherwise None.
    """
    # Get the text content
    text: str | None = get_text(document, tag, namespaces)
    # If time is not provided by server, return None
    if text == "-" or text is None:
        return None
    # Else, convert the string to time
    return datetime.datetime.strptime(text, "%H:%M:%S").time()  # noqa: DTZ007


def get_enum_from_boolean_flags[E: Enum](
    document: etree._Element,
    namespaces: dict[str, str],
    enum_type: type[E],
) -> E | None:
    """Retrieve a single enum value from boolean SOAP flags.

    Iterates over the provided enum and returns the member whose
    corresponding XML tag value is 'true'.

    Returns None if no matching value is found.

    E is some kind of Enum, and the return type matches the input enum

    Args:
        document (etree._Element): XML SOAP response.
        namespaces (dict[str, str]): SOAP namespaces.
        enum_type (type[E]): Enum type to extract.

    Raises:
        ValueError: If multiple True values are found.

    Returns:
        E | None: Extracted enum value or None.
    """
    result: E | None = None
    # Iterate through the Enum to find the result
    for member in enum_type:
        value = get_text(document, member.value, namespaces)

        # if it's the correct value, save it
        if value is not None and value.lower() == "true":
            # If we already have a result, show error
            if result is not None:
                print("Multiple choices detected!")
                raise ValueError
            result = member

    return result
