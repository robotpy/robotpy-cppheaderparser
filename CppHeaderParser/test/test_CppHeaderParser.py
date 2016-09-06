# -*- coding: utf-8 -*-
import unittest
import sys
if sys.version_info[0] == 2:
    sys.path = [".."] + sys.path
    import CppHeaderParser as CppHeaderParser
else:
    sys.path = ["..", "../python3-libs"] + sys.path    
    import CppHeaderParser3 as CppHeaderParser

def filter_pameters(p):
    "Reduce a list of dictionaries to the desired keys for function parameter testing"
    rtn = []
    for d in p:
        rtn.append({'name': d['name'], 'desc': d['desc'], 'type': d['type']})
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
            'SampleClass')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["methods"]["public"][0]["rtnType"],
            'void')

    def test_parameters(self):
        self.assertEqual(
            filter_pameters(self.cppHeader.classes["SampleClass"]["methods"]["public"][0]["parameters"]),
            [])

    def test_doxygen(self):
        self.assertTrue(
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
            filter_pameters(self.cppHeader.classes["SampleClass"]["methods"]["public"][1]["parameters"]),
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
            filter_pameters(self.cppHeader.classes["SampleClass"]["methods"]["public"][2]["parameters"]),
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
            filter_pameters(self.cppHeader.classes["SampleClass"]["methods"]["public"][3]["parameters"]),
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
            filter_pameters(self.cppHeader.classes["SampleClass"]["methods"]["public"][4]["parameters"]),
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
            filter_pameters(self.cppHeader.classes["SampleClass"]["methods"]["private"][0]["parameters"]),
            [])

    def test_doxygen(self):
        self.assertTrue(
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
        self.assertTrue(
        "doxygen"
        not in self.cppHeader.classes["SampleClass"]["enums"]["public"][0].keys())

    def test_values(self):
        self.assertEqual(
            self.cppHeader.classes["SampleClass"]["enums"]["public"][0]["values"],
            [{'name': 'EL_ONE', 'value': 1}, {'name': 'EL_TWO', 'value': 2}, {'name': 'EL_NINE', 'value': 9}, {'name': 'EL_TEN', 'value': 10}])



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
            filter_pameters(self.cppHeader.classes["AlphaClass"]["methods"]["public"][0]["parameters"]),
            [])

    def test_doxygen(self):
        self.assertTrue(
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
            filter_pameters(self.cppHeader.classes["AlphaClass"]["methods"]["public"][1]["parameters"]),
            [])

    def test_doxygen(self):
        self.assertTrue(
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
        self.assertTrue(
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
        self.assertTrue(
        "doxygen"
        not in self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0].keys())

    def test_values(self):
        self.assertEqual(
            self.cppHeader.classes["AlphaClass"]["enums"]["protected"][0]["values"],
            [{'name': 'Z_A', 'value': 0},
             {'name': 'Z_B', 'raw_value': '0x2B', 'value': 43}, 
             {'name': 'Z_C', 'raw_value': 'j', 'value': 106},
             {'name': 'Z_D', 'value': 107}])



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
            filter_pameters(self.cppHeader.classes["OmegaClass"]["methods"]["public"][0]["parameters"]),
            [])

    def test_doxygen(self):
        self.assertTrue(
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
        self.assertTrue(
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
            [{'name': 'RI_ZERO', 'value': 0}, {'name': 'RI_ONE', 'value': 1}, {'name': 'RI_TWO', 'value': 2}])


class Bug3488053_TestCase(unittest.TestCase):
    
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
        
    def test_public(self):
        self.assertEqual(len(self.cppHeader.classes["Bug_3488053::Bug_3488053_Nested"]["properties"]["public"]), 1)
    
    def test_private(self):
        self.assertEqual(len(self.cppHeader.classes["Bug_3488053::Bug_3488053_Nested"]["properties"]["private"]), 0)
    
    def test_protected(self):
        self.assertEqual(len(self.cppHeader.classes["Bug_3488053::Bug_3488053_Nested"]["properties"]["protected"]), 0)
    

class Bug3488360_TestCase(unittest.TestCase):
    
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_BloodOrange_inherits(self):
        self.assertEqual(self.cppHeader.classes["BloodOrange"]["inherits"], [])
    
    def test_Bananna_inherits(self):
        self.assertEqual(self.cppHeader.classes["Bananna"]["inherits"], [{'access': 'public', 'class': 'Citrus::BloodOrange', 'virtual': False}])
    
    def test_ExcellentCake_inherits(self):
        self.assertEqual(self.cppHeader.classes["ExcellentCake"]["inherits"],
            [{'access': 'private', 'class': 'Citrus::BloodOrange', 'virtual': False},
             {'access': 'private', 'class': 'Convoluted::Nested::Mixin', 'virtual': False}])
    
class Bug3487551_TestCase(unittest.TestCase):
    
    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_method_rtn_type(self):
        self.assertEqual(self.cppHeader.classes["Bug_3487551"]["methods"]["public"][0]["rtnType"], "int")
    

class SampleStruct_meth_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["methods"]["public"][0]["name"],
            'meth')

    def test_rtntype(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["methods"]["public"][0]["rtnType"],
            'unsigned int')

    def test_parameters(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["methods"]["public"][0]["parameters"],
            [])

    def test_doxygen(self):
        self.assertTrue(
        "doxygen"
        not in self.cppHeader.classes["SampleStruct"]["methods"]["public"][0].keys())



class SampleStruct_prop_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_name(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["properties"]["private"][0]["name"],
            'prop')

    def test_type(self):
        self.assertEqual(
            self.cppHeader.classes["SampleStruct"]["properties"]["private"][0]["type"],
            'int')

    def test_doxygen(self):
        self.assertTrue(
        "doxygen"
        not in self.cppHeader.classes["SampleStruct"]["properties"]["private"][0].keys())


class Bird_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_items_array(self):
        self.assertEqual(self.cppHeader.classes["Bird"]["properties"]["private"][0]["array"], 1)
    
    def test_otherItems_array(self):
        self.assertEqual(self.cppHeader.classes["Bird"]["properties"]["private"][1]["array"], 1)
    
    def test_oneItem_array(self):
        self.assertEqual(self.cppHeader.classes["Bird"]["properties"]["private"][2]["array"], 0)
    
    def test_items_array_size(self):
        self.assertEqual(self.cppHeader.classes["Bird"]["properties"]["private"][0]["array_size"], "MAX_ITEM")
    
    def test_otherItems_array_size(self):
        self.assertEqual(self.cppHeader.classes["Bird"]["properties"]["private"][1]["array_size"], "7")


class Monkey_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Monkey"]["methods"]["public"]), 0)
        
    def test_num_private_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Monkey"]["methods"]["private"]), 1)
        
    def test_num_protected_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Monkey"]["methods"]["protected"]), 0)



class Chicken_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Chicken"]["methods"]["public"]), 0)
        
    def test_num_private_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Chicken"]["methods"]["private"]), 1)
        
    def test_num_protected_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Chicken"]["methods"]["protected"]), 0)
                        
    def test_template(self):
        self.assertEqual(self.cppHeader.classes["Chicken"]["methods"]["private"][0]['template'], "template <typename T>")



class Lizzard_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_normal_constructor(self):
        cmp_values = {'inline': False, 'name': 'Lizzard', 'parameters': [], 'friend': False,
                      'explicit': False, 'constructor': True, 'namespace': '', 'destructor': False,
                      'pure_virtual': False, 'returns': '', 'static': False, 'virtual': False,
                      'template': False, 'rtnType': 'void', 'extern': False, 'path': 'Lizzard',
                      'returns_pointer': 0, 'class': None}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["Lizzard"]["methods"]["private"][0], cmp_values.keys()), 
                         cmp_values)
    
    def test_explicit_constructor(self):
        cmp_values = {'inline': False, 'name': 'Lizzard', 'friend': False,
                      'explicit': True, 'constructor': True, 'namespace': '', 'destructor': False,
                      'pure_virtual': False, 'returns': '', 'static': False, 'virtual': False,
                      'template': False, 'rtnType': 'void', 'extern': False, 'path': 'Lizzard',
                      'returns_pointer': 0, 'class': None}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["Lizzard"]["methods"]["private"][1], cmp_values.keys()), 
                         cmp_values)



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
        self.assertEqual(len(self.cppHeader.classes["GrapeClass"]["properties"]["public"]), 0)
        
    def test_num_private_properties(self):
        self.assertEqual(len(self.cppHeader.classes["GrapeClass"]["properties"]["private"]), 1)
        
    def test_num_protected_properties(self):
        self.assertEqual(len(self.cppHeader.classes["GrapeClass"]["properties"]["protected"]), 0)

    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["GrapeClass"]["methods"]["public"]), 0)
        
    def test_num_private_methods(self):
        self.assertEqual(len(self.cppHeader.classes["GrapeClass"]["methods"]["private"]), 1)
        
    def test_num_protected_methods(self):
        self.assertEqual(len(self.cppHeader.classes["GrapeClass"]["methods"]["protected"]), 0)


class AnonHolderClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_property(self):
        cmp_values = {'constant': 0, 'name': 'a', 'reference': 0, 'type': '', 'static': 0, 'pointer': 0}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["AnonHolderClass"]["properties"]["public"][0], cmp_values.keys()), cmp_values)


class CowClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_class_declaration_method(self):
        self.assertEqual(self.cppHeader.classes["CowClass"]["declaration_method"], "class")

    def test_struct_declaration_method(self):
        self.assertEqual(self.cppHeader.classes["CowStruct"]["declaration_method"], "struct")


class Mango_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_virtual_inherits(self):
        self.assertEqual(self.cppHeader.classes["MangoClass"]["inherits"][0]["virtual"], True)



class Eagle_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_property(self):
        cmp_values = {'constant': 0, 'name': 'a', 'reference': 0, 'array_size': 'MAX_LEN', 'type': 'int', 'static': 0, 'pointer': 0}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["EagleClass"]["properties"]["private"][0], cmp_values.keys()), cmp_values)
    

class Frog_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties(self):
        self.assertEqual(len(self.cppHeader.classes["FrogClass"]["properties"]["private"]), 3)

    

class Cat_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties(self):
        self.assertEqual(len(self.cppHeader.classes["CatClass"]["properties"]["private"]), 0)


class Fish_TestCase(unittest.TestCase):

    def setUp(self):
        #Just make sure it doesnt crash
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    

class Panda_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_property_CONST_A(self):
        cmp_values = {'typedef': None, 'unresolved': False, 'constant': 1, 'name': 'CONST_A',
                      'parent': None, 'pointer': 0, 'namespace': '', 'raw_type': 'int', 'class': 0,
                      'property_of_class': 'PandaClass', 'static': 1, 'fundamental': True,
                      'mutable': False, 'typedefs': 0, 'array': 0, 'type': 'static const int',
                      'reference': 0, 'aliases': []}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["PandaClass"]["properties"]["private"][0], cmp_values.keys()), cmp_values)

    def test_property_CONST_B(self):
        cmp_values = {'typedef': None, 'unresolved': False, 'constant': 1, 'name': 'CONST_B',
                      'parent': None, 'pointer': 0, 'namespace': '', 'raw_type': 'int', 'class': 0,
                      'property_of_class': 'PandaClass', 'static': 1, 'fundamental': True,
                      'mutable': False, 'typedefs': 0, 'array': 0, 'type': 'static const int',
                      'reference': 0, 'aliases': []}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["PandaClass"]["properties"]["private"][1], cmp_values.keys()), cmp_values)


class Potato_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties_potato(self):
        self.assertEqual(len(self.cppHeader.classes["PotatoClass"]["properties"]["private"]), 1)
    
    def test_num_public_properties_potato_fwdstruct(self):
        self.assertEqual(len(self.cppHeader.classes["PotatoClass::FwdStruct"]["properties"]["public"]), 1)


class Hog_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties_potato(self):
        self.assertEqual(len(self.cppHeader.classes["HogClass"]["properties"]["private"]), 1)
    
    def test_property(self):
        cmp_values = {'constant': 0, 'name': 'u', 'reference': 0, 'type': 'union HogUnion', 'static': 0, 'pointer': 0}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["HogClass"]["properties"]["private"][0], cmp_values.keys()), cmp_values)

    def test_union(self):
        cmp_values = {"name": "union HogUnion", "parent":  "HogClass", "declaration_method": "union"}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["HogClass::union HogUnion"], cmp_values.keys()), cmp_values)
    
    def test_union_member_a(self):
        cmp_values = {'constant': 0, 'name': 'a', 'reference': 0, 'type': 'int', 'static': 0, 'pointer': 0}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["HogClass::union HogUnion"]["members"][0], cmp_values.keys()), cmp_values)
    
    def test_union_member_b(self):
        cmp_values = {'constant': 0, 'name': 'b', 'reference': 0, 'type': 'float', 'static': 0, 'pointer': 0}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["HogClass::union HogUnion"]["members"][1], cmp_values.keys()), cmp_values)

# Bug 3497158
class CherryClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties(self):
        self.assertEqual(len(self.cppHeader.classes["CherryClass::NestStruct"]["properties"]["public"]), 1)
    
    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["CherryClass::NestStruct"]["methods"]["public"]), 1)

# Bug 3517308
class GarlicClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties(self):
        self.assertEqual(len(self.cppHeader.classes["GarlicClass"]["properties"]["public"]), 0)
    
    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["GarlicClass"]["methods"]["public"]), 3)

# Bug 3514728
class CarrotClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_properties(self):
        self.assertEqual(len(self.cppHeader.classes["CarrotClass"]["properties"]["private"]), 1)
    
    def test_num_private_methods(self):
        self.assertEqual(len(self.cppHeader.classes["CarrotClass"]["methods"]["private"]), 1)
    
    def test_method_params(self):
        self.assertEqual(
            filter_pameters(self.cppHeader.classes["CarrotClass"]["methods"]["private"][0]["parameters"]),
            [])
        
    def test_class_template(self):
        self.assertEqual(self.cppHeader.classes["CarrotClass"]["template"], "template<class T>")


# Bug 3517289
class CarrotClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_private_methods(self):
        self.assertEqual(len(self.cppHeader.classes["ExternClass"]["methods"]["private"]), 1)


# Bug 3514671
class OliveStruct_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties(self):
        self.assertEqual(len(self.cppHeader.classes["OliveStruct"]["properties"]["public"]), 4)
    
    def test_var_a(self):
        self.assertEqual(self.cppHeader.classes["OliveStruct"]["properties"]["public"][0]["name"], "a")


# Bug 3515330
class Rooster_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_num_public_properties(self):
        self.assertEqual(len(self.cppHeader.classes["RoosterOuterClass"]["properties"]["public"]), 1)
    
    def test_num_private_properties(self):
        self.assertEqual(len(self.cppHeader.classes["RoosterOuterClass"]["properties"]["private"]), 1)
    
    def test_num_sub1_public_properties(self):
        self.assertEqual(len(self.cppHeader.classes["RoosterOuterClass::RoosterSubClass1"]["properties"]["public"]), 1)
    
    def test_num_sub1_private_properties(self):
        self.assertEqual(len(self.cppHeader.classes["RoosterOuterClass::RoosterSubClass1"]["properties"]["private"]), 1)
    
    def test_num_sub2_public_properties(self):
        self.assertEqual(len(self.cppHeader.classes["RoosterOuterClass::RoosterSubClass2"]["properties"]["public"]), 1)
    
    def test_num_sub2_private_properties(self):
        self.assertEqual(len(self.cppHeader.classes["RoosterOuterClass::RoosterSubClass2"]["properties"]["private"]), 1)


# Bug 3514672
class OperatorClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_op_0(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][0]["name"], 'operator=')

    def test_op_1(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][1]["name"], 'operator-=')

    def test_op_2(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][2]["name"], 'operator+=')

    def test_op_3(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][3]["name"], 'operator[]')

    def test_op_4(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][4]["name"], 'operator==')

    def test_op_5(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][5]["name"], 'operator+')

    def test_op_6(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][6]["name"], 'operator-')

    def test_op_7(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][7]["name"], 'operator*')

    def test_op_8(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][8]["name"], 'operator\\')

    def test_op_9(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][9]["name"], 'operator%')

    def test_op_10(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][10]["name"], 'operator^')

    def test_op_11(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][11]["name"], 'operator|')

    def test_op_12(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][12]["name"], 'operator&')

    def test_op_13(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][13]["name"], 'operator~')

    def test_op_14(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][14]["name"], 'operator<<')

    def test_op_15(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][15]["name"], 'operator>>')

    def test_op_16(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][16]["name"], 'operator!=')

    def test_op_17(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][17]["name"], 'operator<')

    def test_op_18(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][18]["name"], 'operator>')

    def test_op_19(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][19]["name"], 'operator>=')

    def test_op_20(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][20]["name"], 'operator<=')

    def test_op_21(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][21]["name"], 'operator!')

    def test_op_22(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][22]["name"], 'operator&&')

    def test_op_23(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][23]["name"], 'operator||')

    def test_op_24(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][24]["name"], 'operator+=')

    def test_op_25(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][25]["name"], 'operator-=')

    def test_op_26(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][26]["name"], 'operator*=')

    def test_op_27(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][27]["name"], 'operator\\=')

    def test_op_28(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][28]["name"], 'operator%=')

    def test_op_29(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][29]["name"], 'operator&=')

    def test_op_30(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][30]["name"], 'operator|=')

    def test_op_31(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][31]["name"], 'operator^=')

    def test_op_32(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][32]["name"], 'operator<<=')

    def test_op_33(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][33]["name"], 'operator>>=')

    def test_op_34(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][34]["name"], 'operator++')

    def test_op_35(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][35]["name"], 'operator--')

    def test_op_36(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][36]["name"], 'operator()')

    def test_op_37(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][37]["name"], 'operator->')

    def test_op_38(self):
        self.assertEqual(self.cppHeader.classes["OperatorClass"]["methods"]["public"][38]["name"], 'operator,')


# Feature Request 3519502 & 3523010
class CrowClass_TestCase(unittest.TestCase):

    def setUp(self):
        self.savedSupportedAccessSpecifier = CppHeaderParser.supportedAccessSpecifier
        CppHeaderParser.supportedAccessSpecifier.append("public  slots ")#intentionally add expra spaces to make sure they get cleaned up
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["CrowClass"]["methods"]["public"]), 1)

    def test_rtntype_public_slot_method(self):
        self.assertEqual(self.cppHeader.classes["CrowClass"]["methods"]["public slots"][0]["rtnType"], 'void')

    def test_num_public_slot_methods(self):
        self.assertEqual(len(self.cppHeader.classes["CrowClass"]["methods"]["public slots"]), 1)
    
    def tearDown(self):
        CppHeaderParser.supportedAccessSpecifier = self.savedSupportedAccessSpecifier


# Bug 3497170
class DriverFuncs_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_name_0(self):
        self.assertEqual(self.cppHeader.classes["DriverFuncs"]["properties"]["public"][0]["name"], "init")
        
    def test_type_0(self):
        self.assertEqual(self.cppHeader.classes["DriverFuncs"]["properties"]["public"][0]["type"], "void * ( * ) ( )")
    
    def test_function_pointer_field_0(self):
        self.assertEqual(self.cppHeader.classes["DriverFuncs"]["properties"]["public"][0]["function_pointer"], 1)
        
    def test_name_1(self):
        self.assertEqual(self.cppHeader.classes["DriverFuncs"]["properties"]["public"][1]["name"], "write")
        
    def test_type_1(self):
        self.assertEqual(self.cppHeader.classes["DriverFuncs"]["properties"]["public"][1]["type"], "void ( * ) ( void * buf, int buflen )")
    
    def test_function_pointer_field_1(self):
        self.assertEqual(self.cppHeader.classes["DriverFuncs"]["properties"]["public"][1]["function_pointer"], 1)
    

# Bug 3519178
class Snail_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_rtn_type(self):
        self.assertEqual(self.cppHeader.classes["Snail2Class"]["methods"]["public"][0]["rtnType"], "SnailNamespace::SnailClass")
    
    def test_param_name(self):
        self.assertEqual(self.cppHeader.classes["Snail2Class"]["methods"]["public"][0]["parameters"][0]["name"], "")
    
    def test_param_name(self):
        self.assertEqual(self.cppHeader.classes["Snail2Class"]["methods"]["public"][0]["parameters"][0]["type"], "tr1::shared_ptr<SnailTemplateClass<SnailNamespace::SnailClass> >")

# Feature Request 3523198
class Quale_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_rtn_type(self):
        self.assertEqual(self.cppHeader.classes["QualeClass"]["methods"]["private"][0]["rtnType"], "void")


# Feature Request 3523235
class Rock_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_const_0(self):
        self.assertEqual(self.cppHeader.classes["RockClass"]["methods"]["private"][0]["const"], True)
    
    def test_const_1(self):
        self.assertEqual(self.cppHeader.classes["RockClass"]["methods"]["private"][1]["const"], False)


# Bug 3523196
class Almond_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_rtn_type(self):
        self.assertEqual(self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["rtnType"], "std::map<unsigned, std::pair<unsigned, SnailTemplateClass<SnailNamespace::SnailClass> > >")
 
    def test_param_1_name(self):
        self.assertEqual(self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["parameters"][0]["name"], "flag")
     
    def test_param_1_type(self):
        self.assertEqual(self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["parameters"][0]["type"], "bool")
     
    def test_param_2_name(self):
        self.assertEqual(self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["parameters"][1]["name"], "bigArg")
    
    def test_param_2_type(self):
        self.assertEqual(self.cppHeader.classes["AlmondClass"]["methods"]["public"][0]["parameters"][1]["type"], "std::map<unsigned, std::pair<unsigned, SnailTemplateClass<SnailNamespace::SnailClass> > >")


# Bug 3524327
class Stone_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_const_0(self):
        self.assertEqual(self.cppHeader.classes["StoneClass"]["methods"]["private"][0]["const"], True)
    
    def test_const_1(self):
        self.assertEqual(self.cppHeader.classes["StoneClass"]["methods"]["private"][1]["const"], False)
 

# Bug 3531219
class Kangaroo_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_kangaroo_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Kangaroo"]["methods"]["public"]), 1)
    
    def test_num_joey_methods(self):
        self.assertEqual(len(self.cppHeader.classes["Kangaroo::Joey"]["methods"]["public"]), 1)


# Bug 3535465
class Ant_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_num_constructor_1_params(self):
        self.assertEqual(len(self.cppHeader.classes["Ant"]["methods"]["public"][0]["parameters"]), 3)
    
    def test_num_constructor_2_params(self):
        self.assertEqual(len(self.cppHeader.classes["Ant"]["methods"]["public"][1]["parameters"]), 1)

# Bug 3536069
class Onion_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_properties_red(self):
        self.assertEqual(len(self.cppHeader.classes["Onion<Red,Plant>"]["properties"]["public"]), 1)

    def test_num_public_properties_sweet(self):
        self.assertEqual(len(self.cppHeader.classes["Onion<Sweet,Plant>"]["properties"]["public"]), 1)

    def test_class_template(self):
        self.assertEqual(self.cppHeader.classes["Onion<Sweet,Plant>"]["template"], "template <typename Plant>")
    
# Bug 3536067
class BlueJay_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_num_public_methods(self):
        self.assertEqual(len(self.cppHeader.classes["BlueJay"]["methods"]["public"]), 1)

# Bug 3536266
class functions_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("""\
              void global_funct1(int i);             
              int global_funct2(void);
              """, "string")
    
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
        self.assertEqual(self.cppHeader.classes["Pea"]["inherits"][0]["class"], "Vegetable<Green>")

# Bug 3540172
class functions2_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("""\
              void global_funct1(int i);             
              int global_funct2(void){
                  // do something
              }
              """, "string")
    
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
        return self.assertEqual(self.cppHeader.classes["Worm"]["methods"]["public"][0]["line_number"], 23)
        
    def test_lineno_Worm_getName(self):
        return self.assertEqual(self.cppHeader.classes["Worm"]["methods"]["public"][1]["line_number"], 24)
            
    def test_lineno_Worm_namep(self):
        return self.assertEqual(self.cppHeader.classes["Worm"]["properties"]["private"][0]["line_number"], 29)

# Bug 3567172
class Pear_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")

    def test_property(self):
        self.assertEqual(self.cppHeader.classes["Pear"]["properties"]["private"][0]["name"], "stem_property")



# Bug 3567217 and 3569663
class Macro_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(r"""
#include <string.h>
#include "../../debug.h"

#define ONE 1
#define TWO_NUM_N_NAME "2 (TWO)"
#pragma once

 #define DEBUG_PRINT(x)           \
    printf("---------------\n"); \
    printf("DEBUG: %d\n", x);    \
    printf("---------------\n");""", "string")

    def test_includes(self):
        self.assertEqual(self.cppHeader.includes, ['<string.h>', '"../../debug.h"'])
    
    def test_pragmas(self):
        self.assertEqual(self.cppHeader.pragmas, ['once'])
        
    def test_pragmas0(self):
        self.assertEqual(self.cppHeader.defines[0], 'ONE 1')
            
    def test_pragmas1(self):
        self.assertEqual(self.cppHeader.defines[1], 'TWO_NUM_N_NAME "2 (TWO)"')
                
    def test_pragmas2(self):
        self.assertEqual(self.cppHeader.defines[2], 'DEBUG_PRINT(x)           \\\n    printf("---------------\\n"); \\\n    printf("DEBUG: %d\\n", x);    \\\n    printf("---------------\\n");')



# Bug: 3567854 and 3568241
class Beans_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_anonymous_union_name(self):
        return self.assertEqual(self.cppHeader.classes["Beans"]["properties"]["public"][1]["name"], "")
    
    def test_second_anonymous_union_name(self):
        return self.assertEqual(self.cppHeader.classes["Beans"]["properties"]["public"][3]["name"], "")


# Bug: 3567854 and 3568241
class termite_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_termite_function(self):
        self.assertEqual(self.cppHeader.functions[5]["name"], "termite")



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
        self.assertEqual(self.cppHeader.enums[0]["values"], [
            {'name': 'NAME', 'value': "( 'J' << 24 | 'A' << 16 | 'S' << 8 | 'H' )"}])


# Bug: 3577484
class Fly_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("FruitFly<int>"), True)

# Bug BitBucket #2
class ClassAfterMagicMacro_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_class_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("ClassAfterMagicMacro"), True)

# Bug BitBucket #3
class FilterMagicMacro_TestCase(unittest.TestCase):

    def setUp(self):
        savedIgnoreSymbols = CppHeaderParser.ignoreSymbols
        CppHeaderParser.ignoreSymbols.append("MAGIC_FUNC()")
        self.cppHeader = CppHeaderParser.CppHeader(r"""
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
};""", "string")
        CppHeaderParser.ignoreSymbols = savedIgnoreSymbols
    
    def test_method_exists(self):
        self.assertEqual(self.cppHeader.classes["FilterMagicMacro"]["methods"]["public"][0]["name"], "FilterMagicMacroMethod")
    
    def test_line_num_is_correct(self):
        self.assertEqual(self.cppHeader.classes["FilterMagicMacro"]["methods"]["public"][0]["line_number"], 14);

# Bug BitBucket #4
class ClassRegularTypedefs_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_uint_exists(self):
        self.assertEqual(self.cppHeader.typedefs.has_key("uint"), True)
    
    def test_string_array_exists(self):
        self.assertEqual(self.cppHeader.typedefs.has_key("string_array"), True)
    
    def test_SmartObjPtr_exists(self):
        self.assertEqual(self.cppHeader.typedefs.has_key("SmartObjPtr"), True)
    
    def test_StrStrMap_exists(self):
        self.assertEqual(self.cppHeader.typedefs.has_key("StrStrMap"), True)
    
    def test_AfterTypedefClass_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("AfterTypedefClass"), True)

# Bug BitBucket #6
class LineNumAfterDivide_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_line_num(self):
        self.assertEqual(self.cppHeader.classes["LineNumAfterDivide"]["methods"]["private"][1]["line_number"], 583)

# Bug BitBucket #5
class ClassHerbCilantro_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
        
    def test_HerbCilantro_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("Herb::Cilantro"), True)

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
        self.assertEqual(self.cppHeader.classes["Garlic"]["methods"]["public"][0]["name"], "genNum")

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
        self.assertEqual(self.cppHeader.classes.has_key("Peach"), True)
            
    def test_Plumb_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("Plumb"), True)
        
    def test_function_exists(self):
        self.assertEqual(self.cppHeader.classes["Plumb"]["methods"]["private"][0]["name"], "doSomethingGreat")

# Bug BitBucket #9
class Grape_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
        
    def test_Grape_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("Grape"), True)
        
    def test_a_exists(self):
        self.assertEqual(self.cppHeader.classes["Grape"]["properties"]["public"][0]["name"], "a")
        
    def test_a_type(self):
        self.assertEqual(self.cppHeader.classes["Grape"]["properties"]["public"][0]["type"], "int")
        
    def test_b_exists(self):
        self.assertEqual(self.cppHeader.classes["Grape"]["properties"]["public"][1]["name"], "b")
        
    def test_b_type(self):
        self.assertEqual(self.cppHeader.classes["Grape"]["properties"]["public"][1]["type"], "int")
        
    def test_c_exists(self):
        self.assertEqual(self.cppHeader.classes["Grape"]["properties"]["public"][2]["name"], "c")
        
    def test_d_exists(self):
        self.assertEqual(self.cppHeader.classes["Grape"]["properties"]["public"][3]["name"], "d")
        
    def test_e_exists(self):
        self.assertEqual(self.cppHeader.classes["Grape"]["properties"]["public"][4]["name"], "e")
        
    def test_f_exists(self):
        self.assertEqual(self.cppHeader.classes["Grape"]["properties"]["public"][5]["name"], "f")

# Bug BitBucket #14
class Avacado_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
        
    def test_Avacado_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("Avacado"), True)
        
    def test_foo_return_type(self):
        self.assertEqual(self.cppHeader.classes["Avacado"]["methods"]["public"][0]["returns"], "uint8_t")
        
    def test_bar_return_type(self):
        self.assertEqual(self.cppHeader.classes["Avacado"]["methods"]["public"][1]["returns"], "::uint8_t")

# Bug BitBucket #13
class Raspberry_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_anon_struct_1_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("<anon-struct-1>"), True)
        
    def test_beta_exists(self):
        self.assertEqual(self.cppHeader.classes["<anon-struct-1>"]["properties"]["public"][0]["name"], "anon_struct_variable")
    
    def test_Raspberry_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("Raspberry"), True)
        
    def test_a_exists(self):
        self.assertEqual(self.cppHeader.classes["Raspberry"]["properties"]["public"][0]["name"], "a")

# Bug BitBucket #15 & 16
class Hen_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
        
    def test_default_a(self):
        self.assertEqual(self.cppHeader.classes["Hen"]["methods"]["public"][0]["parameters"][0]["defaultValue"], "100")
        
    def test_default_b(self):
        self.assertEqual(self.cppHeader.classes["Hen"]["methods"]["public"][0]["parameters"][1]["defaultValue"], "0xfd")
                
    def test_default_c(self):
        self.assertEqual(self.cppHeader.classes["Hen"]["methods"]["public"][0]["parameters"][2]["defaultValue"], "1.7e-3")
                
    def test_default_d(self):
        self.assertEqual(self.cppHeader.classes["Hen"]["methods"]["public"][0]["parameters"][3]["defaultValue"], "3.14")
                
    def test_default_s1(self):
        self.assertEqual(self.cppHeader.classes["Hen"]["methods"]["public"][1]["parameters"][0]["defaultValue"], '""')
                
    def test_default_s2(self):
        self.assertEqual(self.cppHeader.classes["Hen"]["methods"]["public"][1]["parameters"][1]["defaultValue"], '"nothing"')


# Bug BitBucket #19
class Raddish_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
        
    def test_Avacado_exists(self):
        self.assertEqual(self.cppHeader.classes["Raddish_SetIterator"]["properties"]["protected"][0]["name"], "_beg")
        
    def test_class_template(self):
        template_str = \
        "template<typename VALUE,\n" \
        "         typename VALUE_SET_ITERATOR,\n" \
        "         typename ACCESOR=Raddish::SimpleAccessor<VALUE,VALUE_SET_ITERATOR> >"
        self.assertEqual(self.cppHeader.classes["Raddish_SetIterator"]["template"], template_str)


# Bug bug 57
class Carambola_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_name(self):
        self.assertEqual(self.cppHeader.enums[2]["name"], "Carambola")
    
    def test_values(self):
        self.assertEqual(self.cppHeader.enums[2]["values"], [
            {'name': 'StarFruit', 'value': '( 2 + 2 ) / 2'}])
     
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
        self.assertEqual(self.cppHeader.typedefs.has_key("TenCharArray[10]"), True)
    
    def test_value(self):
        self.assertEqual(self.cppHeader.typedefs["TenCharArray[10]"], "char")

# typedef structs
class TypedefStruct_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
        
    def test_name(self):
        self.assertEqual(self.cppHeader.typedefs.has_key("MAGIC_FILE"), True)
    
    def test_value(self):
        self.assertEqual(self.cppHeader.typedefs["MAGIC_FILE"], "struct SUPER_MAGIC_FILE")
        
    
# Bug SourceForge #10
class Picture_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
        
    def test_array_size(self):
        self.assertEqual(self.cppHeader.classes["Picture"]["properties"]["public"][1]["array_size"], 16384)
            
    def test_multi_dimensional_array_size(self):
        self.assertEqual(self.cppHeader.classes["Picture"]["properties"]["public"][1]["multi_dimensional_array_size"], "128x128")
    


# SourceForge bug 58
class Apricot_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_Apricot_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("Apricot"), True)
        
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
        self.assertEqual(self.cppHeader.classes["Lemon"]["methods"]["public"][0]["final"], True)
        
    def test_lemon_foo2_is_not_final(self):
        self.assertEqual(self.cppHeader.classes["Lemon"]["methods"]["public"][1]["final"], False)
        
    def test_lime_abc_is_not_override(self):
        self.assertEqual(self.cppHeader.classes["Lime"]["methods"]["public"][0]["override"], False)
        
    def test_lime_foo2_is_not_override(self):
        self.assertEqual(self.cppHeader.classes["Lime"]["methods"]["public"][1]["override"], True)


class JSON_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader(r"""
struct Lemon
{
    virtual void foo() final;
    virtual void foo2();
};
 
struct Lime final : Lemon
{
    void abc();
    void foo2() override;
};""", "string")
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
        self.assertEqual(self.cppHeader.classes.has_key("MouseClass"), True)
        
    def test_mouse_typedef_correct_value(self):
        self.assertEqual(self.cppHeader.classes["MouseClass"]["methods"]["public"][0]["parameters"][0]['raw_type'],
                         "MouseNS::MouseClass::mouse_typedef")

# BitBucket bug 26
class Fig_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_Fig_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("Fig"), True)
        
    def test_a_exists(self):
        self.assertEqual(self.cppHeader.classes["Grape"]["properties"]["public"][0]["name"], "a")

# BitBucket bug 27
class Olive_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_Olive_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("union olive"), True)
        
    def test_union_member_x(self):
        cmp_values = {'constant': 0, 'name': 'x', 'reference': 0, 'type': 'int', 'static': 0, 'pointer': 0}
        self.assertEqual(filter_dict_keys(self.cppHeader.classes["union olive"]["members"][0], cmp_values.keys()), cmp_values)

# BitBucket bug 61
class Beet_TestCase(unittest.TestCase):

    def setUp(self):
        self.cppHeader = CppHeaderParser.CppHeader("TestSampleClass.h")
    
    def test_Beet_exists(self):
        self.assertEqual(self.cppHeader.classes.has_key("BeetStruct"), True)
        
    def test_BeetEnum_exists(self):
        self.assertEqual(self.cppHeader.classes["BeetStruct"]["enums"]["public"][0]["name"], "BeetEnum")
    
    
    
if __name__ == '__main__':
    unittest.main()


