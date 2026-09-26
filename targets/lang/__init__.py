"""Stand-in for the shared lang/ package when a target script puts targets/ on sys.path.

Target scripts reach the shared models with `sys.path.insert(0, '..'); from lang import lm` (and a dozen variants).
Since the targets moved into targets/, '..' is targets/ itself, so this package forwards `lang.*` to the real package.
"""
import os
__path__ = [os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'lang')]
