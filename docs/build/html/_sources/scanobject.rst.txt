ScanObject Module
=================


Purpose of ScanObject
---------------------

The ScanObject module is an object that is owned BusinessUnit. This recieves data from the BusinessUnit reading the config files, and configures the nmap scan to be run. It holds data such as: flags, IP set, ports, and output file. It will configure the final command and serve it to the BusinessUnit object when the BusinessUnit.scan() method is called. 


Using ScanObject
----------------

::
    
    Hello World
    This is some example code


ScanObject methods
------------------

.. automodule:: KPS.ScanObject
.. autoclass:: ScanObject
    :members:

    .. automethod:: __init__
