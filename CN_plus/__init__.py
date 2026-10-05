"""
CN_plus package initialization.
Ensures local package modules can be imported directly.
"""
import sys
import os

_pkg_dir = os.path.dirname(os.path.abspath(__file__))
if _pkg_dir not in sys.path:
    sys.path.insert(0, _pkg_dir)
