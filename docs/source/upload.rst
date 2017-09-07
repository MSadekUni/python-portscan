Upload Module
=============


Purpose of Upload
-----------------

This module allows uploading to DropBox to keep reports in a remote accessible repository.

Using Upload
------------

This module is implicitly called the BusinessUnit object, but can still be called by the user. It requires both a Google URL Shortnerer api key defined in an environment variable named 'google_key', and a DropBox API key defined in an environment variable named 'dropbox_key'. If these are not defined a EnvironmentException will be raised and caught in the BusinessUnit Object, and no files will be uploaded.

::

    $ export google_key='{YOUR GOOGLE API KEY}'
    $ export dropbox_key='{YOUR DROPBOX API KEY}'

The function provided by the Upload module requires a list of files to be uploaded and a relative path inside of DropBox to upload to.

::
    
    from portscan import Upload

    ... 

    #relative filepath inside of DropBox
    path = "/nmap-test/"
    files = ['out.html','test.html']
    
    UploadToDropbox(files, path)


Upload methods
--------------

.. automodule:: portscan.Upload
.. autofunction:: UploadToDropbox
