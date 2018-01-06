===
QDG
===
Diceware passphrases from quantum random data

.. image:: password_strength.png


Features
--------
- Simulates dice rolls by gathering quantum data.
- Includes the standard Diceware wordlist.
- Generate passphrases from custom wordlists.

Python 3.6 is required.


Usage
-----

Install

    $ pip install quantumdiceware

Generate a Passphrase

    $ qdg

Generate five Passphrases and save them to output.txt

    $ qdg -c 5 > output.txt

Generate two Passphrases that are eight words long

    $ qdg -c 2 -w 8


Documentation
-------------

For more in-line help, run:

    $ qdg -h

QDG's documentation lives at `qdg.readthedocs.io <http://qdg.readthedocs.io>`_

See `The Diceware Passphrase Home Page <http://world.std.com/~reinhold/diceware.html>`_ to learn more about Diceware.


Meta
----

Justin M. Sloan - `justinsloan.com <https://justinsloan.com>`_ - pydev@justinsloan.com

Public Domain. See ``LICENSE.txt`` for more information.

https://github.com/justinsloan/qdg