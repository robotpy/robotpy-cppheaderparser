Python package "CppHeaderParser"
--------------------------------
**Purpose:** Parse C++ header files and generate a data structure representing the class

**Author:** Jashua Cloutier

**Licence:** BSD

**External modules required:** PLY

**Quick start**::

    #include <vector>
    #include <string>
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

**Output**::

    CppHeaderParser view of class SampleClass
    {
    public
        // Methods
       {'inline': False, 'name': 'SampleClass', 'parameters': [], 'friend': False, 'explicit': False, 'constructor': True, 'namespace': '', 'returns_fundamental': True, 'destructor': False, 'pure_virtual': False, 'returns': '', 'static': False, 'virtual': False, 'template': False, 'rtnType': 'void', 'extern': False, 'path': 'SampleClass', 'returns_pointer': 0, 'class': None, 'debug': 'SampleClass ( ) ;', 'returns_class': False}
       {'static': False, 'rtnType': 'string', 'returns_unknown': True, 'parameters': [], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'string', 'template': False, 'friend': False, 'returns_class': False, 'inline': False, 'extern': False, 'path': 'SampleClass', 'class': None, 'doxygen': '/*!\n* Method 1\n*/', 'name': 'meth1', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': False, 'constructor': False, 'debug': 'string meth1 ( ) ;', 'returns_pointer': 0}
       {'static': False, 'rtnType': 'int', 'parameters': [{'constant': 0, 'name': 'v1', 'reference': 0, 'type': 'int', 'static': 0, 'pointer': 0, 'desc': 'Variable 1'}], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'int', 'template': False, 'friend': False, 'returns_class': False, 'inline': False, 'extern': False, 'path': 'SampleClass', 'class': None, 'doxygen': '///\n/// Method 2 description\n///\n/// @param v1 Variable 1\n///', 'name': 'meth2', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'int meth2 ( int v1 ) ;', 'returns_pointer': 0}
       {'static': False, 'rtnType': 'void', 'parameters': [{'constant': 1, 'name': 'v1', 'reference': 1, 'type': 'const string &', 'static': 0, 'pointer': 0, 'desc': 'Variable 1'}, {'constant': 0, 'name': 'v2', 'reference': 1, 'type': 'vector<string> &', 'static': 0, 'pointer': 0, 'desc': 'Variable 2'}], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'void', 'template': False, 'friend': False, 'unresolved_parameters': True, 'returns_class': False, 'inline': False, 'extern': False, 'path': 'SampleClass', 'class': None, 'doxygen': '/**\n* Method 3 description\n*\n* \\param v1 Variable 1\n* \\param v2 Variable 2\n*/', 'name': 'meth3', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'void meth3 ( const string & v1 , vector <string > & v2 ) ;', 'returns_pointer': 0}
       {'static': False, 'rtnType': 'unsigned int', 'parameters': [], 'namespace': '', 'virtual': False, 'destructor': False, 'returns': 'unsigned int', 'template': False, 'friend': False, 'returns_class': False, 'inline': False, 'extern': False, 'path': 'SampleClass', 'class': None, 'doxygen': '/**********************************\n* Method 4 description\n*\n* @return Return value\n*********************************/', 'name': 'meth4', 'pure_virtual': False, 'explicit': False, 'returns_fundamental': True, 'constructor': False, 'debug': 'unsigned int meth4 ( ) ;', 'returns_pointer': 0}
    protected
    private
        // Properties
        {'constant': 0, 'name': 'prop1', 'reference': 0, 'type': 'string', 'static': 0, 'pointer': 0}
        {'constant': 0, 'name': 'prop5', 'reference': 0, 'type': 'int', 'static': 0, 'pointer': 0}
        // Methods
       {'inline': False, 'name': 'meth5', 'parameters': [], 'friend': False, 'explicit': False, 'constructor': False, 'namespace': '', 'returns_fundamental': True, 'destructor': False, 'pure_virtual': False, 'returns': 'void', 'static': False, 'virtual': False, 'template': False, 'rtnType': 'void *', 'extern': False, 'path': 'SampleClass', 'returns_pointer': 1, 'class': None, 'debug': 'void * meth5 ( ) {', 'returns_class': False}
    }
    
    class Alpha::AlphaClass
    {
    public
        // Properties
        {'constant': 0, 'name': 'alphaString', 'reference': 0, 'type': 'string', 'static': 0, 'pointer': 0}
        // Methods
       {'inline': False, 'name': 'AlphaClass', 'parameters': [], 'friend': False, 'explicit': False, 'constructor': True, 'namespace': 'Alpha::', 'returns_fundamental': True, 'destructor': False, 'pure_virtual': False, 'returns': '', 'static': False, 'virtual': False, 'template': False, 'rtnType': 'void', 'extern': False, 'path': 'Alpha::AlphaClass', 'returns_pointer': 0, 'class': None, 'debug': 'AlphaClass ( ) ;', 'returns_class': False}
       {'inline': False, 'name': 'alphaMethod', 'parameters': [], 'friend': False, 'explicit': False, 'constructor': False, 'namespace': 'Alpha::', 'returns_fundamental': True, 'destructor': False, 'pure_virtual': False, 'returns': 'void', 'static': False, 'virtual': False, 'template': False, 'rtnType': 'void', 'extern': False, 'path': 'Alpha::AlphaClass', 'returns_pointer': 0, 'class': None, 'debug': 'void alphaMethod ( ) ;', 'returns_class': False}
    protected
    private
    }
    
    class Alpha::Omega::OmegaClass
    {
    public
        // Properties
        {'constant': 0, 'name': 'omegaString', 'reference': 0, 'type': 'string', 'static': 0, 'pointer': 0}
        // Methods
       {'inline': False, 'name': 'OmegaClass', 'parameters': [], 'friend': False, 'explicit': False, 'constructor': True, 'namespace': 'Alpha::Omega::', 'returns_fundamental': True, 'destructor': False, 'pure_virtual': False, 'returns': '', 'static': False, 'virtual': False, 'template': False, 'rtnType': 'void', 'extern': False, 'path': 'Alpha::Omega::OmegaClass', 'returns_pointer': 0, 'class': None, 'debug': 'OmegaClass ( ) ;', 'returns_class': False}
    protected
    private
    }
    
    
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
    [{'constant': 1, 'name': 'v1', 'reference': 1, 'type': 'const string &', 'static': 0, 'pointer': 0, 'desc': 'Variable 1'}, {'constant': 0, 'name': 'v2', 'reference': 1, 'type': 'vector<string> &', 'static': 0, 'pointer': 0, 'desc': 'Variable 2'}]
    
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
    


Contributors
------------
* Chris Love
* HartsAntler
