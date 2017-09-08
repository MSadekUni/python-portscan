Emailing Module
===============


Purpose of Emailing
-------------------

The Eamiling module send push notifications to white listed email handles specified in the config files.


Using Emailing
--------------

Emailing is a module specifically called by the user. No other module explicitly or implicitly imports this set of functions, but does need a BusinessUnit Object to format and send emails.


::

    from portscan import Emailing

    ...

    # After running a BusinessUnit Scan
    BU.Collect()

    if BU.emails > 0:
      Emailing.SendMail(BU)


Emailing methods
----------------

.. automodule:: portscan.Emailing
.. autofunction:: SendMail