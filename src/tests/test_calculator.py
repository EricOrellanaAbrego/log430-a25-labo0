"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import pytest
from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

# TODO: ajoutez les tests

def test_addition():
    c = Calculator()
    assert c.addition(2, 3)

def test_subtraction():
    c = Calculator()
    assert c.subtraction(10, 4) == 6

def test_multiplication():
    c = Calculator()
    assert c.multiplication(7, 6) == 42

def test_division():
    c = Calculator()
    assert c.division(9, 2) == 4.5

def test_division_by_0():
    c = Calculator()
    assert c.division(9, 0) == "Erreur : division par zéro"

# Test qui échoue
def test_echec_addition():
    c = Calculator()
    assert c.addition(2, 2) == 5

