"""Dictionary EX05."""

__author__ = "730396719"


def invert(names: dict[str, str]) -> dict[str, str]:
    """Invert function."""
    inv_dict: dict[str, str] = {}
    for key, value in names.items():
        if value in inv_dict:
            raise KeyError("Duplicates not allowed!")
        inv_dict[value] = key
    return inv_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Favorite color most popular or if tie repeated first."""
    color_counts: dict[str, int] = {}
    for color in dictionary.values():
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    most_color = ""
    max_counts = 0
    for color, count in color_counts.items():
        if count > max_counts:
            most_color = color
            max_counts = count
    return most_color


def count(vals: list[str]) -> dict[str, int]:
    """Counts number of times the value appears in input list."""
    freq: dict[str, int] = {}
    for item in vals:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


def alphabetizer(vals: list[str]) -> dict[str, list[str]]:
    """Sorts based on first letter."""
    sorted_words: dict[str, list[str]] = {}
    for word in vals:
        f_letter = word[0].lower()
        if f_letter in sorted_words:
            sorted_words[f_letter].append(word)
        else:
            sorted_words[f_letter] = [word]
    return sorted_words


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Updated logged attendance."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]