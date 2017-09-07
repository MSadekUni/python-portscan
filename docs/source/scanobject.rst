ScanObject Module
=================


Purpose of ScanObject
---------------------

The ScanObject module is an object that is owned BusinessUnit. This recieves data from the BusinessUnit reading the config files, and configures the nmap scan to be run. It holds data such as: flags, IP set, ports, and output file. It will configure the final command and serve it to the BusinessUnit object when the BusinessUnit.scan() method is called. 


Using ScanObject
----------------

::
    
    BU_SO = ScanObject.ScanObject()
    
    # populate fields based on line input
    if(BU_SO.Populate(line.strip(' \t\n\r'))):
        # from populated fields, create the command using this data
        BU_SO.CreateCommand(self.exclude_string, self.ports, self.nmap_dir)


ScanObject methods
------------------

.. automodule:: portscan.ScanObject
.. autoclass:: ScanObject
    :members:

    .. automethod:: __init__
