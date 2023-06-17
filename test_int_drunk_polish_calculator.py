import sys
import pytest
from drunk_polish_calculator import main

def test_integration(monkeypatch, capsys):
    input_string = '2 7 +'
    expected_output = '9.0\n'

    # Patch the input function to return the input string
    monkeypatch.setattr('builtins.input', lambda _: input_string)

    # Call the main function

    main()

    # Capture the output
    captured = capsys.readouterr()
    captured_output = captured.out

    # Assert the output
    assert captured_output == expected_output
