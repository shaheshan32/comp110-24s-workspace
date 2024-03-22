"""Tests my mutating functions."""

from lessons.mutations.mutating_functions import remove_first, get_first, get_and_remove_first

def test_remove_first_use_case() -> None:
    """Test basic use case for remove_first function."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    remove_first(t)
    assert t == ["rainy", "sunny"]


def test_get_first_use_case() -> None:
    """Test basic use case for get_first function."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    ret_value: str = get_first(t)
    #Test it doesn't mutate
    assert t == ["cloudy", "rainy", "sunny"]
    assert ret_value == "cloudy"


def test_get_and_remove_first_use_case() -> None:
    """Test basic use case for get and remove first functions."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    ret_value: str = get_and_remove_first(t)
    assert t == ["rainy", "sunny"]
    assert ret_value == "cloudy"
