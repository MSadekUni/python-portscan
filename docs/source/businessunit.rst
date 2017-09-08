BusinessUnit Module
===================


Purpose of BusinessUnit
-----------------------

The BusinessUnit object is the backbone of portscan, it structures the data needed for a business unit to exist,
handles reading of input, creates ScanObjects, handles concurrency of scans, and parses output. 


Using BusinessUnit
------------------

Most modules while callable by the user are integrated into BusinessUnit. An example workflow is given below.



BusinessUnit methods
--------------------

.. automodule:: portscan.BusinessUnit
.. autoclass:: BusinessUnit
    :members:

    .. automethod:: __init__

