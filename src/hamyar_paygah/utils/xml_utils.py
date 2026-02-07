"""Utility functions relate to XML."""

# pylint: disable=I1101
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
    # If element has data, return it's text, else return none
    return element.text if element is not None else None


# E is some kind of Enum, and the return type matches the input enum
def get_enum_from_boolean_flags[E: Enum](
    document: etree._Element,
    namespaces: dict[str, str],
    enum_type: type[E],
) -> E | None:
    """Retrieve a single enum value from boolean SOAP flags.

    Iterates over the provided enum and returns the member whose
    corresponding XML tag value is 'true'.

    Returns None if no matching value is found.

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
