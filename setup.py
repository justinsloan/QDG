"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('quantumdiceware/quantumdiceware.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "quantumdiceware",
    packages = ["quantumdiceware"],
    entry_points = {
        "console_scripts": ['qdg = quantumdiceware.quantumdiceware:main']
        },
    version = version,
    description = "Generates Diceware passphrases using quantum random data.",
    long_description = long_descr,
    author = "Justin M. Sloan",
    author_email = "justin@justinsloan.com",
    url = "http://github.com/justinsloan/qdg",
    )
