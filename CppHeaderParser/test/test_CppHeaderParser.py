# -*- coding: utf-8 -*-
import unittest
import sys
if sys.version_info[0] == 2:
    from test import test_support
    sys.path = [".."] + sys.path
    import CppHeaderParser
else:
    import test.support as test_support
    sys.path = ["..", "../python3-libs"] + sys.path
    import CppHeaderParser3 as CppHeaderParser



class SampleClass_SampleClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][0]["name"],
            'SampleClass')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][0]["rtnType"],
            'void')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][0]["parameters"],
            [])

    def test_doxygen(self):
        self.assert_(
        "doxygen"
        not in self.cppHeader.classes["SampleClass"]["methods"]["public"][0].keys())



class SampleClass_meth1_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][1]["name"],
            'meth1')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][1]["rtnType"],
            'string')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][1]["parameters"],
            [])

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][1]["doxygen"],
            '/*!\n* Method 1\n*/')



class SampleClass_meth2_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][2]["name"],
            'meth2')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][2]["rtnType"],
            'int')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][2]["parameters"],
            [{'type': 'int', 'name': 'v1', 'desc': 'Variable 1'}])

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][2]["doxygen"],
            '///\n/// Method 2 description\n///\n/// @param v1 Variable 1\n///')



class SampleClass_meth3_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][3]["name"],
            'meth3')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][3]["rtnType"],
            'void')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][3]["parameters"],
            [{'type': 'const string &', 'name': 'v1', 'desc': 'Variable 1 with a really long wrapping description'}, {'type': 'vector<string> &', 'name': 'v2', 'desc': 'Variable 2'}])

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][3]["doxygen"],
            '/**\n* Method 3 description\n*\n* \\param v1 Variable 1 with a really long\n* wrapping description\n* \\param v2 Variable 2\n*/')



class SampleClass_meth4_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][4]["name"],
            'meth4')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][4]["rtnType"],
            'unsigned int')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][4]["parameters"],
            [])

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][4]["doxygen"],
            '/**********************************\n* Method 4 description\n*\n* @return Return value\n*********************************/')



class SampleClass_meth5_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["private"][0]["name"],
            'meth5')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["private"][0]["rtnType"],
            'void *')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["private"][0]["parameters"],
            [])

    def test_doxygen(self):
        self.assert_(
        "doxygen"
        not in self.cppHeader.classes["SampleClass"]["methods"]["private"][0].keys())



class SampleClass_prop1_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["properties"]["private"][0]["name"],
            'prop1')

    def test_type(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["properties"]["private"][0]["type"],
            'string')

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["properties"]["private"][0]["doxygen"],
            '/// prop1 description')



class SampleClass_prop5_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["properties"]["private"][1]["name"],
            'prop5')

    def test_type(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["properties"]["private"][1]["type"],
            'int')

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["properties"]["private"][1]["doxygen"],
            '//! prop5 description')



class SampleClass_Elephant_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["enums"]["public"][0]["name"],
            'Elephant')

    def test_namespace(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["enums"]["public"][0]["namespace"],
            '')

    def test_doxygen(self):
        self.assert_(
        "doxygen"
        not in self.cppHeader.classes["SampleClass"]["enums"]["public"][0].keys())

    def test_values(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["enums"]["public"][0]["values"],
            [{'name': 'EL_ONE', 'value': '1'}, {'name': 'EL_TWO', 'value': '2'}, {'name': 'EL_NINE', 'value': '9'}, {'name': 'EL_TEN'}])



class AlphaClass_AlphaClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][0]["name"],
            'AlphaClass')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][0]["rtnType"],
            'void')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][0]["parameters"],
            [])

    def test_doxygen(self):
        self.assert_(
        "doxygen"
        not in self.cppHeader.classes["AlphaClass"]["methods"]["public"][0].keys())



class AlphaClass_alphaMethod_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][1]["name"],
            'alphaMethod')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][1]["rtnType"],
            'void')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][1]["parameters"],
            [])

    def test_doxygen(self):
        self.assert_(
        "doxygen"
        not in self.cppHeader.classes["AlphaClass"]["methods"]["public"][1].keys())



class AlphaClass_alphaString_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["properties"]["public"][0]["name"],
            'alphaString')

    def test_type(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["properties"]["public"][0]["type"],
            'string')

    def test_doxygen(self):
        self.assert_(
        "doxygen"
        not in self.cppHeader.classes["AlphaClass"]["properties"]["public"][0].keys())



class AlphaClass_Zebra_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0]["name"],
            'Zebra')

    def test_namespace(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0]["namespace"],
            'Alpha')

    def test_doxygen(self):
        self.assert_(
        "doxygen"
        not in self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0].keys())

    def test_values(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0]["values"],
            [{'name': 'Z_A'}, {'name': 'Z_B', 'value': '0x2B'}, {'name': 'Z_C'}, {'name': 'Z_D'}])



class OmegaClass_OmegaClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["methods"]["public"][0]["name"],
            'OmegaClass')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["methods"]["public"][0]["rtnType"],
            'void')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["methods"]["public"][0]["parameters"],
            [])

    def test_doxygen(self):
        self.assert_(
        "doxygen"
        not in self.cppHeader.classes["OmegaClass"]["methods"]["public"][0].keys())



class OmegaClass_omegaString_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["properties"]["public"][0]["name"],
            'omegaString')

    def test_type(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["properties"]["public"][0]["type"],
            'string')

    def test_doxygen(self):
        self.assert_(
        "doxygen"
        not in self.cppHeader.classes["OmegaClass"]["properties"]["public"][0].keys())



class OmegaClass_Rino_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["enums"]["protected"][0]["name"],
            'Rino')

    def test_namespace(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["enums"]["protected"][0]["namespace"],
            'Alpha::Omega')

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["enums"]["protected"][0]["doxygen"],
            '///\n/// @brief Rino Numbers, not that that means anything\n///')

    def test_values(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["enums"]["protected"][0]["values"],
            [{'name': 'RI_ZERO'}, {'name': 'RI_ONE'}, {'name': 'RI_TWO'}])



def test_main():
    test_support.run_unittest(
        SampleClass_SampleClass_TestCase,
        SampleClass_meth1_TestCase,
        SampleClass_meth2_TestCase,
        SampleClass_meth3_TestCase,
        SampleClass_meth4_TestCase,
        SampleClass_meth5_TestCase,
        SampleClass_prop1_TestCase,
        SampleClass_prop5_TestCase,
        SampleClass_Elephant_TestCase,
        AlphaClass_AlphaClass_TestCase,
        AlphaClass_alphaMethod_TestCase,
        AlphaClass_alphaString_TestCase,
        AlphaClass_Zebra_TestCase,
        OmegaClass_OmegaClass_TestCase,
        OmegaClass_omegaString_TestCase,
        OmegaClass_Rino_TestCase)

if __name__ == '__main__':
    test_main()


