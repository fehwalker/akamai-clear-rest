akamai-clear-rest
=================

Just a Python script to clear Akamai cache via their new REST API.

    $ ./akamai-clear-rest.py --help
    usage: akamai-clear-rest.py [-h] (--cpcode CPCODE | --object OBJECT) --user
                                USER --passwd PASSWD
    
    optional arguments:
      -h, --help       show this help message and exit
      --cpcode CPCODE  CP code to clear
      --object OBJECT  Object to clear (can specify multiple times)
      --user USER      Akamai user
      --passwd PASSWD  Akamai password

Uses the lovely [Requests](http://docs.python-requests.org/en/latest/) module.

Recommend you set PYTHONUNBUFFERED=[whatever] environmnt variable if you want to see output immediately (for example if running in an automated build system).
