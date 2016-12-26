from __future__ import absolute_import

from nose.tools import assert_equal
from ..mymodule import myfunction, myfunction2

def test_my_function():
    """ Tests my function """
    assert_equal(myfunction(), 0)

def test_my_function2():
    """ Tests my second function """
    assert_equal(myfunction2(), 0)
