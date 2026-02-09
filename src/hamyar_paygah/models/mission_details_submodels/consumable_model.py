"""Consumable used sub-model for Mission details model."""

from collections import Counter
from dataclasses import dataclass


@dataclass(slots=True)
class ConsumablesUsed:
    """Consumable medical items used during the mission."""

    items: Counter[str]
    """Mapping of consumable item name to quantity used."""
