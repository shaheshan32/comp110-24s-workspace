"""Dictionary test from EX05."""

__author__ = "730396719"

import pytest

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_ucase_one() -> None:
    """Testing inverting with a list of three."""
    inp_dict = {'a': '1', 'b': '2', 'c': '3'}
    add_inp_dict = {'1': 'a', '2': 'b', '3': 'c'}
    assert invert(inp_dict) == add_inp_dict


def test_invert_ucase_two() -> None:
    """Testing inverting one item."""
    inp_dict = {'Florida': 'Miami'}
    add_inp_dict = {'Miami': 'Florida'}
    assert invert(inp_dict) == add_inp_dict


def test_invert_ecase_three() -> None:
    """Testing that same name wont work with the keyerror."""
    inp_dict = {'Steph': 'Curry', 'Seth': 'Curry'}    
    with pytest.raises(KeyError):
        invert(inp_dict)


def test_favorite_color_ucase_one() -> None:
    """Testing favorite colors normally."""
    inp_dict = {'Abby': 'carolina blue', 'Bella': 'crimson red', 'Charlie': 'carolina blue'}
    assert favorite_color(inp_dict) == 'carolina blue'


def test_favorite_color_ucase_two() -> None:
    """Testing only one color comes back."""
    inp_dict = {'Danny': 'forest green'}
    assert favorite_color(inp_dict) == 'forest green'


def test_favorite_color_ecase_three() -> None:
    """Testing favorite color tied with colors."""
    inp_dict = {'person1': 'red', 'person2': 'white', 'person3': 'blue'}
    assert favorite_color(inp_dict) == 'red'


def test_count_ucase_one() -> None:
    """Testing vote counting with a list of multiple NBA players."""
    inp_list = ['Lebron James', 'Micheal Jordan', 'Steph Curry', 'Lebron James', 'Micheal Jordan']
    exp_output = {'Lebron James': 2, 'Micheal Jordan': 2, 'Steph Curry': 1}
    assert count(inp_list) == exp_output


def test_count_ucase_two() -> None:
    """Testing vote counting with list of NBA players with same count."""
    inp_list = ['Kevin Durant', 'Devin Booker', 'Bradley Beal']
    exp_output = {'Kevin Durant': 1, 'Devin Booker': 1, 'Bradley Beal': 1}
    assert count(inp_list) == exp_output


def test_count_ecase_three() -> None:
    """Testing counting with an empty list."""
    inp_list = []
    exp_output = {}
    assert count(inp_list) == exp_output


def test_alphabetizer_ucase_one() -> None:
    """Test sorting with multiple NBA Players starting with different letters."""
    inp_list = ['doncic', 'tatum', 'brown', 'irving', 'lillard']
    exp_output = {'d': ['doncic'], 't': ['tatum'], 'b': ['brown'], 'i': ['irving'], 'l': ['lillard']}
    assert alphabetizer(inp_list) == exp_output


def test_alphabetizer_ucase_two() -> None:
    """Test sorting with NBA Players starting with a same letter."""
    inp_list = ['curry', 'cook', 'caldwell']
    exp_output = {'c': ['curry', 'cook', 'caldwell']}
    assert alphabetizer(inp_list) == exp_output


def test_alphabetizer_ecase_three() -> None:
    """Test sorting by alphabet with an empty list."""
    inp_list = []
    exp_output = {}
    assert alphabetizer(inp_list) == exp_output


def test_update_attendance_ucase_one() -> None:
    """Testing updating attendance for existing day."""
    attendance_log = {"Friday": ["Leonard", "George"], "Satuday": ["Green"]}
    day = "Satuday"
    student = "Thompson"
    update_attendance(attendance_log, day, student)
    assert attendance_log == {"Friday": ["Leonard", "George"], "Satuday": ["Green", "Thompson"]}


def test_update_attendance_ucase_two() -> None:
    """Testing updating attendance for a new day."""
    attendance_log = {"Monday": ["Jordan", "Rodman"], "Tuesday": ["Bird"]}
    day = "Wednesday"
    student = "Duncan"
    update_attendance(attendance_log, day, student)
    assert attendance_log == {"Monday": ["Jordan", "Rodman"], "Tuesday": ["Bird"], "Wednesday": ["Duncan"]}


def test_update_attendance_ecase_three() -> None:
    """Testing updating attendance for a day with an no list."""
    attendance_log = {}
    day = "Sunday"
    student = "Shah"
    update_attendance(attendance_log, day, student)
    assert attendance_log == {"Sunday": ["Shah"]}