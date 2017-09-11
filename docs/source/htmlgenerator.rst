HTMLGenerator Module
====================


Purpose of HTMLGenerator
------------------------

The HTMLGenerator module provides a programtic generator for HTML output using data provided by a BusinessUnit object. The current version is fixed, and generates only once version of output.


Using HTMLGenerator
-------------------

The BusinessUnit object implicitly calls functions inside of HMTLGenerator, but functions are also avalible to users. GenerateHTML requires a reference to a BusinessUnit object to collect data to generate the HTML report. An VERY basic example is provided below.

::
    
    from portscan imoport HTMLGenerator

    ...

    BU.Collect()

    GenerateHTML(BU)


HTMLGenerator methods
---------------------

.. automodule:: portscan.htmlgenerator
.. autofunction:: GenerateHTML