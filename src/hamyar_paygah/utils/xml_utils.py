"""Utility functions relate to XML."""

# pylint: disable=I1101
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
