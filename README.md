robotpy-cppheaderparser
=======================

[![Build Status](https://travis-ci.org/robotpy/robotpy-cppheaderparser.svg?branch=master)](https://travis-ci.org/robotpy/robotpy-cppheaderparser)

CppHeaderParser is a pure python C++ header parser that parses C++ headers
and creates a data structure that you can use to do many types of things.
We've found it particularly useful for creating programs that generate
python wrappers around existing C++ programs.

robotpy-cppheaderparser is a fork of the [CppHeaderParser](https://bitbucket.org/senex/cppheaderparser)
library originally created by @senex. CppHeaderParser is an excellent
library and critical to some of the stuff we do in the RobotPy project.
Unfortunately, the maintainer seems to be busy, so robotpy-cppheaderparser
was born.

We don't currently intend to develop new features, but aim to maintain
compatibility with the existing code and make improvements and bugfixes as
we need them.

If you find an bug, we encourage you to submit a pull request! New changes
will only be accepted if there are tests to cover the change you made (and
if they don't break existing tests).

Install
-------

    pip install robotpy-cppheaderparser

Usage
-----

[See the examples](CppHeaderParser/examples).

License
-------

BSD License

Authors
-------

Originally developed by Jashua Cloutier, this fork is maintained by the RobotPy
project.

Past contributors include:
* Jashua Cloutier
* Chris Love
* HartsAntler
