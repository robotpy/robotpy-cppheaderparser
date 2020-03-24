# -*- coding: utf-8 -*-
import unittest
import sys

import CppHeaderParser as CppHeaderParser


def filter_pameters(p, extra=[]):
    "Reduce a list of dictionaries to the desired keys for function parameter testing"
    rtn = []
    for d in p:
        rd = {}
        for k in ["name", "desc", "type"] + extra:
            rd[k] = d.get(k)
        rtn.append(rd)
    return rtn


def filter_dict_keys(d, keys):
    "Filter a dictonary to a specified set of keys"
    rtn = {}
    for k in keys:
        rtn[k] = d.get(k, None)
    return rtn


class SampleClass_SampleClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][0]["name"],
            "SampleClass",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][0]["rtnType"],
            "void",
        )

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["SampleClass"]["methods"]["public"][0][
                    "parameters"
                ]
            ),
            [],
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["SampleClass"]["methods"]["public"][0].keys()
        )


class SampleClass_meth1_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][1]["name"],
            "meth1",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][1]["rtnType"],
            "string",
        )

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["SampleClass"]["methods"]["public"][1][
                    "parameters"
                ]
            ),
            [],
        )

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][1]["doxygen"],
            "/*!\n* Method 1\n*/",
        )


class SampleClass_meth2_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][2]["name"],
            "meth2",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][2]["rtnType"],
            "int",
        )

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["SampleClass"]["methods"]["public"][2][
                    "parameters"
                ]
            ),
            [{"type": "int", "name": "v1", "desc": "Variable 1"}],
        )

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][2]["doxygen"],
            "///\n/// Method 2 description\n///\n/// @param v1 Variable 1\n///",
        )


class SampleClass_meth3_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][3]["name"],
            "meth3",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][3]["rtnType"],
            "void",
        )

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["SampleClass"]["methods"]["public"][3][
                    "parameters"
                ]
            ),
            [
                {
                    "type": "const string &",
                    "name": "v1",
                    "desc": "Variable 1 with a really long wrapping description",
                },
                {"type": "vector<string> &", "name": "v2", "desc": "Variable 2"},
            ],
        )

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][3]["doxygen"],
            "/**\n* Method 3 description\n*\n* \\param v1 Variable 1 with a really long\n* wrapping description\n* \\param v2 Variable 2\n*/",
        )


class SampleClass_meth4_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][4]["name"],
            "meth4",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][4]["rtnType"],
            "unsigned int",
        )

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["SampleClass"]["methods"]["public"][4][
                    "parameters"
                ]
            ),
            [],
        )

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][4]["doxygen"],
            "/**********************************\n* Method 4 description\n*\n* @return Return value\n*********************************/",
        )


class SampleClass_meth5_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["private"][0]["name"],
            "meth5",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["private"][0]["rtnType"],
            "void *",
        )

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["SampleClass"]["methods"]["private"][0][
                    "parameters"
                ]
            ),
            [],
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["SampleClass"]["methods"]["private"][0].keys()
        )


class SampleClass_doxygen_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_prop1(self):
        m = self.cppHeader.classes["SampleClass"]["properties"]["private"][0]
        self.assertEqual(m["name"], "prop1")
        self.assertEqual(m["type"], "string")
        self.assertEqual(m["doxygen"], "/// prop1 description")

    def test_prop5(self):
        m = self.cppHeader.classes["SampleClass"]["properties"]["private"][1]
        self.assertEqual(m["name"], "prop5")
        self.assertEqual(m["type"], "int")
        self.assertEqual(m["doxygen"], "//! prop5 description")

    def test_prop6(self):
        m = self.cppHeader.classes["SampleClass"]["properties"]["private"][2]
        self.assertEqual(m["name"], "prop6")
        self.assertEqual(m["type"], "bool")
        self.assertEqual(m["doxygen"], "/*!< prop6 description */")

    def test_prop7(self):
        m = self.cppHeader.classes["SampleClass"]["properties"]["private"][3]
        self.assertEqual(m["name"], "prop7")
        self.assertEqual(m["type"], "double")
        self.assertEqual(m["doxygen"], "//!< prop7 description\n//!< with two lines")

    def test_prop8(self):
        m = self.cppHeader.classes["SampleClass"]["properties"]["private"][4]
        self.assertEqual(m["name"], "prop8")
        self.assertEqual(m["type"], "int")
        self.assertEqual(m["doxygen"], "/// prop8 description")


class SampleClass_Elephant_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["enums"]["public"][0]["name"],
            "Elephant",
        )

    def test_namespace(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["enums"]["public"][0]["namespace"], ""
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["SampleClass"]["enums"]["public"][0].keys()
        )

    def test_values(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["enums"]["public"][0]["values"],
            [
                {"name": "EL_ONE", "value": 1},
                {"name": "EL_TWO", "value": 2},
                {"name": "EL_NINE", "value": 9},
                {"name": "EL_TEN", "value": 10},
            ],
        )


class AlphaClass_AlphaClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][0]["name"],
            "AlphaClass",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][0]["rtnType"],
            "void",
        )

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["AlphaClass"]["methods"]["public"][0][
                    "parameters"
                ]
            ),
            [],
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["AlphaClass"]["methods"]["public"][0].keys()
        )


class AlphaClass_alphaMethod_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][1]["name"],
            "alphaMethod",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["methods"]["public"][1]["rtnType"],
            "void",
        )

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["AlphaClass"]["methods"]["public"][1][
                    "parameters"
                ]
            ),
            [],
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["AlphaClass"]["methods"]["public"][1].keys()
        )


class AlphaClass_alphaString_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["properties"]["public"][0]["name"],
            "alphaString",
        )

    def test_type(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["properties"]["public"][0]["type"],
            "string",
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["AlphaClass"]["properties"]["public"][
                0
            ].keys()
        )


class AlphaClass_Zebra_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0]["name"],
            "Zebra",
        )

    def test_namespace(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0]["namespace"],
            "Alpha",
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0].keys()
        )

    def test_values(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0]["values"],
            [
                {"name": "Z_A", "value": 0},
                {"name": "Z_B", "raw_value": "0x2B", "value": 43},
                {"name": "Z_C", "raw_value": "j", "value": 106},
                {"name": "Z_D", "value": 107},
            ],
        )


class OmegaClass_OmegaClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["methods"]["public"][0]["name"],
            "OmegaClass",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["methods"]["public"][0]["rtnType"],
            "void",
        )

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["OmegaClass"]["methods"]["public"][0][
                    "parameters"
                ]
            ),
            [],
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["OmegaClass"]["methods"]["public"][0].keys()
        )


class OmegaClass_omegaString_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["properties"]["public"][0]["name"],
            "omegaString",
        )

    def test_type(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["properties"]["public"][0]["type"],
            "string",
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["OmegaClass"]["properties"]["public"][
                0
            ].keys()
        )


class OmegaClass_Rino_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["enums"]["protected"][0]["name"],
            "Rino",
        )

    def test_namespace(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["enums"]["protected"][0]["namespace"],
            "Alpha::Omega",
        )

    def test_doxygen(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["enums"]["protected"][0]["doxygen"],
            "///\n/// @brief Rino Numbers, not that that means anything\n///",
        )

    def test_values(self):
        self.assertEqual(
            self.cppHeader.classes["OmegaClass"]["enums"]["protected"][0]["values"],
            [
                {"name": "RI_ZERO", "value": 0, "doxygen": "/// item zero"},
                {"name": "RI_ONE", "value": 1, "doxygen": "/** item one */"},
                {"name": "RI_TWO", "value": 2, "doxygen": "//!< item two"},
                {"name": "RI_THREE", "value": 3},
                {"name": "RI_FOUR", "value": 4, "doxygen": "/// item four"},
            ],
        )


class Bug3488053_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_public(self):
        self.assertEqual(
            len(
                self.cppHeader.classes["Bug_3488053::Bug_3488053_Nested"]["properties"][
                    "public"
                ]
            ),
            1,
        )

    def test_private(self):
        self.assertEqual(
            len(
                self.cppHeader.classes["Bug_3488053::Bug_3488053_Nested"]["properties"][
                    "private"
                ]
            ),
            0,
        )

    def test_protected(self):
        self.assertEqual(
            len(
                self.cppHeader.classes["Bug_3488053::Bug_3488053_Nested"]["properties"][
                    "protected"
                ]
            ),
            0,
        )


class Bug3488360_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_BloodOrange_inherits(self):
        self.assertEqual(self.cppHeader.classes["BloodOrange"]["inherits"], [])

    def test_Bananna_inherits(self):
        self.assertEqual(
            self.cppHeader.classes["Bananna"]["inherits"],
            [
                {
                    "access": "public",
                    "class": "Citrus::BloodOrange",
                    "decl_name": "Citrus::BloodOrange",
                    "decltype": False,
                    "virtual": False,
                    "...": False,
                }
            ],
        )

    def test_ExcellentCake_inherits(self):
        self.assertEqual(
            self.cppHeader.classes["ExcellentCake"]["inherits"],
            [
                {
                    "access": "private",
                    "class": "Citrus::BloodOrange",
                    "decl_name": "Citrus::BloodOrange",
                    "decltype": False,
                    "virtual": False,
                    "...": False,
                },
                {
                    "access": "private",
                    "class": "Convoluted::Nested::Mixin",
                    "decl_name": "Convoluted::Nested::Mixin",
                    "decltype": False,
                    "virtual": False,
                    "...": False,
                },
            ],
        )


class Bug3487551_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_method_rtn_type(self):
        self.assertEqual(
            self.cppHeader.classes["Bug_3487551"]["methods"]["public"][0]["rtnType"],
            "int",
        )


class SampleStruct_meth_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["methods"]["public"][0]["name"],
            "meth",
        )

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["methods"]["public"][0]["rtnType"],
            "unsigned int",
        )

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["methods"]["public"][0][
                "parameters"
            ],
            [],
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["SampleStruct"]["methods"]["public"][0].keys()
        )


class SampleStruct_prop_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["properties"]["private"][0]["name"],
            "prop",
        )

    def test_type(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["properties"]["private"][0]["type"],
            "int",
        )

    def test_doxygen(self):
        self.assertTrue(
            "doxygen"
            not in self.cppHeader.classes["SampleStruct"]["properties"]["private"][
                0
            ].keys()
        )


class Bird_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_items_array(self):
        self.assertEqual(
            self.cppHeader.classes["Bird"]["properties"]["private"][0]["array"], 1
        )

    def test_otherItems_array(self):
        self.assertEqual(
            self.cppHeader.classes["Bird"]["properties"]["private"][1]["array"], 1
        )

    def test_oneItem_array(self):
        self.assertEqual(
            self.cppHeader.classes["Bird"]["properties"]["private"][2]["array"], 0
        )

    def test_items_array_size(self):
        self.assertEqual(
            self.cppHeader.classes["Bird"]["properties"]["private"][0]["array_size"],
            "MAX_ITEM",
        )

    def test_otherItems_array_size(self):
        self.assertEqual(
            self.cppHeader.classes["Bird"]["properties"]["private"][1]["array_size"],
            "7",
        )


class Monkey_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Monkey"]["methods"]["public"]), 0)

    def test_num_private_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Monkey"]["methods"]["private"]), 1)

    def test_num_protected_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["Monkey"]["methods"]["protected"]), 0
        )


class Chicken_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Chicken"]["methods"]["public"]), 0)

    def test_num_private_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["Chicken"]["methods"]["private"]), 1
        )

    def test_num_protected_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["Chicken"]["methods"]["protected"]), 0
        )

    def test_template(self):
        self.assertEqual(
            self.cppHeader.classes["Chicken"]["methods"]["private"][0]["template"],
            "template<typename T>",
        )


class Lizzard_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_normal_constructor(self):
        cmp_values = {
            "inline": False,
            "name": "Lizzard",
            "parameters": [],
            "friend": False,
            "explicit": False,
            "constructor": True,
            "namespace": "",
            "destructor": False,
            "pure_virtual": False,
            "returns": "",
            "static": False,
            "virtual": False,
            "template": False,
            "rtnType": "void",
            "extern": False,
            "path": "Lizzard",
            "returns_pointer": 0,
            "class": None,
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["Lizzard"]["methods"]["private"][0],
                cmp_values.keys(),
            ),
            cmp_values,
        )

    def test_explicit_constructor(self):
        cmp_values = {
            "inline": False,
            "name": "Lizzard",
            "friend": False,
            "explicit": True,
            "constructor": True,
            "namespace": "",
            "destructor": False,
            "pure_virtual": False,
            "returns": "",
            "static": False,
            "virtual": False,
            "template": False,
            "rtnType": "void",
            "extern": False,
            "path": "Lizzard",
            "returns_pointer": 0,
            "class": None,
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["Lizzard"]["methods"]["private"][1],
                cmp_values.keys(),
            ),
            cmp_values,
        )


class Owl_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Owl"]["methods"]["public"]), 0)

    def test_num_private_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Owl"]["methods"]["private"]), 1)

    def test_num_protected_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Owl"]["methods"]["protected"]), 0)


class Grape_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["GrapeClass"]["properties"]["public"]), 0
        )

    def test_num_private_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["GrapeClass"]["properties"]["private"]), 1
        )

    def test_num_protected_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["GrapeClass"]["properties"]["protected"]), 0
        )

    def test_num_public_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["GrapeClass"]["methods"]["public"]), 0
        )

    def test_num_private_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["GrapeClass"]["methods"]["private"]), 1
        )

    def test_num_protected_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["GrapeClass"]["methods"]["protected"]), 0
        )


class AnonHolderClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_property(self):
        cmp_values = {
            "constant": 0,
            "name": "a",
            "reference": 0,
            "type": "<anon-struct-1>",
            "static": 0,
            "pointer": 0,
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["AnonHolderClass"]["properties"]["public"][0],
                cmp_values.keys(),
            ),
            cmp_values,
        )


class CowClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_class_declaration_method(self):
        self.assertEqual(
            self.cppHeader.classes["CowClass"]["declaration_method"], "class"
        )

    def test_struct_declaration_method(self):
        self.assertEqual(
            self.cppHeader.classes["CowStruct"]["declaration_method"], "struct"
        )


class Mango_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_virtual_inherits(self):
        self.assertEqual(
            self.cppHeader.classes["MangoClass"]["inherits"][0]["virtual"], True
        )


class Eagle_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_property(self):
        cmp_values = {
            "constant": 0,
            "name": "a",
            "reference": 0,
            "array_size": "MAX_LEN",
            "type": "int",
            "static": 0,
            "pointer": 0,
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["EagleClass"]["properties"]["private"][0],
                cmp_values.keys(),
            ),
            cmp_values,
        )


class Frog_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["FrogClass"]["properties"]["private"]), 3
        )


class Cat_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["CatClass"]["properties"]["private"]), 0
        )


class Fish_TestCase(unittest.TestCase):
    def setUp(self):
        # Just make sure it doesnt crash
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")


class Panda_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_property_CONST_A(self):
        cmp_values = {
            "typedef": None,
            "unresolved": False,
            "constant": 1,
            "name": "CONST_A",
            "parent": self.cppHeader.classes["PandaClass"],
            "pointer": 0,
            "namespace": "",
            "raw_type": "int",
            "class": 0,
            "property_of_class": "PandaClass",
            "static": 1,
            "fundamental": True,
            "mutable": False,
            "typedefs": 0,
            "array": 0,
            "type": "static const int",
            "reference": 0,
            "aliases": [],
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["PandaClass"]["properties"]["private"][0],
                cmp_values.keys(),
            ),
            cmp_values,
        )

    def test_property_CONST_B(self):
        cmp_values = {
            "typedef": None,
            "unresolved": False,
            "constant": 1,
            "name": "CONST_B",
            "parent": self.cppHeader.classes["PandaClass"],
            "pointer": 0,
            "namespace": "",
            "raw_type": "int",
            "class": 0,
            "property_of_class": "PandaClass",
            "static": 1,
            "fundamental": True,
            "mutable": False,
            "typedefs": 0,
            "array": 0,
            "type": "static const int",
            "reference": 0,
            "aliases": [],
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["PandaClass"]["properties"]["private"][1],
                cmp_values.keys(),
            ),
            cmp_values,
        )


class Potato_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties_potato(self):
        self.assertEqual(
            len(self.cppHeader.classes["PotatoClass"]["properties"]["private"]), 1
        )

    def test_num_public_properties_potato_fwdstruct(self):
        self.assertEqual(
            len(
                self.cppHeader.classes["PotatoClass::FwdStruct"]["properties"]["public"]
            ),
            1,
        )


class Hog_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties_potato(self):
        self.assertEqual(
            len(self.cppHeader.classes["HogClass"]["properties"]["private"]), 1
        )

    def test_property(self):
        cmp_values = {
            "constant": 0,
            "name": "u",
            "reference": 0,
            "type": "HogUnion",
            "static": 0,
            "pointer": 0,
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["HogClass"]["properties"]["private"][0],
                cmp_values.keys(),
            ),
            cmp_values,
        )

    def test_union(self):
        cmp_values = {
            "name": "HogUnion",
            "parent": self.cppHeader.classes["HogClass"],
            "declaration_method": "union",
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["HogClass::HogUnion"], cmp_values.keys()
            ),
            cmp_values,
        )

    def test_union_member_a(self):
        cmp_values = {
            "constant": 0,
            "name": "a",
            "reference": 0,
            "type": "int",
            "static": 0,
            "pointer": 0,
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["HogClass::HogUnion"]["members"][0],
                cmp_values.keys(),
            ),
            cmp_values,
        )

    def test_union_member_b(self):
        cmp_values = {
            "constant": 0,
            "name": "b",
            "reference": 0,
            "type": "float",
            "static": 0,
            "pointer": 0,
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["HogClass::HogUnion"]["members"][1],
                cmp_values.keys(),
            ),
            cmp_values,
        )


# Bug 3497158
class CherryClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties(self):
        self.assertEqual(
            len(
                self.cppHeader.classes["CherryClass::NestStruct"]["properties"][
                    "public"
                ]
            ),
            1,
        )

    def test_num_public_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["CherryClass::NestStruct"]["methods"]["public"]),
            1,
        )


# Bug 3517308
class GarlicClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["GarlicClass"]["properties"]["public"]), 0
        )

    def test_num_public_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["GarlicClass"]["methods"]["public"]), 3
        )


# Bug 3514728
class CarrotClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["CarrotClass"]["properties"]["private"]), 1
        )

    def test_num_private_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["CarrotClass"]["methods"]["private"]), 1
        )

    def test_method_params(self):
        self.assertEqual(
            filter_pameters(
                self.cppHeader.classes["CarrotClass"]["methods"]["private"][0][
                    "parameters"
                ]
            ),
            [],
        )

    def test_class_template(self):
        self.assertEqual(
            self.cppHeader.classes["CarrotClass"]["template"], "template<class T>"
        )


# Bug 3517289
class CarrotClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["ExternClass"]["methods"]["private"]), 1
        )


# Bug 3514671
class OliveStruct_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["OliveStruct"]["properties"]["public"]), 4
        )

    def test_var_a(self):
        self.assertEqual(
            self.cppHeader.classes["OliveStruct"]["properties"]["public"][0]["name"],
            "a",
        )


# Bug 3515330
class Rooster_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["RoosterOuterClass"]["properties"]["public"]), 1
        )

    def test_num_private_properties(self):
        self.assertEqual(
            len(self.cppHeader.classes["RoosterOuterClass"]["properties"]["private"]), 1
        )

    def test_num_sub1_public_properties(self):
        self.assertEqual(
            len(
                self.cppHeader.classes["RoosterOuterClass::RoosterSubClass1"][
                    "properties"
                ]["public"]
            ),
            1,
        )

    def test_num_sub1_private_properties(self):
        self.assertEqual(
            len(
                self.cppHeader.classes["RoosterOuterClass::RoosterSubClass1"][
                    "properties"
                ]["private"]
            ),
            1,
        )

    def test_num_sub2_public_properties(self):
        self.assertEqual(
            len(
                self.cppHeader.classes["RoosterOuterClass::RoosterSubClass2"][
                    "properties"
                ]["public"]
            ),
            1,
        )

    def test_num_sub2_private_properties(self):
        self.assertEqual(
            len(
                self.cppHeader.classes["RoosterOuterClass::RoosterSubClass2"][
                    "properties"
                ]["private"]
            ),
            1,
        )


# Bug 3514672
class OperatorClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_op_0(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][0]["name"],
            "operator=",
        )

    def test_op_1(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][1]["name"],
            "operator-=",
        )

    def test_op_2(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][2]["name"],
            "operator+=",
        )

    def test_op_3(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][3]["name"],
            "operator[]",
        )

    def test_op_4(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][4]["name"],
            "operator==",
        )

    def test_op_5(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][5]["name"],
            "operator+",
        )

    def test_op_6(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][6]["name"],
            "operator-",
        )

    def test_op_7(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][7]["name"],
            "operator*",
        )

    def test_op_8(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][8]["name"],
            "operator\\",
        )

    def test_op_9(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][9]["name"],
            "operator%",
        )

    def test_op_10(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][10]["name"],
            "operator^",
        )

    def test_op_11(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][11]["name"],
            "operator|",
        )

    def test_op_12(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][12]["name"],
            "operator&",
        )

    def test_op_13(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][13]["name"],
            "operator~",
        )

    def test_op_14(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][14]["name"],
            "operator<<",
        )

    def test_op_15(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][15]["name"],
            "operator>>",
        )

    def test_op_16(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][16]["name"],
            "operator!=",
        )

    def test_op_17(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][17]["name"],
            "operator<",
        )

    def test_op_18(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][18]["name"],
            "operator>",
        )

    def test_op_19(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][19]["name"],
            "operator>=",
        )

    def test_op_20(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][20]["name"],
            "operator<=",
        )

    def test_op_21(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][21]["name"],
            "operator!",
        )

    def test_op_22(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][22]["name"],
            "operator&&",
        )

    def test_op_23(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][23]["name"],
            "operator||",
        )

    def test_op_24(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][24]["name"],
            "operator+=",
        )

    def test_op_25(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][25]["name"],
            "operator-=",
        )

    def test_op_26(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][26]["name"],
            "operator*=",
        )

    def test_op_27(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][27]["name"],
            "operator\\=",
        )

    def test_op_28(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][28]["name"],
            "operator%=",
        )

    def test_op_29(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][29]["name"],
            "operator&=",
        )

    def test_op_30(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][30]["name"],
            "operator|=",
        )

    def test_op_31(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][31]["name"],
            "operator^=",
        )

    def test_op_32(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][32]["name"],
            "operator<<=",
        )

    def test_op_33(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][33]["name"],
            "operator>>=",
        )

    def test_op_34(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][34]["name"],
            "operator++",
        )

    def test_op_35(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][35]["name"],
            "operator--",
        )

    def test_op_36(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][36]["name"],
            "operator()",
        )

    def test_op_37(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][37]["name"],
            "operator->",
        )

    def test_op_38(self):
        self.assertEqual(
            self.cppHeader.classes["OperatorClass"]["methods"]["public"][38]["name"],
            "operator,",
        )


# Feature Request 3519502 & 3523010
class CrowClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.savedSupportedAccessSpecifier = CppHeaderParser.supportedAccessSpecifier
        CppHeaderParser.supportedAccessSpecifier.append(
            "public  slots "
        )  # intentionally add expra spaces to make sure they get cleaned up
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["CrowClass"]["methods"]["public"]), 1
        )

    def test_rtntype_public_slot_method(self):
        self.assertEqual(
            self.cppHeader.classes["CrowClass"]["methods"]["public slots"][0][
                "rtnType"
            ],
            "void",
        )

    def test_num_public_slot_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["CrowClass"]["methods"]["public slots"]), 1
        )

    def tearDown(self):
        CppHeaderParser.supportedAccessSpecifier = self.savedSupportedAccessSpecifier


# Bug 3497170
class DriverFuncs_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name_0(self):
        self.assertEqual(
            self.cppHeader.classes["DriverFuncs"]["properties"]["public"][0]["name"],
            "init",
        )

    def test_type_0(self):
        self.assertEqual(
            self.cppHeader.classes["DriverFuncs"]["properties"]["public"][0]["type"],
            "void * ( * ) ( )",
        )

    def test_function_pointer_field_0(self):
        self.assertEqual(
            self.cppHeader.classes["DriverFuncs"]["properties"]["public"][0][
                "function_pointer"
            ],
            1,
        )

    def test_name_1(self):
        self.assertEqual(
            self.cppHeader.classes["DriverFuncs"]["properties"]["public"][1]["name"],
            "write",
        )

    def test_type_1(self):
        self.assertEqual(
            self.cppHeader.classes["DriverFuncs"]["properties"]["public"][1]["type"],
            "void ( * ) ( void * buf, int buflen )",
        )

    def test_function_pointer_field_1(self):
        self.assertEqual(
            self.cppHeader.classes["DriverFuncs"]["properties"]["public"][1][
                "function_pointer"
            ],
            1,
        )


# Bug 3519178
class Snail_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_rtn_type(self):
        self.assertEqual(
            self.cppHeader.classes["Snail2Class"]["methods"]["public"][0]["rtnType"],
            "SnailNamespace::SnailClass",
        )

    def test_param_name(self):
        self.assertEqual(
            self.cppHeader.classes["Snail2Class"]["methods"]["public"][0]["parameters"][
                0
            ]["name"],
            "",
        )

    def test_param_name(self):
        self.assertEqual(
            self.cppHeader.classes["Snail2Class"]["methods"]["public"][0]["parameters"][
                0
            ]["type"],
            "tr1::shared_ptr<SnailTemplateClass<SnailNamespace::SnailClass> >",
        )


# Feature Request 3523198
class Quale_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_rtn_type(self):
        self.assertEqual(
            self.cppHeader.classes["QualeClass"]["methods"]["private"][0]["rtnType"],
            "void",
        )


# Feature Request 3523235
class Rock_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_const_0(self):
        self.assertEqual(
            self.cppHeader.classes["RockClass"]["methods"]["private"][0]["const"], True
        )

    def test_const_1(self):
        self.assertEqual(
            self.cppHeader.classes["RockClass"]["methods"]["private"][1]["const"], False
        )


# Bug 3523196
class Almond_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_rtn_type(self):
        self.assertEqual(
            self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["rtnType"],
            "std::map<unsigned, std::pair<unsigned, SnailTemplateClass<SnailNamespace::SnailClass> > >",
        )

    def test_param_1_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["parameters"][
                0
            ]["name"],
            "flag",
        )

    def test_param_1_type(self):
        self.assertEqual(
            self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["parameters"][
                0
            ]["type"],
            "bool",
        )

    def test_param_2_name(self):
        self.assertEqual(
            self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["parameters"][
                1
            ]["name"],
            "bigArg",
        )

    def test_param_2_type(self):
        self.assertEqual(
            self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["parameters"][
                1
            ]["type"],
            "std::map<unsigned, std::pair<unsigned, SnailTemplateClass<SnailNamespace::SnailClass> > >",
        )


# Bug 3524327
class Stone_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_const_0(self):
        self.assertEqual(
            self.cppHeader.classes["StoneClass"]["methods"]["private"][0]["const"], True
        )

    def test_const_1(self):
        self.assertEqual(
            self.cppHeader.classes["StoneClass"]["methods"]["private"][1]["const"],
            False,
        )


# Bug 3531219
class Kangaroo_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_kangaroo_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["Kangaroo"]["methods"]["public"]), 1
        )

    def test_num_joey_methods(self):
        self.assertEqual(
            len(self.cppHeader.classes["Kangaroo::Joey"]["methods"]["public"]), 1
        )


# Bug 3535465
class Ant_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_constructor_1_params(self):
        self.assertEqual(
            len(self.cppHeader.classes["Ant"]["methods"]["public"][0]["parameters"]), 3
        )

    def test_num_constructor_2_params(self):
        self.assertEqual(
            len(self.cppHeader.classes["Ant"]["methods"]["public"][1]["parameters"]), 1
        )


# Bug 3536069
class Onion_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties_red(self):
        self.assertEqual(
            len(self.cppHeader.classes["Onion<Red,Plant>"]["properties"]["public"]), 1
        )

    def test_num_public_properties_sweet(self):
        self.assertEqual(
            len(self.cppHeader.classes["Onion<Sweet,Plant>"]["properties"]["public"]), 1
        )

    def test_class_template(self):
        self.assertEqual(
            self.cppHeader.classes["Onion<Sweet,Plant>"]["template"],
            "template<typename Plant>",
        )


# Bug 3536067
class BlueJay_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["BlueJay"]["methods"]["public"]), 1)


# Bug 3536266
class functions_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """\
              void global_funct1(int i);             
              int global_funct2(void);
              """,
            "string",
        )

    def test_num_functions(self):
        self.assertEqual(len(self.cppHeader.functions), 2)

    def test_function_name_1(self):
        self.assertEqual(self.cppHeader.functions[0]["name"], "global_funct1")

    def test_function_name_2(self):
        self.assertEqual(self.cppHeader.functions[1]["name"], "global_funct2")


# Bug 3536071
class Pea_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_inherits(self):
        self.assertEqual(len(self.cppHeader.classes["Pea"]["inherits"]), 1)

    def test_name_inherits(self):
        self.assertEqual(
            self.cppHeader.classes["Pea"]["inherits"][0]["class"], "Vegetable<Green>"
        )


# Bug 3540172
class functions2_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """\
              void global_funct1(int i);             
              int global_funct2(void){
                  // do something
              }
              """,
            "string",
        )

    def test_num_functions(self):
        self.assertEqual(len(self.cppHeader.functions), 2)

    def test_function_name_1(self):
        self.assertEqual(self.cppHeader.functions[0]["name"], "global_funct1")

    def test_function_name_2(self):
        self.assertEqual(self.cppHeader.functions[1]["name"], "global_funct2")


# Feature: line numbers
class line_num_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("LineNumTest.h")

    def test_lineno_function1(self):
        return self.assertEqual(self.cppHeader.functions[0]["line_number"], 13)

    def test_lineno_function2(self):
        return self.assertEqual(self.cppHeader.functions[1]["line_number"], 17)

    def test_lineno_Worm(self):
        return self.assertEqual(self.cppHeader.classes["Worm"]["line_number"], 20)

    def test_lineno_Worm_Constructor(self):
        return self.assertEqual(
            self.cppHeader.classes["Worm"]["methods"]["public"][0]["line_number"], 23
        )

    def test_lineno_Worm_getName(self):
        return self.assertEqual(
            self.cppHeader.classes["Worm"]["methods"]["public"][1]["line_number"], 24
        )

    def test_lineno_Worm_namep(self):
        return self.assertEqual(
            self.cppHeader.classes["Worm"]["properties"]["private"][0]["line_number"],
            29,
        )


# Bug 3567172
class Pear_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_property(self):
        self.assertEqual(
            self.cppHeader.classes["Pear"]["properties"]["private"][0]["name"],
            "stem_property",
        )


# Bug 3567217 and 3569663
class Macro_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            r"""
#include <string.h>
#include "../../debug.h"

#define ONE 1
#define TWO_NUM_N_NAME "2 (TWO)"
#pragma once

 #define DEBUG_PRINT(x)           \
    printf("---------------\n"); \
    printf("DEBUG: %d\n", x);    \
    printf("---------------\n");""",
            "string",
        )

    def test_includes(self):
        self.assertEqual(self.cppHeader.includes, ["<string.h>", '"../../debug.h"'])
        self.assertEqual(self.cppHeader.includes_detail[0]["value"], "<string.h>")
        self.assertEqual(self.cppHeader.includes_detail[0]["line_number"], 2)
        self.assertEqual(self.cppHeader.includes_detail[1]["value"], '"../../debug.h"')
        self.assertEqual(self.cppHeader.includes_detail[1]["line_number"], 3)

    def test_pragmas(self):
        self.assertEqual(self.cppHeader.pragmas, ["once"])
        self.assertEqual(self.cppHeader.pragmas_detail[0]["value"], "once")
        self.assertEqual(self.cppHeader.pragmas_detail[0]["line_number"], 7)

    def test_pragmas0(self):
        self.assertEqual(self.cppHeader.defines[0], "ONE 1")
        self.assertEqual(self.cppHeader.defines_detail[0]["value"], "ONE 1")
        self.assertEqual(self.cppHeader.defines_detail[0]["line_number"], 5)

    def test_pragmas1(self):
        self.assertEqual(self.cppHeader.defines[1], 'TWO_NUM_N_NAME "2 (TWO)"')
        self.assertEqual(
            self.cppHeader.defines_detail[1]["value"], 'TWO_NUM_N_NAME "2 (TWO)"'
        )
        self.assertEqual(self.cppHeader.defines_detail[1]["line_number"], 6)

    def test_pragmas2(self):
        self.assertEqual(
            self.cppHeader.defines[2],
            'DEBUG_PRINT(x)           \\\n    printf("---------------\\n"); \\\n    printf("DEBUG: %d\\n", x);    \\\n    printf("---------------\\n");',
        )


# Bug: 3567854 and 3568241
class Beans_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_public_props(self):
        self.assertEqual(
            len(self.cppHeader.classes["Beans"]["properties"]["public"]), 4
        )
        self.assertEqual(
            self.cppHeader.classes["Beans"]["properties"]["public"][2]["name"], "data"
        )

    def test_anonymous_union_name(self):
        return self.assertEqual(
            self.cppHeader.classes["Beans"]["properties"]["public"][1]["name"], ""
        )

    def test_second_anonymous_union_name(self):
        return self.assertEqual(
            self.cppHeader.classes["Beans"]["properties"]["public"][3]["name"], ""
        )


# Bug: 3567854 and 3568241
class termite_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_termite_function(self):
        f = self.cppHeader.functions[5]
        self.assertEqual(f["name"], "termite")
        self.assertEqual(len(f["parameters"]), 0)


# Bug: 3569622
class Japyx_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_japyxFunc(self):
        self.assertEqual(self.cppHeader.functions[6]["name"], "japyxFunc")


# Bug: 3570105
class Author_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(self.cppHeader.enums[0]["name"], "Author")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.enums[0]["values"],
            [{"name": "NAME", "value": "( 'J' << 24 | 'A' << 16 | 'S' << 8 | 'H' )"}],
        )


# Bug: 3577484
class Fly_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_exists(self):
        self.assertEqual("FruitFly<int>" in self.cppHeader.classes, True)


# Bug BitBucket #2
class ClassAfterMagicMacro_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_class_exists(self):
        self.assertEqual("ClassAfterMagicMacro" in self.cppHeader.classes, True)


# Bug BitBucket #3
class FilterMagicMacro_TestCase(unittest.TestCase):
    def setUp(self):
        savedIgnoreSymbols = CppHeaderParser.ignoreSymbols
        CppHeaderParser.ignoreSymbols.append("MAGIC_FUNC()")
        self.cppHeader = CppHeaderParser.CppHeader(
            r"""
class FilterMagicMacro
{
public:

  MAGIC_FUNC(var)
  MAGIC_FUNC(v,
             a,
             r)
  MAGIC_FUNC((int)var)
  MAGIC_FUNC(((()))var()()())
  MAGIC_FUNC("1) \" var")

  void FilterMagicMacroMethod(int);
};""",
            "string",
        )
        CppHeaderParser.ignoreSymbols = savedIgnoreSymbols

    def test_method_exists(self):
        self.assertEqual(
            self.cppHeader.classes["FilterMagicMacro"]["methods"]["public"][0]["name"],
            "FilterMagicMacroMethod",
        )

    def test_line_num_is_correct(self):
        self.assertEqual(
            self.cppHeader.classes["FilterMagicMacro"]["methods"]["public"][0][
                "line_number"
            ],
            14,
        )


# Bug BitBucket #4
class ClassRegularTypedefs_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_uint_exists(self):
        self.assertEqual("uint" in self.cppHeader.typedefs, True)

    def test_string_array_exists(self):
        self.assertEqual("string_array" in self.cppHeader.typedefs, True)

    def test_SmartObjPtr_exists(self):
        self.assertEqual("SmartObjPtr" in self.cppHeader.typedefs, True)

    def test_StrStrMap_exists(self):
        self.assertEqual("StrStrMap" in self.cppHeader.typedefs, True)

    def test_AfterTypedefClass_exists(self):
        self.assertEqual("AfterTypedefClass" in self.cppHeader.classes, True)


# Bug BitBucket #6
class LineNumAfterDivide_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """

// Bug BitBucket #6
class LineNumAfterDivide
{
  static int func1(float alpha_num)
  { return funcX(alpha_num /
                 beta_num); }
  void func2();
};

""",
            "string",
        )

    def test_line_num(self):
        m = self.cppHeader.classes["LineNumAfterDivide"]["methods"]["private"][1]
        self.assertEqual("func2", m["name"])
        self.assertEqual(9, m["line_number"])


# Bug BitBucket #5
class ClassHerbCilantro_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_HerbCilantro_exists(self):
        self.assertEqual("Herb::Cilantro" in self.cppHeader.classes, True)


# Bug BitBucket #7
class print_statement_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_function_name_type(self):
        self.assertEqual(self.cppHeader.functions[7]["name"], "print_statement")

    def test_return_type(self):
        self.assertEqual(self.cppHeader.functions[7]["returns"], "int")


# Bug BitBucket #8
class Garlic_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_function_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Garlic"]["methods"]["public"][0]["name"], "genNum"
        )


# Bug SourceForge #54
class Wheat_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(self.cppHeader.enums[1]["name"], "Wheat")

    def test_typedef(self):
        self.assertEqual(self.cppHeader.enums[1]["typedef"], False)


# Bug SourceForge #55
class PeachPlumb_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_Peach_exists(self):
        self.assertEqual("Peach" in self.cppHeader.classes, True)

    def test_Plumb_exists(self):
        self.assertEqual("Plumb" in self.cppHeader.classes, True)

    def test_function_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Plumb"]["methods"]["private"][0]["name"],
            "doSomethingGreat",
        )


# Bug BitBucket #9
class Grape_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_Grape_exists(self):
        self.assertEqual("Grape" in self.cppHeader.classes, True)

    def test_a_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Grape"]["properties"]["public"][0]["name"], "a"
        )

    def test_a_type(self):
        self.assertEqual(
            self.cppHeader.classes["Grape"]["properties"]["public"][0]["type"], "int"
        )

    def test_b_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Grape"]["properties"]["public"][1]["name"], "b"
        )

    def test_b_type(self):
        self.assertEqual(
            self.cppHeader.classes["Grape"]["properties"]["public"][1]["type"], "int"
        )

    def test_c_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Grape"]["properties"]["public"][2]["name"], "c"
        )

    def test_d_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Grape"]["properties"]["public"][3]["name"], "d"
        )

    def test_e_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Grape"]["properties"]["public"][4]["name"], "e"
        )

    def test_f_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Grape"]["properties"]["public"][5]["name"], "f"
        )


# Bug BitBucket #14
class Avacado_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_Avacado_exists(self):
        self.assertEqual("Avacado" in self.cppHeader.classes, True)

    def test_foo_return_type(self):
        self.assertEqual(
            self.cppHeader.classes["Avacado"]["methods"]["public"][0]["returns"],
            "uint8_t",
        )

    def test_bar_return_type(self):
        self.assertEqual(
            self.cppHeader.classes["Avacado"]["methods"]["public"][1]["returns"],
            "::uint8_t",
        )


# Bug BitBucket #13
class Raspberry_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_anon_struct_1_exists(self):
        self.assertEqual("<anon-struct-5>" in self.cppHeader.classes, True)

    def test_beta_exists(self):
        self.assertEqual(
            self.cppHeader.classes["<anon-struct-5>"]["properties"]["public"][0][
                "name"
            ],
            "anon_struct_variable",
        )

    def test_Raspberry_exists(self):
        self.assertEqual("Raspberry" in self.cppHeader.classes, True)

    def test_a_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Raspberry"]["properties"]["public"][0]["name"], "a"
        )


# Bug BitBucket #15 & 16
class Hen_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_default_a(self):
        self.assertEqual(
            self.cppHeader.classes["Hen"]["methods"]["public"][0]["parameters"][0][
                "defaultValue"
            ],
            "100",
        )

    def test_default_b(self):
        self.assertEqual(
            self.cppHeader.classes["Hen"]["methods"]["public"][0]["parameters"][1][
                "defaultValue"
            ],
            "0xfd",
        )

    def test_default_c(self):
        self.assertEqual(
            self.cppHeader.classes["Hen"]["methods"]["public"][0]["parameters"][2][
                "defaultValue"
            ],
            "1.7e-3",
        )

    def test_default_d(self):
        self.assertEqual(
            self.cppHeader.classes["Hen"]["methods"]["public"][0]["parameters"][3][
                "defaultValue"
            ],
            "3.14",
        )

    def test_default_s1(self):
        self.assertEqual(
            self.cppHeader.classes["Hen"]["methods"]["public"][1]["parameters"][0][
                "defaultValue"
            ],
            '""',
        )

    def test_default_s2(self):
        self.assertEqual(
            self.cppHeader.classes["Hen"]["methods"]["public"][1]["parameters"][1][
                "defaultValue"
            ],
            '"nothing"',
        )


# Bug BitBucket #19
class Raddish_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_Avacado_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Raddish_SetIterator"]["properties"]["protected"][0][
                "name"
            ],
            "_beg",
        )

    def test_class_template(self):
        template_str = "template<typename VALUE, typename VALUE_SET_ITERATOR, typename ACCESOR=Raddish::SimpleAccessor<VALUE, VALUE_SET_ITERATOR>>"
        self.assertEqual(
            self.cppHeader.classes["Raddish_SetIterator"]["template"], template_str
        )


# Bug bug 57
class Carambola_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(self.cppHeader.enums[2]["name"], "Carambola")

    def test_values(self):
        self.assertEqual(
            self.cppHeader.enums[2]["values"],
            [{"name": "StarFruit", "value": "( 2 + 2 ) / 2"}],
        )

    def test_typedef(self):
        self.assertEqual(self.cppHeader.enums[2]["typedef"], True)


# globals
class Globals_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_externVar_name(self):
        self.assertEqual(self.cppHeader.variables[2]["name"], "externVar")

    def test_externVar_extern(self):
        self.assertEqual(self.cppHeader.variables[2]["extern"], 1)

    def test_globalVar_name(self):
        self.assertEqual(self.cppHeader.variables[3]["name"], "globalVar")

    def test_globalVar_extern(self):
        self.assertEqual(self.cppHeader.variables[3]["extern"], 0)


# globals
class TypedefArray_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual("TenCharArray[10]" in self.cppHeader.typedefs, True)

    def test_value(self):
        self.assertEqual(self.cppHeader.typedefs["TenCharArray[10]"], "char")


# typedef structs
class TypedefStruct_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual("MAGIC_FILE" in self.cppHeader.typedefs, True)

    def test_value(self):
        self.assertEqual(
            self.cppHeader.typedefs["MAGIC_FILE"], "struct SUPER_MAGIC_FILE"
        )


# Bug SourceForge #10
class Picture_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_array_size(self):
        self.assertEqual(
            self.cppHeader.classes["Picture"]["properties"]["public"][1]["array_size"],
            16384,
        )

    def test_multi_dimensional_array_size(self):
        self.assertEqual(
            self.cppHeader.classes["Picture"]["properties"]["public"][1][
                "multi_dimensional_array_size"
            ],
            "128x128",
        )


# SourceForge bug 58
class Apricot_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_Apricot_exists(self):
        self.assertEqual("Apricot" in self.cppHeader.classes, True)

    def test_i_exists(self):
        self.assertEqual(self.cppHeader.classes["Apricot"]["members"][0]["name"], "i")

    def test_f_exists(self):
        self.assertEqual(self.cppHeader.classes["Apricot"]["members"][1]["name"], "f")

    def test_s_exists(self):
        self.assertEqual(self.cppHeader.classes["Apricot"]["members"][2]["name"], "s")


# SourceForge bug 59
class LemonLime_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_lemon_not_final(self):
        self.assertEqual(self.cppHeader.classes["Lemon"]["final"], False)

    def test_lime_final(self):
        self.assertEqual(self.cppHeader.classes["Lime"]["final"], True)

    def test_lemon_foo_is_final(self):
        self.assertEqual(
            self.cppHeader.classes["Lemon"]["methods"]["public"][0]["final"], True
        )

    def test_lemon_foo2_is_not_final(self):
        self.assertEqual(
            self.cppHeader.classes["Lemon"]["methods"]["public"][1]["final"], False
        )

    def test_lime_abc_is_not_override(self):
        self.assertEqual(
            self.cppHeader.classes["Lime"]["methods"]["public"][0]["override"], False
        )

    def test_lime_foo2_is_not_override(self):
        self.assertEqual(
            self.cppHeader.classes["Lime"]["methods"]["public"][1]["override"], True
        )


class JSON_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            r"""
struct Lemon
{
    virtual void foo() final;
    virtual void foo2();
};
 
struct Lime final : Lemon
{
    void abc();
    void foo2() override;
};""",
            "string",
        )
        self.jsonString = self.cppHeader.toJSON()

    def test_hasLemon(self):
        hasString = '        "Lemon": {' in self.jsonString
        self.assertEqual(hasString, True)

    def test_can_parse_complex_file(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
        j = self.cppHeader.toJSON()


# BitBucket bug 24
class Mouse_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_MouseClass_exists(self):
        self.assertEqual("MouseClass" in self.cppHeader.classes, True)

    def test_mouse_typedef_correct_value(self):
        self.assertEqual(
            self.cppHeader.classes["MouseClass"]["methods"]["public"][0]["parameters"][
                0
            ]["raw_type"],
            "MouseNS::MouseClass::mouse_typedef",
        )


# BitBucket bug 26
class Fig_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_Fig_exists(self):
        self.assertEqual("Fig" in self.cppHeader.classes, True)

    def test_a_exists(self):
        self.assertEqual(
            self.cppHeader.classes["Grape"]["properties"]["public"][0]["name"], "a"
        )


# BitBucket bug 27
class Olive_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_Olive_exists(self):
        self.assertEqual("olive" in self.cppHeader.classes, True)

    def test_union_member_x(self):
        cmp_values = {
            "constant": 0,
            "name": "x",
            "reference": 0,
            "type": "int",
            "static": 0,
            "pointer": 0,
        }
        self.assertEqual(
            filter_dict_keys(
                self.cppHeader.classes["olive"]["members"][0], cmp_values.keys()
            ),
            cmp_values,
        )


# BitBucket bug 61
class Beet_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_Beet_exists(self):
        self.assertEqual("BeetStruct" in self.cppHeader.classes, True)

    def test_BeetEnum_exists(self):
        self.assertEqual(
            self.cppHeader.classes["BeetStruct"]["enums"]["public"][0]["name"],
            "BeetEnum",
        )


# BitBucket bug 40
class set_callback_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_set_callback(self):
        self.assertEqual(self.cppHeader.functions[8]["name"], "set_callback")
        self.assertEqual(
            self.cppHeader.functions[8]["parameters"][1]["name"], "callback"
        )
        self.assertEqual(
            self.cppHeader.functions[8]["parameters"][1]["function_pointer"], 1
        )
        self.assertEqual(
            self.cppHeader.functions[8]["parameters"][1]["type"],
            "long ( * ) ( struct test_st *, int, const char *, int long, long, long )",
        )


# BitBucket bug 45
class HALControlWord_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """\
            struct HAL_ControlWord {
                int x : 1;
                int y : 1;
            };
            typedef struct HAL_ControlWord HAL_ControlWord;
            int HAL_GetControlWord(HAL_ControlWord* controlWord);
        """,
            "string",
        )

    def test_functions(self):
        self.assertEqual(len(self.cppHeader.functions), 1)
        self.assertEqual(self.cppHeader.functions[0]["name"], "HAL_GetControlWord")

    def test_classes(self):
        self.assertEqual(len(self.cppHeader.classes), 1)
        self.assertEqual(
            self.cppHeader.classes["HAL_ControlWord"]["name"], "HAL_ControlWord"
        )

    def test_num_typedefs(self):
        self.assertEqual(len(self.cppHeader.typedefs), 1)
        self.assertEqual(
            self.cppHeader.typedefs["HAL_ControlWord"], "struct HAL_ControlWord"
        )


# Bitbucket bug 47
class CommentEOF_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
namespace a {
}  // namespace a""",
            "string",
        )

    def test_comment(self):
        self.assertTrue("a" in self.cppHeader.namespaces)


# BitBucket bug 35
class Grackle_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_Grackle_exists(self):
        self.assertEqual("Grackle" in self.cppHeader.classes, True)

    def test_Grackle_no_noexcept_None(self):
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][0]["noexcept"], None
        )

    def test_Grackle_noexcept(self):
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][1]["noexcept"],
            "noexcept",
        )

    def test_Grackle_const_noexcept(self):
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][2]["const"], True
        )
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][2]["noexcept"],
            "noexcept",
        )

    def test_Grackle_noexcept_true(self):
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][3]["noexcept"],
            "noexcept(true)",
        )

    def test_Grackle_const_noexcept_true(self):
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][4]["const"], True
        )
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][4]["noexcept"],
            "noexcept(true)",
        )

    def test_Grackle_noexcept_noexcept_operator(self):
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][5]["noexcept"],
            "noexcept(noexcept(Grackle()))",
        )

    def test_Grackle_const_noexcept_noexcept_operator(self):
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][6]["const"], True
        )
        self.assertEqual(
            self.cppHeader.classes["Grackle"]["methods"]["public"][6]["noexcept"],
            "noexcept(noexcept(Grackle()))",
        )


# Test enhancement 13 (default constructor / destructor)
class DefaultConstDest_TestCase:
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_DefaultConstDest_exists(self):
        self.assertEqual("DefaultConstDest" in self.cppHeader.classes, True)
        self.assertEqual("default_class_tricky" in self.cppHeader.classes, True)

    def test_DefaultConstDest_constructor_default(self):
        self.assertEqual(
            self.cppHeader.classes["DefaultConstDest"]["methods"]["public"][0][
                "constructor"
            ],
            True,
        )
        self.assertEqual(
            self.cppHeader.classes["DefaultConstDest"]["methods"]["public"][0][
                "default"
            ],
            True,
        )
        self.assertEqual(
            self.cppHeader.classes["DefaultConstDest"]["methods"]["public"][0][
                "defined"
            ],
            True,
        )

    def test_DefaultConstDest_destructor_default(self):
        self.assertEqual(
            self.cppHeader.classes["DefaultConstDest"]["methods"]["public"][1][
                "destructor"
            ],
            True,
        )
        self.assertEqual(
            self.cppHeader.classes["DefaultConstDest"]["methods"]["public"][1][
                "default"
            ],
            True,
        )
        self.assertEqual(
            self.cppHeader.classes["DefaultConstDest"]["methods"]["public"][1][
                "defined"
            ],
            True,
        )

    def test_DefaultConstDest_default_edgeCaseNaming(self):
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][0][
                "constructor"
            ],
            True,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][0][
                "default"
            ],
            False,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][0][
                "defined"
            ],
            False,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][1][
                "destructor"
            ],
            True,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][1][
                "default"
            ],
            False,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][1][
                "defined"
            ],
            False,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][2][
                "name"
            ],
            "randomMethod1_default",
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][2][
                "destructor"
            ],
            False,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][2][
                "default"
            ],
            False,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][2][
                "defined"
            ],
            False,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][3][
                "name"
            ],
            "defaultrandomMethod2",
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][3][
                "destructor"
            ],
            False,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][3][
                "default"
            ],
            False,
        )
        self.assertEqual(
            self.cppHeader.classes["default_class_tricky"]["methods"]["public"][3][
                "defined"
            ],
            False,
        )


class VarargFunc_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_vararg_func(self):
        vf = next(x for x in self.cppHeader.functions if x["name"] == "vararg_func")
        nvf = next(
            x for x in self.cppHeader.functions if x["name"] == "non_vararg_func"
        )
        self.assertTrue(vf["vararg"])
        self.assertFalse(nvf["vararg"])
        self.assertEqual(len(vf["parameters"]), len(nvf["parameters"]))


class UsingNamespace_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
using std::thing;
using MyThing = SomeThing;
namespace a {
    using std::string;
    using VoidFunction = std::function<void()>;

    void fn(string &s, VoidFunction fn, thing * t);

    class A : public B {
    public:
        using B::B;
        using IntFunction = std::function<int()>;

        void a(string &s, IntFunction fn, thing * t);
    };
}
""",
            "string",
        )

    def test_using(self):
        self.assertEqual(len(self.cppHeader.using), 4)

        self.assertEqual(
            filter_pameters(
                [self.cppHeader.using["a::string"]],
                extra=["using_type", "raw_type", "namespace"],
            ),
            [
                {
                    "desc": None,
                    "name": "",
                    "namespace": "std::",
                    "raw_type": "std::string",
                    "type": "string",
                    "using_type": "declaration",
                }
            ],
        )

        self.assertEqual(
            filter_pameters(
                [self.cppHeader.using["a::VoidFunction"]],
                extra=["using_type", "raw_type", "namespace", "typealias"],
            ),
            [
                {
                    "desc": None,
                    "name": "",
                    "namespace": "std::",
                    "raw_type": "std::function<void ( )>",
                    "type": "function<void ( )>",
                    "typealias": "VoidFunction",
                    "using_type": "typealias",
                }
            ],
        )

        self.assertEqual(
            filter_pameters(
                [self.cppHeader.using["thing"]],
                extra=["using_type", "raw_type", "namespace"],
            ),
            [
                {
                    "desc": None,
                    "name": "",
                    "namespace": "std::",
                    "raw_type": "std::thing",
                    "type": "thing",
                    "using_type": "declaration",
                }
            ],
        )

        self.assertEqual(
            filter_pameters(
                [self.cppHeader.using["MyThing"]],
                extra=["using_type", "raw_type", "namespace", "typealias"],
            ),
            [
                {
                    "desc": None,
                    "name": "",
                    "namespace": "",
                    "raw_type": "SomeThing",
                    "type": "SomeThing",
                    "typealias": "MyThing",
                    "using_type": "typealias",
                }
            ],
        )

    def test_fn(self):
        self.assertEqual(len(self.cppHeader.functions), 1)
        fn = self.cppHeader.functions[0]
        self.assertEqual(fn["name"], "fn")
        self.assertEqual(
            filter_pameters(fn["parameters"], ["namespace", "raw_type"]),
            [
                {
                    "type": "string",
                    "name": "s",
                    "desc": None,
                    "namespace": "std::",
                    "raw_type": "std::string",
                },
                {
                    "type": "function<void ( )>",
                    "name": "fn",
                    "desc": None,
                    "namespace": "std::",
                    "raw_type": "std::function<void ( )>",
                },
                {
                    "type": "thing",
                    "name": "t",
                    "desc": None,
                    "namespace": "std::",
                    "raw_type": "std::thing",
                },
            ],
        )

    def test_class(self):
        c = self.cppHeader.classes["A"]

        self.assertEqual(len(c["using"]), 2)
        self.assertIn("B", c["using"])
        self.assertIn("IntFunction", c["using"])

        self.assertEqual(len(c["methods"]["public"]), 1)
        fn = c["methods"]["public"][0]
        self.assertEqual(fn["name"], "a")
        self.assertEqual(
            filter_pameters(fn["parameters"], ["namespace", "raw_type"]),
            [
                {
                    "type": "string",
                    "name": "s",
                    "desc": None,
                    "namespace": "std::",
                    "raw_type": "std::string",
                },
                {
                    "type": "function<int ( )>",
                    "name": "fn",
                    "desc": None,
                    "namespace": "std::",
                    "raw_type": "std::function<int ( )>",
                },
                {
                    "type": "thing",
                    "name": "t",
                    "desc": None,
                    "namespace": "std::",
                    "raw_type": "std::thing",
                },
            ],
        )


class StaticFn_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
class A {
    static int fn();
};
""",
            "string",
        )

    def test_fn(self):
        m = self.cppHeader.classes["A"]["methods"]["private"][0]
        self.assertEqual(m["static"], True)
        self.assertEqual(m["rtnType"], "int")


class ConstExpr_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
class A {
    static constexpr double kThing = 0.02;
};
""",
            "string",
        )

    def test_fn(self):
        p = self.cppHeader.classes["A"]["properties"]["private"][0]
        self.assertEqual(p["static"], 1)
        self.assertEqual(p["constexpr"], 1)
        self.assertEqual(p["raw_type"], "double")
        self.assertEqual(p["defaultValue"], "0.02")


class DefaultEnum_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
class A {
    enum {
        v1,
        v2,
    } m_v1 = v1;

    enum {
        vv1,
        vv2, vv3
    } m_v2 = vv2, m_v3 = vv3;
};
""",
            "string",
        )

    def test_fn(self):
        p = self.cppHeader.classes["A"]["properties"]["private"][0]
        self.assertEqual("enum", p["type"])
        self.assertEqual("m_v1", p["name"])
        self.assertEqual("v1", p["default"])
        self.assertEqual(
            p.get("enum_type", {}).get("values"),
            [{"name": "v1", "value": 0}, {"name": "v2", "value": 1}],
        )

        p = self.cppHeader.classes["A"]["properties"]["private"][1]
        self.assertEqual("enum", p["type"])
        self.assertEqual("m_v2", p["name"])
        self.assertEqual("vv2", p["default"])
        self.assertEqual(
            p.get("enum_type", {}).get("values"),
            [
                {"name": "vv1", "value": 0},
                {"name": "vv2", "value": 1},
                {"name": "vv3", "value": 2},
            ],
        )

        p = self.cppHeader.classes["A"]["properties"]["private"][2]
        self.assertEqual("enum", p["type"])
        self.assertEqual("m_v3", p["name"])
        self.assertEqual("vv3", p["default"])
        self.assertEqual(
            p.get("enum_type", {}).get("values"),
            [
                {"name": "vv1", "value": 0},
                {"name": "vv2", "value": 1},
                {"name": "vv3", "value": 2},
            ],
        )


class MultiFile_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
#line 3 "child.h"
#include <stdint.h>
#line 3 "base.h"
void functionInBase(void);

class Base
{
public:
    virtual void baseFunction();
};
#line 7 "child.h"
void functionInChild(void);

class Child : public Base
{
public:
    void childOnlyFunction();
    void baseFunction() override;
};

""",
            "string",
        )

    def assertLocation(self, thing, fname, lineno):
        self.assertEqual(fname, thing["filename"])
        self.assertEqual(lineno, thing["line_number"])

    def test_fn(self):
        baseFn = self.cppHeader.functions[0]
        self.assertEqual("functionInBase", baseFn["name"])
        self.assertLocation(baseFn, "base.h", 3)

        base = self.cppHeader.classes["Base"]
        self.assertLocation(base, "base.h", 5)

        childFn = self.cppHeader.functions[1]
        self.assertEqual("functionInChild", childFn["name"])
        self.assertLocation(childFn, "child.h", 7)

        child = self.cppHeader.classes["Child"]
        self.assertLocation(child, "child.h", 9)


class TemplateMadness_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
template <typename Type>
class XYZ : public MyBaseClass<Type, int>
{
    public:
    XYZ();
};

template <typename ValueT, typename... IterTs>
class concat_iterator
    : public iterator_facade_base<concat_iterator<ValueT, IterTs...>,
                                  std::forward_iterator_tag, ValueT> {
};

template <std::size_t N, std::size_t... I>
struct build_index_impl : build_index_impl<N - 1, N - 1, I...> {};

template <std::size_t... I>
struct build_index_impl<0, I...> : index_sequence<I...> {};

//template <typename F, typename P, typename... T>
//struct is_callable<F, P, typelist<T...>,
//        void_t<decltype(((*std::declval<P>()).*std::declval<F>())(std::declval<T>()...))>>
//    : std::true_type {};

template <typename T...>
struct S : public T... {};

""",
            "string",
        )

    def testXYZ(self):
        c = self.cppHeader.classes["XYZ"]
        self.assertEqual("XYZ", c["name"])
        self.assertEqual(
            [
                {
                    "access": "public",
                    "class": "MyBaseClass<Type,int>",
                    "decltype": False,
                    "decl_name": "MyBaseClass",
                    "decl_params": [
                        {"param": "Type", "...": False, "decltype": False},
                        {"param": "int", "...": False, "decltype": False},
                    ],
                    "virtual": False,
                    "...": False,
                }
            ],
            c["inherits"],
        )

    def testConcatIterator(self):
        c = self.cppHeader.classes["concat_iterator"]
        self.assertEqual("concat_iterator", c["name"])
        self.assertEqual(
            [
                {
                    "access": "public",
                    "class": "iterator_facade_base<concat_iterator<ValueT,IterTs...>,std::forward_iterator_tag,ValueT>",
                    "decltype": False,
                    "decl_name": "iterator_facade_base",
                    "decl_params": [
                        {
                            "decltype": False,
                            "param": "concat_iterator",
                            "params": [
                                {"param": "ValueT", "...": False, "decltype": False},
                                {"param": "IterTs", "...": True, "decltype": False},
                            ],
                            "...": False,
                        },
                        {
                            "decltype": False,
                            "param": "std::forward_iterator_tag",
                            "...": False,
                        },
                        {"decltype": False, "param": "ValueT", "...": False},
                    ],
                    "virtual": False,
                    "...": False,
                }
            ],
            c["inherits"],
        )

    def testBuildIndexImpl1(self):
        c = self.cppHeader.classes["build_index_impl"]
        self.assertEqual("build_index_impl", c["name"])
        self.assertEqual(
            [
                {
                    "access": "public",
                    "class": "build_index_impl<N-1,N-1,I...>",
                    "decltype": False,
                    "decl_name": "build_index_impl",
                    "decl_params": [
                        {"param": "N-1", "...": False, "decltype": False},
                        {"param": "N-1", "...": False, "decltype": False},
                        {"param": "I", "...": True, "decltype": False},
                    ],
                    "virtual": False,
                    "...": False,
                }
            ],
            c["inherits"],
        )

    def testBuildIndexImpl2(self):
        c = self.cppHeader.classes["build_index_impl<0,I...>"]
        self.assertEqual("build_index_impl", c["bare_name"])
        self.assertEqual("build_index_impl<0,I...>", c["name"])
        self.assertEqual(
            [
                {"decltype": False, "param": "0", "...": False},
                {"decltype": False, "param": "I", "...": True},
            ],
            c["class_params"],
        )
        self.assertEqual(
            [
                {
                    "access": "public",
                    "class": "index_sequence<I...>",
                    "decltype": False,
                    "decl_name": "index_sequence",
                    "decl_params": [{"decltype": False, "param": "I", "...": True}],
                    "virtual": False,
                    "...": False,
                }
            ],
            c["inherits"],
        )

    # def testIsCallable(self):
    #     c = self.cppHeader.classes["is_callable"]
    #     self.assertEqual("is_callable", c["name"])
    #     self.assertEqual(
    #         [
    #             {"param": "F", "...": False, "decltype": False},
    #             {"param": "P", "...": False, "decltype": False},
    #             {
    #                 "param": "typelist",
    #                 "...": False,
    #                 "decltype": False,
    #                 "params": [{"param": "T", "...": True, "decltype": False},],
    #             },
    #             {
    #                 "param": "void_t",
    #                 "...": False,
    #                 "decltype": False,
    #                 "params": [
    #                     {
    #                         "param": "(((*std::declval<P>()).*std::declval<F>())(std::declval<T>()...))",
    #                         "...": False,
    #                         "decltype": True,
    #                     },
    #                 ],
    #             },
    #         ],
    #         c["class_params"],
    #     )
    #     self.assertEqual(
    #         [{"access": "private", "class": "std::true_type", "virtual": False,}],
    #         c["inherits"],
    #     )

    def testS(self):
        c = self.cppHeader.classes["S"]
        self.assertEqual("S", c["name"])
        self.assertEqual(
            [
                {
                    "access": "public",
                    "class": "T...",
                    "decl_name": "T",
                    "virtual": False,
                    "...": True,
                    "decltype": False,
                }
            ],
            c["inherits"],
        )


class Attributes_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """

struct [[deprecated]] S {};
[[deprecated]] typedef S* PS;

[[deprecated]] int x;
union U { [[deprecated]] int n; };
[[deprecated]] void f();

enum [[deprecated]] E { A [[deprecated]], B [[deprecated]] = 42 };

struct alignas(8) AS {};

""",
            "string",
        )

    def test_existance(self):

        self.assertIn("S", self.cppHeader.classes)
        self.assertIn("PS", self.cppHeader.typedefs)
        self.assertEqual("x", self.cppHeader.variables[0]["name"])
        self.assertEqual("f", self.cppHeader.functions[0]["name"])
        self.assertIn("AS", self.cppHeader.classes)


class EnumWithTemplates_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
enum {
    IsRandomAccess = std::is_base_of<std::random_access_iterator_tag,
                                     IteratorCategoryT>::value,
    IsBidirectional = std::is_base_of<std::bidirectional_iterator_tag,
                                      IteratorCategoryT>::value,
  };
""",
            "string",
        )

    def test_values(self):
        e = self.cppHeader.enums[0]
        v0 = e["values"][0]
        self.assertEqual(
            v0["value"],
            "std :: is_base_of < std :: random_access_iterator_tag , IteratorCategoryT > :: value",
        )

        v1 = e["values"][1]
        self.assertEqual(
            v1["value"],
            "std :: is_base_of < std :: bidirectional_iterator_tag , IteratorCategoryT > :: value",
        )


class FreeTemplates_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """

template <typename Allocator>
StringRef copy(Allocator &A) const {
  // Don't request a length 0 copy from the allocator.
  if (empty())
    return StringRef();
  char *S = A.template Allocate<char>(Length);
  std::copy(begin(), end(), S);
  return StringRef(S, Length);
}

""",
            "string",
        )

    def test_fn(self):
        fn = self.cppHeader.functions[0]
        self.assertEqual("copy", fn["name"])


class MessedUpDoxygen_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """

/// fn comment
void
fn();

/// var comment
int
v1 = 0;

int
v2 = 0; /// var2 comment

/// cls comment
class
C {};

/// template comment
template <typename T>
class
C2 {};

""",
            "string",
        )

    def test_fn(self):
        fn = self.cppHeader.functions[0]
        self.assertEqual("fn", fn["name"])
        self.assertEqual("/// fn comment", fn["doxygen"])

    def test_var1(self):
        v = self.cppHeader.variables[0]
        self.assertEqual("v1", v["name"])
        self.assertEqual("/// var comment", v["doxygen"])

    def test_var2(self):
        v = self.cppHeader.variables[1]
        self.assertEqual("v2", v["name"])
        self.assertEqual("/// var2 comment", v["doxygen"])

    def test_cls(self):
        c = self.cppHeader.classes["C"]
        self.assertEqual("C", c["name"])
        self.assertEqual("/// cls comment", c["doxygen"])

    def test_cls2(self):
        c = self.cppHeader.classes["C2"]
        self.assertEqual("C2", c["name"])
        self.assertEqual("/// template comment", c["doxygen"])


class EnumParameter_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
enum E {
  VALUE,
};

void fn_with_enum_param1(const enum E e);

void fn_with_enum_param2(const enum E e) {
  // code here
}

enum E fn_with_enum_retval1(void);

enum E fn_with_enum_retval2(void) {
  // code here
}

""",
            "string",
        )

    def test_enum_param(self):
        fn = self.cppHeader.functions[0]
        self.assertEqual("fn_with_enum_param1", fn["name"])
        self.assertEqual(1, len(fn["parameters"]))

        p1 = fn["parameters"][0]
        self.assertEqual("e", p1["name"])
        self.assertEqual("const enum E", p1["type"])
        self.assertEqual("int", p1["raw_type"])

        fn = self.cppHeader.functions[1]
        self.assertEqual("fn_with_enum_param2", fn["name"])
        self.assertEqual(1, len(fn["parameters"]))

        p1 = fn["parameters"][0]
        self.assertEqual("e", p1["name"])
        self.assertEqual("const enum E", p1["type"])
        self.assertEqual("int", p1["raw_type"])

    def test_enum_retval(self):
        fn = self.cppHeader.functions[2]
        self.assertEqual("fn_with_enum_retval1", fn["name"])
        self.assertEqual(0, len(fn["parameters"]))
        self.assertEqual("enum E", fn["rtnType"])

        fn = self.cppHeader.functions[3]
        self.assertEqual("fn_with_enum_retval2", fn["name"])
        self.assertEqual(0, len(fn["parameters"]))
        self.assertEqual("enum E", fn["rtnType"])


class StaticAssert_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
static_assert(sizeof(int) == 4, 
              "integer size is wrong"
              "for some reason");
""",
            "string",
        )

    def test_nothing(self):
        self.assertEqual(self.cppHeader.functions, [])


class InitializerWithInitializerList_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
struct ComplexInit : SomeBase {
  ComplexInit(int i) :
    m_stuff{i,2}
  {
    auto i = something();
  }

  void fn();
  
  std::vector<int> m_stuff;
};

template <typename T>
class future final {
public:
  template <typename R>
  future(future<R>&& oth) noexcept
      : future(oth.then([](R&& val) -> T { return val; })) {}
};


""",
            "string",
        )

    def test_cls_props(self):
        c = self.cppHeader.classes["ComplexInit"]
        self.assertEqual(2, len(c["methods"]["public"]))
        self.assertEqual(0, len(c["methods"]["private"]))
        self.assertEqual(0, len(c["methods"]["private"]))
        self.assertEqual(1, len(c["properties"]["public"]))
        self.assertEqual(0, len(c["properties"]["private"]))
        self.assertEqual(0, len(c["properties"]["protected"]))

        self.assertEqual(c["methods"]["public"][0]["name"], "ComplexInit")
        self.assertEqual(c["methods"]["public"][1]["name"], "fn")

        self.assertEqual(c["properties"]["public"][0]["name"], "m_stuff")

    def test_future(self):
        c = self.cppHeader.classes["future"]
        self.assertEqual(1, len(c["methods"]["public"]))
        self.assertEqual(0, len(c["methods"]["private"]))
        self.assertEqual(0, len(c["methods"]["private"]))
        self.assertEqual(0, len(c["properties"]["public"]))
        self.assertEqual(0, len(c["properties"]["private"]))
        self.assertEqual(0, len(c["properties"]["protected"]))
        self.assertEqual(c["methods"]["public"][0]["name"], "future")


class EnumClass_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
enum class MyEnum {
    V = 1
};

""",
            "string",
        )

    def test_enum(self):
        self.assertEqual(self.cppHeader.classes, {})
        self.assertEqual(len(self.cppHeader.enums), 1)
        e = self.cppHeader.enums[0]

        self.assertEqual(e["name"], "MyEnum")
        self.assertEqual(
            e["values"], [{"name": "V", "value": 1}],
        )


class NestedResolving_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
struct A {

    enum { ANON };

    struct B {};
    enum C { X };

    B fnested(B b);
    C fenum(C c);
};

""",
            "string",
        )

    def test_nothing(self):
        c = self.cppHeader.classes["A"]
        fn = c["methods"]["public"][0]
        self.assertEqual(fn["name"], "fnested")
        self.assertEqual(fn["rtnType"], "A::B")
        self.assertEqual(len(fn["parameters"]), 1)
        self.assertEqual(fn["parameters"][0]["raw_type"], "A::B")

        fn = c["methods"]["public"][1]
        self.assertEqual(fn["name"], "fenum")
        self.assertEqual(fn["rtnType"], "A::C")
        self.assertEqual(len(fn["parameters"]), 1)
        self.assertEqual(fn["parameters"][0]["enum"], "A::C")


class EnumCrash_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
enum HAL_Type {
  HAL_UNASSIGNED = 0,
};

struct HAL_Value {
  union {
    HAL_Bool v_boolean;
  } data;
  enum HAL_Type type;
};

""",
            "string",
        )

    def test_nothing(self):
        pass


class ExternInline_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
extern "C++" {
inline HAL_Value HAL_GetSimValue(HAL_SimValueHandle handle) {
  HAL_Value v;
  return v;
}
}  // extern "C++"

""",
            "string",
        )

    def test_fn(self):
        self.assertEqual(self.cppHeader.variables, [])
        self.assertEqual(len(self.cppHeader.functions), 1)
        fn = self.cppHeader.functions[0]
        self.assertEqual(fn["name"], "HAL_GetSimValue")
        self.assertEqual(
            filter_pameters(fn["parameters"], ["namespace", "raw_type"]),
            [
                {
                    "type": "HAL_SimValueHandle",
                    "name": "handle",
                    "desc": None,
                    "namespace": "",
                    "raw_type": "HAL_SimValueHandle",
                },
            ],
        )
        self.assertEqual(fn["rtnType"], "HAL_Value")


class PointerTemplate_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """

std::vector<Pointer*> * fn(std::vector<Pointer*> * ps);

""",
            "string",
        )

    def test_fn(self):
        self.assertEqual(len(self.cppHeader.functions), 1)
        fn = self.cppHeader.functions[0]
        self.assertEqual(fn["name"], "fn")
        self.assertEqual(
            filter_pameters(fn["parameters"], ["namespace", "raw_type"]),
            [
                {
                    "type": "std::vector<Pointer *> *",
                    "name": "ps",
                    "desc": None,
                    "namespace": None,
                    "raw_type": "std::vector<Pointer *>",
                },
            ],
        )
        self.assertEqual(fn["rtnType"], "std::vector<Pointer *> *")


class ParamWithInitializer_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
template <typename T, typename U>
void fn(something<T, U> s = something<T, U>{1,2,3});
""",
            "string",
        )

    def test_fn(self):
        self.assertEqual(len(self.cppHeader.functions), 1)
        fn = self.cppHeader.functions[0]
        self.assertEqual(fn["name"], "fn")
        self.assertEqual(
            filter_pameters(fn["parameters"], ["namespace", "raw_type", "default"]),
            [
                {
                    "type": "something<T, U >",
                    "name": "s",
                    "desc": None,
                    "namespace": "",
                    "raw_type": "something<T, U >",
                    "default": "something<T, U>{ 1, 2, 3}",
                },
            ],
        )
        self.assertEqual(fn["rtnType"], "void")


class NestedClassAccess_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
class Outer {
    struct Inner {
        void fn();
    };

    void ofn();
};
""",
            "string",
        )

    def test_fn(self):
        self.assertEqual(len(self.cppHeader.functions), 0)

        outer = self.cppHeader.classes["Outer"]
        self.assertEqual(outer["parent"], None)

        self.assertEqual(0, len(outer["methods"]["public"]))
        self.assertEqual(0, len(outer["methods"]["protected"]))
        self.assertEqual(1, len(outer["methods"]["private"]))
        self.assertEqual("ofn", outer["methods"]["private"][0]["name"])

        inner = self.cppHeader.classes["Outer::Inner"]
        self.assertIs(inner["parent"], outer)
        self.assertEqual(inner["access_in_parent"], "private")

        self.assertEqual(1, len(inner["methods"]["public"]))
        self.assertEqual(0, len(inner["methods"]["protected"]))
        self.assertEqual(0, len(inner["methods"]["private"]))
        self.assertEqual("fn", inner["methods"]["public"][0]["name"])


class AnonUnion_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
struct Outer {
    union {
        int x;
        int y;
    };
    int z;
};
""",
            "string",
        )

    def test_fn(self):
        self.assertEqual(len(self.cppHeader.functions), 0)

        outer = self.cppHeader.classes["Outer"]
        self.assertEqual(outer["parent"], None)

        inner = self.cppHeader.classes["Outer::<anon-union-1>"]
        self.assertIs(inner["parent"], outer)

        self.assertEqual(2, len(outer["properties"]["public"]))
        self.assertEqual(0, len(outer["properties"]["protected"]))
        self.assertEqual(0, len(outer["properties"]["private"]))

        props = outer["properties"]["public"]
        self.assertEqual(props[0]["name"], "")
        self.assertEqual(props[1]["name"], "z")

        self.assertEqual(2, len(outer["properties"]["public"]))
        self.assertEqual(0, len(outer["properties"]["protected"]))
        self.assertEqual(0, len(outer["properties"]["private"]))

        props = inner["properties"]["public"]
        self.assertEqual(props[0]["name"], "x")
        self.assertEqual(props[1]["name"], "y")


class Deleted_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
class A {
public:
    A() = delete;
};
""",
            "string",
        )

    def test_fn(self):
        m = self.cppHeader.classes["A"]["methods"]["public"][0]
        self.assertEqual(m["constructor"], True)
        self.assertEqual(m["deleted"], True)


class BaseTemplateNs_TestCase(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
class A : public B<int, int>::C {};
""",
            "string",
        )

    def test_fn(self):
        c = self.cppHeader.classes["A"]
        self.assertEqual("A", c["name"])
        self.assertEqual(
            [
                {
                    "access": "public",
                    "class": "B<int,int>::C",
                    "decl_name": "B<int,int>::C",
                    "virtual": False,
                    "...": False,
                    "decltype": False,
                }
            ],
            c["inherits"],
        )


class NestedTypedef(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
template <class SomeType> class A {
 public:
  typedef B <SomeType> C;
  
  A();

 protected:
  C aCInstance;
};
""",
            "string",
        )

    def test_fn(self):
        c = self.cppHeader.classes["A"]
        self.assertEqual("A", c["name"])

        self.assertEqual(0, len(c["properties"]["public"]))
        self.assertEqual(1, len(c["properties"]["protected"]))
        self.assertEqual(0, len(c["properties"]["private"]))

        c = c["properties"]["protected"][0]
        self.assertEqual(c["name"], "aCInstance")
        self.assertEqual(c["type"], "C")


class MoreTypedef(unittest.TestCase):
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(
            """
typedef C A;

class B {
public:
  A aMethod();
};
""",
            "string",
        )

    def test_fn(self):
        c = self.cppHeader.classes["B"]
        self.assertEqual("B", c["name"])

        m = c["methods"]["public"][0]
        self.assertEqual(m["name"], "aMethod")
        self.assertEqual(m["rtnType"], "A")

        self.assertEqual(self.cppHeader.typedefs["A"], "C")


if __name__ == "__main__":
    unittest.main()
