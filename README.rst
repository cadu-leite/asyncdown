
.. image:: img/asyncdown_big.png



asyncdown
=========

**Python Async Downloader - multiple files**

As simple as possible lib to concurrently download multiple files from a `url`, with limits (`semaphore`) and some control. ;)


Why
---

The first intention was to learn, but then ...

I guess I could have a piece of code able to be called from something like `cron` to periodically download data files.


Main Goals
----------

- Easy to run in a shell with as less configuration as possible.
- Easy to import and be used in a Python Web application.
- Fast with some control (which files where downloaded and how long it takes to be downloaded)


