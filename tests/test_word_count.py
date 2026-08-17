import pytest
from word_count import word_count


def test_normal_sentence():
    assert word_count("hello world") == 2


def test_multiple_spaces():
    assert word_count("one  two   three") == 3


def test_tabs_and_newlines():
    assert word_count("one\ttwo\nthree") == 3


def test_mixed_whitespace():
    assert word_count("one  two\tthree\nfour") == 4


def test_empty_string():
    assert word_count("") == 0


def test_whitespace_only():
    assert word_count("   ") == 0


def test_whitespace_only_tabs_newlines():
    assert word_count("  \t\n  ") == 0


def test_single_word():
    assert word_count("hello") == 1


def test_leading_trailing_whitespace():
    assert word_count("  hello world  ") == 2
