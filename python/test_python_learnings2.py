import pytest

'''
1. Parametrization (@pytest.mark.parametrize)
Instead of writing similar tests over and over (like test_acircle asserting 3 different values), you can write one test function and pass it a list of inputs and expected outputs. This reduces code duplication significantly.

2. Monkeypatching (monkeypatch fixture)
This is crucial for testing interactive programs like yours. monkeypatch allows you to temporarily replace a function or attribute during a test.

Use Case: Your add_up() function uses input(), which usually stops the program and waits for a user. You can use monkeypatch to "fake" the user typing numbers so the test runs automatically.
3. Exception Testing (pytest.raises)
Sometimes you want to ensure your function fails correctly (e.g., if a user passes a string instead of a number). You can verify that a specific error is raised.

4. Markers (@pytest.mark)
As your test suite grows, you might want to group tests. You can "tag" tests (e.g., @pytest.mark.slow, @pytest.mark.smoke) and run only those specific groups using the command line (e.g., pytest -m smoke).
5. Fixtures (@pytest.fixture)
Fixtures are a powerful way to set up and tear down test environments. If you have complex data structures (like your list of states and populations), you can create a fixture that initializes this data once and then use it across multiple tests. This keeps your test code clean and DRY (Don't Repeat Yourself).
'''
#pytest test_python_learnings2.py -v -m smoke (run only tests marked as smoke)
#pytest test_python_learnings2.py -v -m "not smoke" (run all tests except those marked as smoke)
#pytest test_python_learnings2.py -v -m "not smoke or slow" (run all tests except those marked as smoke or slow)
#pytest test_python_learnings2.py -v -k "population"  # Run only tests with "population" in their name

from python_learnings2 import (
    acircle,
    f_to_c,
    c_to_f,
    average,
    who_is_there,
    count_a,
    area,
    absv,
    population,
    add_up,
)

@pytest.mark.smoke
def test_acircle():
    # Test circle area calculation: 3.14 * r * 2
    # Note: The formula in source is 3.14*r*2 (Circumference-ish?) vs pi*r^2.
    # Testing based on the actual implementation in the file.
    assert abs(acircle(1) - 6.28) < 0.001
    assert abs(acircle(10) - 62.80) < 0.001
    assert acircle(0) == 0

@pytest.mark.smoke
def test_f_to_c():
    # Formula: 5*(t-32)/9
    assert f_to_c(32) == 0
    assert abs(f_to_c(212) - 100) < 0.001
    assert abs(f_to_c(-40) - -40) < 0.001

def test_c_to_f():
    # Formula: ((t*9)/5)+32
    assert c_to_f(0) == 32
    assert abs(c_to_f(100) - 212) < 0.001
    assert abs(c_to_f(-40) - -40) < 0.001

def test_average(capsys):
    # The average function prints the result rather than returning it
    test_list = [10, 20, 30]
    average(test_list)
    captured = capsys.readouterr()
    assert "The average is 20.0" in captured.out

    test_list_2 = [0, 10]
    average(test_list_2)
    captured = capsys.readouterr()
    assert "The average is 5.0" in captured.out

def test_who_is_there(capsys):
    # Test presence of animals
    who_is_there(['bear', 'donkey'])
    captured = capsys.readouterr()
    assert "There's a bear." in captured.out
    assert "There is a donkey." in captured.out
    assert "There is no horse in the list." in captured.out

def test_count_a(capsys):
    lis = ["a", "b", "a", "c"]
    count_a(lis)
    captured = capsys.readouterr()
    assert "There are 2 letter a's in the list." in captured.out

def test_area(capsys):
    # Test square calculation
    area("square", 4)
    captured = capsys.readouterr()
    assert "Area of square: 16" in captured.out

    # Test unknown shape
    area("unknown", 10)
    captured = capsys.readouterr()
    assert "Not sure" in captured.out

def test_absv(capsys):
    absv(-5)
    captured = capsys.readouterr()
    # Note: The source function uses comma separation in print, so %d is not replaced but printed literally.
    # Expected output: "absv of %d is %d -5 5"
    assert "absv of %d is %d -5 5" in captured.out

# -------------------------------------------------------------------------
# Handling Complex Data Structures and Initialization
# -------------------------------------------------------------------------

# Approach 1: Use a Fixture.
# This is best when the same complex data is needed for multiple tests.
@pytest.fixture
def state_data_fixture():
    # Initialize complex list of lists
    return [
        ["Massachusetts", 6692824],
        ["Connecticut", 3596080],
        ["Maine", 1328302]
    ]

def test_population_with_fixture(capsys, state_data_fixture):
    # Pass the fixture name as an argument to the test function
    population(state_data_fixture)

    '''
    capsys is a built-in pytest fixture that automatically captures everything your code prints to the console (Standard Output) or logs as errors (Standard Error).
    .readouterr() is a method that:
    Retrieves the text that has been captured so far.
    Resets the capture buffer (clears it) so the next test starts fresh.
    captured becomes an object containing two strings:
    captured.out: The text printed to standard output (e.g., via print()).
    captured.err: The text printed to standard error.
    '''
    captured = capsys.readouterr()
    # Expected sum: 6692824 + 3596080 + 1328302 = 11617206
    assert "The total population of this list of states is 11617206" in captured.out

def test_population_inline_init(capsys):
    # Approach 2: Initialize directly inside the test (good for unique, specific edge cases)
    custom_data = [["SmallState", 100], ["BigState", 1000]]
    population(custom_data)
    captured = capsys.readouterr()
    assert "The total population of this list of states is 1100" in captured.out

# -------------------------------------------------------------------------
# Feature 1: Parametrization
# Run the same test logic with multiple sets of inputs/outputs
# -------------------------------------------------------------------------
@pytest.mark.parametrize("shape, size, expected_msg", [
    ("circle", 3, "Area  of circle: 18.84"),  # 3.14 * 3 * 2
    ("square", 4, "Area of square: 16"),     # 4 * 4
    ("rect", 5, "Not sure"),                 # Unknown shape
])
def test_area_parametrized(capsys, shape, size, expected_msg):
    area(shape, size)
    captured = capsys.readouterr()
    assert expected_msg in captured.out

# -------------------------------------------------------------------------
# Feature 2: Monkeypatching (Simulating User Input)
# -------------------------------------------------------------------------
def test_add_up_input(capsys, monkeypatch):
    # The add_up function calls input() in a loop until 0 is entered.
    # We create an iterator that yields '5', '10', and then '0'.
    inputs = iter(["5", "10", "0"])
    
    # We replace (monkeypatch) the built-in 'input' function.
    # Whenever add_up calls input(), it gets the next value from our list.
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    
    add_up()
    
    captured = capsys.readouterr()
    # 5 + 10 + 0 = 15
    # We look for the final print statement
    assert "15" in captured.out