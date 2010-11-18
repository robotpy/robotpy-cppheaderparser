import sys
sys.path = [".."] + sys.path
import CppHeaderParser

testScript = ""
testCaseClasses = []

def main():
    #init testScript with boiler plate code
    global testScript
    global testCaseClasses
    testScript = """\
import unittest
from test import test_support
import sys
sys.path = [".."] + sys.path
import CppHeaderParser

"""
    cppHeader = CppHeaderParser.CppHeader("SampleClass.h")
    for className, classInstance in cppHeader.classes.items():
        gen_test_cases_for_class(className, classInstance)
    
    testScript += """\


def test_main():
    test_support.run_unittest(
        %s)

if __name__ == '__main__':
    test_main()

"""%",\n        ".join(testCaseClasses)
    
    print testScript

def gen_test_cases_for_class(className, classInstance):
    for methAccessor in classInstance["methods"].keys():
        idx = 0
        for method in classInstance["methods"][methAccessor]:
            gen_test_case_for_method(className, classInstance, methAccessor, idx, method);
            idx += 1

    for propAccessor in classInstance["properties"].keys():
        idx = 0
        for property in classInstance["properties"][propAccessor]:
            gen_test_case_for_property(className, classInstance, propAccessor, idx, property);
            idx += 1

def gen_test_case_for_method(className, classInstance, methAccessor, methIndex, method):
    global testScript
    global testCaseClasses
    testCaseClassName = "%s_%s_TestCase"%(className, method["name"])
    testCaseClasses.append(testCaseClassName)
    testScript += """\


class %s(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

"""%testCaseClassName
    methString = """self.cppHeader.classes["%s"]["methods"]["%s"][%d]"""%(
         className, methAccessor, methIndex)
    for key in ["name", "rtnType", "parameters", "doxygen"]:
        if key in method.keys():
            gen_test_equals(key, methString + '["%s"]'%key, method[key])
        else:
            gen_test_key_not_exist(key, methString)



def gen_test_case_for_property(className, classInstance, propAccessor, propIndex, property):
    global testScript
    global testCaseClasses
    testCaseClassName = "%s_%s_TestCase"%(className, property["name"])
    testCaseClasses.append(testCaseClassName)
    testScript += """\


class %s(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("SampleClass.h")

"""%testCaseClassName
    propString = """self.cppHeader.classes["%s"]["properties"]["%s"][%d]"""%(
         className, propAccessor, propIndex)
    for key in ["name", "type", "doxygen"]:
        if key in property.keys():
            gen_test_equals(key, propString + '["%s"]'%key, property[key])
        else:
            gen_test_key_not_exist(key, propString)




def gen_test_equals(name, v1, v2):
    global testScript
    testScript += """\
    def test_%s(self):
        self.assertEqual(%s, %s)

"""%(name.lower(), v1, repr(v2))

def gen_test_key_not_exist(key, testObj):
    global testScript
    testScript += """\
    def test_%s(self):
        self.assert_("%s" not in %s.keys())
"""%(key.lower(), key, testObj)

if __name__ == "__main__":
    main()


