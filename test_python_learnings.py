import io
import sys

from python_learnings import fib

def test_fib_output(capsys=None):
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    fib(10)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    # The Fibonacci numbers less than 10 are: 0 1 1 2 3 5 8
    assert output.strip() == "0 1 1 2 3 5 8"

def test_fib_zero(capsys=None):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    fib(0)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output.strip() == ""

def test_fib_one(capsys=None):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    fib(1)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output.strip() == "0"

# We recommend installing an extension to run python tests.