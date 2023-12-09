import sys
sys.path.append('D:/python/python_project_Data visualization')

from die.die import Die

def test_default_die_sides():
    die = Die()
    assert die.num_sides == 6

def test_custom_die_sides():
    die = Die(num_sides=10)
    assert die.num_sides == 10

def test_roll_within_range():
    die = Die(num_sides=8)
    result = die.roll()
    assert 1 <= result <= 8

def test_roll_is_integer():
    die = Die()
    result = die.roll()
    assert isinstance(result, int)
