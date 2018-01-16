QDG
===
Diceware passphrases from quantum random data

QDG is free and unencumbered software released into the Public Domain. For more information on the Public Domain visit `Unlicense.org`_.


Features
--------
- Simulates dice rolls by gathering quantum data.
- Includes the standard Diceware Complete wordlist consisting of 7776 short words, abbreviations and easy-to-remember character strings.
- Generate passphrases from custom wordlists.
- Customize passphrase output with selectable length.

*Python 3.6 or better is required.*


How to Install
--------------

Using pip

.. code:: sh

    $ pip install quantumdiceware

Building from source

.. code:: sh

    $ wget --no-check-certificate --content-disposition https://github.com/justinsloan/QDG/archive/master.zip
    $ unzip -a master.zip
    $ cd ./QDG-master
    $ python3 setup.py install


Basic Usage Examples
--------------------
Generate a Passphrase

.. code:: sh

    $ qdg

Generate five Passphrases and save them to output.txt

.. code:: sh

    $ qdg -c 5 > output.txt

Generate two Passphrases that are eight words long

.. code:: sh

    $ qdg -c 2 -w 8


Options
-------
By default, QDG will use quantum data to generate one passphrase consisting of six words selected from the Diceware Complete list. The default behavior requires an internet connection for gathering quantum data.

**[-c, --count]**
    Specify the number of passphrases to generate. By default, QDG will only generate one (1) passphrase each time it is run.

**[-w, --word]**
    Specify the length of the passphrase to generate. By default, QDG will generate passphrases with a length of six (6) words. The '--word' option allows you to specify any number of words you prefer. This option will apply to all passphrases generated when used with the '--count' option.

**[-f, --file]**
    Specify a custom wordlist file. Custom wordlist files should be in plain text format with one dice roll per line. There are many alternate and foreign language wordlists available on the official `Diceware`_ website.

.. code:: sh

    $ qdg --file ./alt_wordlist.txt

**[-l, --local]**
    Use locally obtained random data. This is useful if there is no internet connection available or if local data is preferred.

**[-v, -verbose]**
    Activates verbose mode. Dice rolls will be displayed along with the passphrase so they can easily be compared to the wordlist.

.. code:: sh

    $ qdg -l -v
    Using local random data...
    Dice Rolls: 54642
    Dice Rolls: 14415
    Dice Rolls: 35165
    Dice Rolls: 51352
    Dice Rolls: 55552
    Dice Rolls: 52242
    soma blown karen rasa stoop rondo

**[--char]**
    Specify the character that is placed between words in the passphrase. A space character is used by default, but just about any character or arbitrary text of any length may be used.

.. code:: sh

    $qdg --char -
    vend-grist-hobby-mark-enamel-job
    $qdg --char ""
    vendgristhobbymarkenameljob
    $qdg --char "my text"
    vendmy textgristmy texthobbymy textmarkmy textenamelmy textjobmy text

**[--pretext]**
    Specify text to be added to the beginning of a passphrase.

**[--posttext]**
    Specify text to be added to the end of a passphrase.

**[--version]**
    Displays the version number and exits.


Where to Find Additional Support
--------------------------------
You can get personal support or submit a bug report on `GitHub Issues`_.


Version History
---------------
0.2.0 BETA
- added --pretext option
- aaded --posttext option


0.1.9 (6 January 2018)

- added '--version' option
- improved verbose mode printing
- updated documentation, switched to .rst format


0.1.8 (5 January 2018)

- first build release


.. _Unlicense.org: https://unlicense.org
.. _Diceware: http://world.std.com/~reinhold/diceware.html
.. _GitHub Issues: https://github.com/justinsloan/QDG/issues