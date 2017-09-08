Log Module
==========


Purpose of Log
--------------

Log to a message a record it in a specific format created inside of the module.


Using Log
---------

Log is a module for recording timestamped reports into a designated hidden log file. Logs can be viewd in real time by viewing the file: 

:: 

    $ {editor} .log

The function provided by this module is very simple and only requires a messgae to be appended to the default form being logged.

::
    
    from portscan import Log

    send_log("This is a test log")

    $ cat .log
    >> INFO:root:2017-09-07 01:44:40 This is a test log


Log methods
-----------

.. automodule:: portscan.Log
.. autofunction:: send_log