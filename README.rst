===
QDG
===
Diceware passphrases from quantum random data

.. image:: password_strength.png

Features
--------
- Simulates dice rolls by gathering quantum data.
- Includes the standard Diceware wordlist.

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

For more help, run:

    $ qdg -h

See `The Diceware Passphrase Home Page <http://world.std.com/~reinhold/diceware.html>`_ to learn more about Diceware.



Meta
----

Justin M. Sloan - `justinsloan.com <https://justinsloan.com>`_ - pydev@justinsloan.com

Public Domain. See ``LICENSE.txt`` for more information.

https://github.com/justinsloan/qdg