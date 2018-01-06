QDG
===
> Diceware passphrases from quantum random data


Features
--------
- Simulates dice rolls by gathering quantum data.
- Includes the complete standard Diceware wordlist.
- Generate passphrases from custom wordlists.

*Python 3.6 or better is required.*


How to Install
--------------

Using pip

    $ pip3 install quantumdiceware
    
Building from source

    $ wget...
    $ python3 setup.py install


Basic Usage Examples
--------------------
Generate a Passphrase

    $ qdg

Generate five Passphrases and save them to output.txt

    $ qdg -c 5 > output.txt

Generate two Passphrases that are eight words long

    $ qdg -c 2 -w 8


Options
-------
By default, QDG will use quantum data to generate one passphrase consisting of six words.

[-c, --count]

[-w, --word]

[-f, --file]

[-l, --local]

[-v, -verbose]
Activates verbose mode. Dice rolls will be displayed along with the passphrase so they can easily be compared to the word list.

[--version]
Displays the version number and exits.