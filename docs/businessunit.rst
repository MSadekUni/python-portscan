BusinessUnit Module
===================


Purpose of BusinessUnit
-----------------------

The BusinessUnit object is the backbone of portscan, it structures the data needed for a business unit to exist,
handles reading of input, creates ScanObjects, handles concurrency of scans, and parses output. 


Using BusinessUnit
------------------

Most modules while callable by the user are integrated into BusinessUnit. An example workflow is given below.

::

    from portscan import BusinessUnit

    # create a BusinessUnit object with required arugments
    BU = BusinessUnit.BusinessUnit('test_Business', '.')

    # populate data structures by reading in config files
    BU.ReadPorts()
    BU.ReadBase()

    # Trigger the nmap scans
    BU.Scan()

    # Collect all nmap data and write to file
    BU.Collect()

BusinessUnit methods
--------------------

.. automodule:: portscan.BusinessUnit
.. autoclass:: BusinessUnit
    :members:

    .. automethod:: __init__

