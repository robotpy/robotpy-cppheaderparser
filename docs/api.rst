API
===

To parse a header file and retrieve the resulting data structure, you'll
want to use the :class:`.CppHeader` object::

    import CppHeaderParser

    header = CppHeaderParser.CppHeader("path/to/header.h")

Below is some documentation of the various object types that CppHeaderParser
will generated after parsing a header file. The documentation is not yet
currently comprehensive, so the best way to see what gets generated is
by printing out the JSON representation:

.. code-block:: sh

   python -m CppHeaderParser.tojson /path/to/header.h


.. warning:: CppHeaderParser is not safe to use from multiple threads

CppHeaderParser
---------------

.. automodule:: CppHeaderParser.CppHeaderParser
   :members: CppBaseDecl, CppClass, CppEnum, CppHeader, CppMethod, CppParseError,
             CppStruct, CppTemplateParam, CppUnion, CppVariable, TagStr,
             ignoreSymbols
   :undoc-members:
   :show-inheritance:
