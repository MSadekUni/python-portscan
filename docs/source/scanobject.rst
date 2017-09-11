ScanObject Module
=================


Purpose of ScanObject
---------------------

The ScanObject module is an object that is owned BusinessUnit. This recieves data from the BusinessUnit reading the config files, and configures the nmap scan to be run. It holds data such as: flags, IP set, ports, and output file. It will configure the final command and serve it to the BusinessUnit object when the BusinessUnit.scan() method is called. 


Using ScanObject
----------------

ScanObject is implicitly called, but the user still has access to it. The BusinessUnit keeps a list of these objects under BusinessUnit.scan_objs. An basic example of how a ScanObject operates and serves its data is given below.


::

    from portscan import ScanObject

    ...

    BU_SO = ScanObject.ScanObject()
    
    BU_SO.CreateCommand("127.0.0.1:22", "-127.0.0.2", "23", "nmap-test")

    print(BU_SO.command)

    $ open {nmap-dir}/out.html


ScanObject methods
------------------

.. automodule:: portscan.scanobject
.. autoclass:: ScanObject
    :members:

    .. automethod:: __init__
