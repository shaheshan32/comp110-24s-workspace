"""Test my garden functions."""

__author__ = "730396719"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_ecase_empty_kind() -> None:
    """Test adding a plant to an empty kind."""
    by_kind = {}
    add_by_kind(by_kind, "fruit", "strawberry")
    assert by_kind == {"fruit": ["strawberry"]}


def test_add_by_kind_ucase_existing_kind() -> None:
    """Test adding a plant to an existing kind."""
    by_kind = {"vegetable": ["tomato", "broccoli"], "flower": ["lily"]}
    add_by_kind(by_kind, "vegetable", "lettuce")
    assert by_kind == {"vegetable": ["tomato", "broccoli", "lettuce"], "flower": ["lily"]}


def test_add_by_date_ecase_existing_month() -> None:
    """Test adding a plant to an existing month."""
    by_date = {"March": ["tulip"], "September": ["cucumber"]}
    add_by_date(by_date, "March", "daisy")
    assert by_date == {"March": ["tulip", "daisy"], "September": ["cucumber"]}


def test_add_by_date_ucase_new_month() -> None:
    """Test adding a plant to a new month."""
    by_date = {"March": ["tulip"], "September": ["cucumber"]}
    add_by_date(by_date, "May", "rose")
    assert by_date == {"March": ["tulip"], "September": ["cucumber"], "May": ["rose"]} 


def test_lookup_by_kind_and_date_ecase_found() -> None:
    """Test looking up plants by kind and date when plants are found."""
    # Modified data: No flowers are planted in June
    plants_by_kind = {"vegetable": ["tomato", "broccoli"], "flower": ["lily", "tulip"]}
    plants_by_date = {"April": ["tulip", "tomato"], "June": ["tomato"]}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "June")
    assert result == "No flowers to plant in June."


def test_lookup_by_kind_and_date_ucase_found() -> None:
    """Test looking up plants by kind and date when plants are found."""
    plants_by_kind = {"vegetable": ["tomato", "broccoli"], "flower": ["lily", "tulip"]}
    plants_by_date = {"April": ["tulip", "tomato"], "June": ["broccoli"]}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "April")
    assert result == "flowers to plant in April: ['tulip']" 