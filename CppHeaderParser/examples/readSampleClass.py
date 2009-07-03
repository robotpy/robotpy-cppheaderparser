#!/usr/bin/python
import sys
import CppHeaderParser
try:
    cppHeader = CppHeaderParser.CppHeader("SampleClass.h")
except CppHeaderParser.CppParseError,  e:
    print e
    sys.exit(1)
print "CppHeaderParser view of %s"%cppHeader
sampleClass = cppHeader.classes["SampleClass"]
print "Number of public methods %d"%(len(sampleClass["methods"]["public"]))
print "Number of private properties %d"%(len(sampleClass["properties"]["private"]))
meth3 = [m for m in sampleClass["methods"]["public"] if m["name"] == "meth3"][0] #get meth3
meth3ParamTypes = [t["type"] for t in meth3["parameters"]] #get meth3s parameters
print "Parameter Types for public method meth3 %s"%(meth3ParamTypes)
