# POX3

This is a python3 port of [POX](https://github.com/noxrepo/pox), a networking
software platform written in Python.
POX3 is forked from POX (Version eel 0.5.0) as its goal it to provide a package based library for
constructing controllers.

## History and Details

POX started life as an OpenFlow controller, but can now also function
as an OpenFlow switch, and can be useful for writing networking software
in general.

POX3 officially requires Python 3.8 (though much of it will work fine
fine with Python 3.7 or even 3.6), and should run under Linux, Mac OS, and Windows.

POX3 currently communicates with OpenFlow 1.0 switches and includes
special support for the Open vSwitch/Nicira extensions.

## API

The following example runs with debug logging the of tutorial, it acts
like a simple hub
```
from pox.boot import boot

boot(["log.level", "--DEBUG", "misc.of_tutorial"])
```
