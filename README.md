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

## Installation
```sh
pip3 install pox3
```

## API

The following example runs with debug logging, it acts
like a simple hub
```python
from pox3.boot import boot

boot(["log.level", "--DEBUG", "forwarding.hub"])
```

To learn further I would recommend getting the `act_like_switch` method to work
in `samples/of_tutorial.py`, you will need to read the pox3 source code a bit
particularly the files in `pox3/lib/packet/`
