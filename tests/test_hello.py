# -*- coding: utf-8 -*-
"""
    tests.hello
    ~~~~~~~~~~~~~~~~~~~~~
    Test that the hihylang package says hello.
"""
import pytest
from hihylang.hi import hello

def test_hello(capsys):
	hello()
	captured = capsys.readouterr()
	assert captured.out == "Hi Hy!\n"
