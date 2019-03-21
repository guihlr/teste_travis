import pytest
from main import soma
from main import multi

def test_soma():
  assert soma(6, 4) == 10

def test_multi():
  assert multi(2, 4) == 8