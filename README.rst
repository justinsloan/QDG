QDG
===
> Diceware passphrases from quantum random data

.. image:: https://api.travis-ci.org/dbader/schedule.svg?branch=master
        :target: https://travis-ci.org/dbader/schedule

.. image:: https://coveralls.io/repos/dbader/schedule/badge.svg?branch=master
        :target: https://coveralls.io/r/dbader/schedule

.. image:: https://img.shields.io/pypi/v/schedule.svg
        :target: https://pypi.python.org/pypi/schedule

An in-process scheduler for periodic jobs that uses the builder pattern
for configuration. Schedule lets you run Python functions (or any other
callable) periodically at pre-determined intervals using a simple,
human-friendly syntax.

Features
--------
- Simulates dice rolls by gathering quantum data.
- Includes the standard Diceware wordlist.

Usage
-----

Install

    $ pip install quantumdiceware

Usage

    $ qdg
    $ qdg -c 5 > output.txt

Documentation
-------------

Schedule's documentation lives at `schedule.readthedocs.io <https://schedule.readthedocs.io/>`_.

Please also check the FAQ there with common questions.


Meta
----

Justin M. Sloan - `@dbader_org <https://twitter.com/dbader_org>`_ - justin@justinsloan.com

Public Domain. See ``LICENSE.txt`` for more information.

https://github.com/justinsloan/qdg