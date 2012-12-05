Python package "CppHeaderParser"
--------------------------------
**Purpose:** Parse C++ header files and generate a data structure representing the class

**Author:** Jashua Cloutier

**Licence:** BSD

**External modules required:** PLY

**Quick start**::

    #include <vector>
    #include <string>
    
    #define DEF_1 1
    #define OS_NAME "Linux"
    
    using namespace std;
    class SampleClass
    {
    public:
        SampleClass();
        /*!
         * Method 1
         */
        string meth1();
    
        ///
        /// Method 2 description
        ///
        /// @param v1 Variable 1
        ///
        int meth2(int v1);
    
        /**
         * Method 3 description
         *
         * \param v1 Variable 1
         * \param v2 Variable 2
         */
        void meth3(const string & v1, vector<string> & v2);
    
        /**********************************
         * Method 4 description
         *
         * @return Return value
         *********************************/
        unsigned int meth4();
    private:
        void * meth5(){return NULL};
    
        /// prop1 description
        string prop1;
        //! prop5 description
        int prop5;
    };
    namespace Alpha
    {
        class AlphaClass
        {
        public:
            AlphaClass();
    
            void alphaMethod();
    
            string alphaString;
        };
    
        namespace Omega
        {
            class OmegaClass
            {
            public:
                OmegaClass();
    
                string omegaString;
            };
        };
    }
    
    int sampleFreeFunction(int i)
    {
    	return i + 1;
    }
    
    int anotherFreeFunction(void);
    }
    

**Python code**::

    #!/usr/bin/python
    import sys
    sys.path = ["../"] + sys.path
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
    
    print "\nReturn type for meth1:"
    print cppHeader.classes["SampleClass"]["methods"]["public"][1]["rtnType"]
    
    print "\nDoxygen for meth2:"
    print cppHeader.classes["SampleClass"]["methods"]["public"][2]["doxygen"]
    
    print "\nParameters for meth3:"
    print cppHeader.classes["SampleClass"]["methods"]["public"][3]["parameters"]
    
    print "\nDoxygen for meth4:"
    print cppHeader.classes["SampleClass"]["methods"]["public"][4]["doxygen"]
    
    print "\nReturn type for meth5:"
    print cppHeader.classes["SampleClass"]["methods"]["private"][0]["rtnType"]
    
    print "\nDoxygen type for prop1:"
    print cppHeader.classes["SampleClass"]["properties"]["private"][0]["doxygen"]
    
    print "\nType for prop5:"
    print cppHeader.classes["SampleClass"]["properties"]["private"][1]["type"]
    
    print "\nNamespace for AlphaClass is:"
    print cppHeader.classes["AlphaClass"]["namespace"]
    
    print "\nReturn type for alphaMethod is:"
    print cppHeader.classes["AlphaClass"]["methods"]["public"][0]["rtnType"]
    
    print "\nNamespace for OmegaClass is:"
    print cppHeader.classes["OmegaClass"]["namespace"]
    
    print "\nType for omegaString is:"
    print cppHeader.classes["AlphaClass"]["properties"]["public"][0]["type"]
    
    print "\nFree functions are:"
    for func in cppHeader.functions:
        print " %s"%func["name"]
    
    print "\n#includes are:"
    for incl in cppHeader.includes:
        print " %s"%incl
    
    print "\n#defines are:"
    for define in cppHeader.defines:
        print " %s"%define

**Output**::

    CppHeaderParser view of class SampleClass
    {
    public
        // Methods
       {'line_number': 11, 'static': False, 'rtnType': 'void', 'const': False, 'parameters': [], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': '', 'template': False, 'friend': False, 'returns_class': False, 'extern': False, 'path': 'SampleClass', 'returns_pointer': 0, 'class': None, 'name': 'SampleClass', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': True, 'debug': 'SampleClass ( ) ;', 'inline': False}
       {'line_number': 15, 'static': False, 'rtnType': 'string', 'returns_unknown': True, 'const': False, 'parameters': [], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'string', 'template': False, 'friend': False, 'returns_class': False, 'inline': False, 'extern': False, 'path': 'SampleClass', 'class': None, 'doxygen': '/*!\n* Method 1\n*/', 'name': 'meth1', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': False, 'constructor': False, 'debug': 'string meth1 ( ) ;', 'returns_pointer': 0}
       {'line_number': 22, 'static': False, 'rtnType': 'int', 'const': False, 'parameters': [{'line_number': 22, 'constant': 0, 'name': 'v1', 'reference': 0, 'type': 'int', 'static': 0, 'pointer': 0, 'desc': 'Variable 1'}], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'int', 'template': False, 'friend': False, 'returns_class': False, 'inline': False, 'extern': False, 'path': 'SampleClass', 'class': None, 'doxygen': '///\n/// Method 2 description\n///\n/// @param v1 Variable 1\n///', 'name': 'meth2', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'int meth2 ( int v1 ) ;', 'returns_pointer': 0}
       {'line_number': 30, 'static': False, 'rtnType': 'void', 'const': False, 'parameters': [{'line_number': 30, 'constant': 1, 'name': 'v1', 'reference': 1, 'type': 'const string &', 'static': 0, 'pointer': 0, 'desc': 'Variable 1'}, {'line_number': 30, 'constant': 0, 'name': 'v2', 'reference': 1, 'type': 'vector<string> &', 'static': 0, 'pointer': 0, 'desc': 'Variable 2'}], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'void', 'template': False, 'friend': False, 'unresolved_parameters': True, 'returns_class': False, 'inline': False, 'extern': False, 'path': 'SampleClass', 'class': None, 'doxygen': '/**\n* Method 3 description\n*\n* \\param v1 Variable 1\n* \\param v2 Variable 2\n*/', 'name': 'meth3', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'void meth3 ( const string & v1 , vector <string> & v2 ) ;', 'returns_pointer': 0}
       {'line_number': 37, 'static': False, 'rtnType': 'unsigned int', 'const': False, 'parameters': [], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'unsigned int', 'template': False, 'friend': False, 'returns_class': False, 'inline': False, 'extern': False, 'path': 'SampleClass', 'class': None, 'doxygen': '/**********************************\n* Method 4 description\n*\n* @return Return value\n*********************************/', 'name': 'meth4', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'unsigned int meth4 ( ) ;', 'returns_pointer': 0}
    protected
    private
        // Properties
        {'line_number': 42, 'constant': 0, 'name': 'prop1', 'reference': 0, 'type': 'string', 'static': 0, 'pointer': 0}
        {'line_number': 44, 'constant': 0, 'name': 'prop5', 'reference': 0, 'type': 'int', 'static': 0, 'pointer': 0}
        // Methods
       {'line_number': 39, 'static': False, 'rtnType': 'void *', 'const': False, 'parameters': [], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'void', 'template': False, 'friend': False, 'returns_class': False, 'extern': False, 'path': 'SampleClass', 'returns_pointer': 1, 'class': None, 'name': 'meth5', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'void * meth5 ( ) {', 'inline': False}
    }
    
    class Alpha::AlphaClass
    {
    public
        // Properties
        {'line_number': 55, 'constant': 0, 'name': 'alphaString', 'reference': 0, 'type': 'string', 'static': 0, 'pointer': 0}
        // Methods
       {'line_number': 51, 'static': False, 'rtnType': 'void', 'const': False, 'parameters': [], 'namespace': 'Alpha::', 'virtual': False, 'destructor': False, 'returns': '', 'template': False, 'friend': False, 'returns_class': False, 'extern': False, 'path': 'Alpha::AlphaClass', 'returns_pointer': 0, 'class': None, 'name': 'AlphaClass', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': True, 'debug': 'AlphaClass ( ) ;', 'inline': False}
       {'line_number': 53, 'static': False, 'rtnType': 'void', 'const': False, 'parameters': [], 'namespace': 'Alpha::', 'virtual': False, 'destructor': False, 'returns': 'void', 'template': False, 'friend': False, 'returns_class': False, 'extern': False, 'path': 'Alpha::AlphaClass', 'returns_pointer': 0, 'class': None, 'name': 'alphaMethod', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'void alphaMethod ( ) ;', 'inline': False}
    protected
    private
    }
    
    class Alpha::Omega::OmegaClass
    {
    public
        // Properties
        {'line_number': 65, 'constant': 0, 'name': 'omegaString', 'reference': 0, 'type': 'string', 'static': 0, 'pointer': 0}
        // Methods
       {'line_number': 63, 'static': False, 'rtnType': 'void', 'const': False, 'parameters': [], 'namespace': 'Alpha::Omega::', 'virtual': False, 'destructor': False, 'returns': '', 'template': False, 'friend': False, 'returns_class': False, 'extern': False, 'path': 'Alpha::Omega::OmegaClass', 'returns_pointer': 0, 'class': None, 'name': 'OmegaClass', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': True, 'debug': 'OmegaClass ( ) ;', 'inline': False}
    protected
    private
    }
    
    // functions
    {'line_number': 70, 'static': False, 'rtnType': 'int', 'const': False, 'parameters': [{'line_number': 70, 'constant': 0, 'name': 'i', 'reference': 0, 'type': 'int', 'static': 0, 'pointer': 0}], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'int', 'template': False, 'friend': False, 'returns_class': False, 'extern': False, 'returns_pointer': 0, 'class': None, 'name': 'sampleFreeFunction', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'int sampleFreeFunction ( int i ) {', 'inline': False}
    {'line_number': 75, 'static': False, 'rtnType': 'int', 'const': False, 'parameters': [{'line_number': 75, 'constant': 0, 'name': '', 'reference': 0, 'type': 'void', 'static': 0, 'pointer': 0}], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'int', 'template': False, 'friend': False, 'returns_class': False, 'extern': False, 'returns_pointer': 0, 'class': None, 'name': 'anotherFreeFunction', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'int anotherFreeFunction ( void ) ;', 'inline': False}
    
    Number of public methods 5
    Number of private properties 2
    Parameter Types for public method meth3 ['const string &', 'vector<string> &']
    
    Return type for meth1:
    string
    
    Doxygen for meth2:
    ///
    /// Method 2 description
    ///
    /// @param v1 Variable 1
    ///
    
    Parameters for meth3:
    [{'line_number': 30, 'constant': 1, 'name': 'v1', 'reference': 1, 'type': 'const string &', 'static': 0, 'pointer': 0, 'desc': 'Variable 1'}, {'line_number': 30, 'constant': 0, 'name': 'v2', 'reference': 1, 'type': 'vector<string> &', 'static': 0, 'pointer': 0, 'desc': 'Variable 2'}]
    
    Doxygen for meth4:
    /**********************************
    * Method 4 description
    *
    * @return Return value
    *********************************/
    
    Return type for meth5:
    void *
    
    Doxygen type for prop1:
    /// prop1 description
    
    Type for prop5:
    int
    
    Namespace for AlphaClass is:
    Alpha
    
    Return type for alphaMethod is:
    void
    
    Namespace for OmegaClass is:
    Alpha::Omega
    
    Type for omegaString is:
    string
    
    Free functions are:
     sampleFreeFunction
     anotherFreeFunction
    
    #includes are:
     <vector>
     <string>
    
    #defines are:
     DEF_1 1
     OS_NAME "Linux"
    


Contributors
------------
* Chris Love
* HartsAntler
