
.. image:: img/asyncdown_big.png



asyncdown
=========

**Python Async Downloader - multiple files**

As simple as possible lib to concurrently download multiple files from `url`s, with limits (`semaphore`) and some control. ;)


Why
---

The first intention was to learn, but then ...

I guess I could have a piece of code able to be called from something like `cron` to periodically download data files.


Main Goals
----------

- Easy to run in a shell with as less configuration as possible.
- Easy to import and be used in Python Web application.
- Fast with some control (which files where downloaded and how long it takes to be downloaded)


Using it
--------

Parameters

::

    optional arguments:
      -h, --help            show this help message and exit
      -u URLS_LIST [URLS_LIST ...], --urls-list URLS_LIST [URLS_LIST ...]
      -c CONCURRENT_DOWNLOADAS, --concurrent-downloadas CONCURRENT_DOWNLOADAS
      -v, --verbose, --no-verbose

sample shell call ...

.. code-block:: bash

    $>python -m asyncdown -v -c 5 -u http://asdASD/FILE2.ZIP  http://sffasdf/asdf/asdfasdf.txt


You may pass arguments trough a `txt` file

sample content below...
::

    -v
    -c=4
    -u=http://200.152.38.155/CNPJ/K3241.K03200Y1.D20312.EMPRECSV.zip
    -u=http://200.152.38.155/CNPJ/K3241.K03200Y2.D20312.EMPRECSV.zip


.. note::

    no arquivo como parâmentro, se as "strings" estão separadas por espaço,
    chega uma lista com uma única string - mesmo tendo espaços.
    e se usar `-u<espace>nome_do_arquivo`
    o espaço fica como parte do nome do arquivo 8(  - argparse bug ?!?



