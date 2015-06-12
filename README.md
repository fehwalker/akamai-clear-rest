akamai-clear-rest
=================

Just a Python script to clear Akamai cache via their new REST API.

    $ ./akamai-clear-rest.py --help
    usage: akamai-clear-rest.py [-h] (--cpcode CPCODE | --object OBJECT) --user
                                USER --passwd PASSWD [--timemult TIMEMULT]

    optional arguments:
      -h, --help           show this help message and exit
      --cpcode CPCODE      CP code to clear
      --object OBJECT      Object to clear (can specify multiple times)
      --user USER          Akamai user
      --passwd PASSWD      Akamai password
      --timemult TIMEMULT  Multiplier for Akamai estimated clear time (optional,
                           default 1.5)

Uses the lovely [Requests](http://docs.python-requests.org/en/latest/) module.

Recommend you set PYTHONUNBUFFERED=[whatever] environment variable if you want to see output immediately (for example if running in an automated build system).
