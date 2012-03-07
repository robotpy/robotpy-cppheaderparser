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
        self.assertEqual(self.cppHeader.classes["Bananna"]["inherits"], [{'access': 'public', 'class': 'Citrus::BloodOrange'}])
    
    def test_ExcellentCake_inherits(self):
        self.assertEqual(self.cppHeader.classes["ExcellentCake"]["inherits"],
            [{'access': 'private', 'class': 'Citrus::BloodOrange'}, {'access': 'private', 'class': 'Convoluted::Nested::Mixin'}])
    
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



class Lizzard_TestCase(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()


