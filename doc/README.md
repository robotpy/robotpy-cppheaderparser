# CppHeaderParser

CppHeaderParser is a parser of C++ header files developed in Python.  
In order to use CppHeaderParser, it is just required to create an instance of the python class CppHeader, we will see in this documentation how to retrieve the data you need from the CppHeader class instance : 

```python
import CppHeaderParser

header = CppHeaderParser.CppHeader("path/to/cpp_header_file.hh") 
# CppHeaderParser will then parse the header file and you can use the header instance to access the informations you need
```

## CppHeader object overview

For example purpose we are going to use this [testing header file](https://github.com/robotpy/robotpy-cppheaderparser/blob/master/CppHeaderParser/examples/SampleClass.h) as sample for the below json.
CppHeader is composed of multiple member (we can easily print everything thanks to the toJSON method proposed by the CppHeader object):  

```python
import CppHeaderParser

header = CppHeaderParser.CppHeader("path/to/SampleClass.hh") 
print (header.toJSON)
```
<details>
  <summary>The above python code would result in this output (Click to expand!)</summary>

```json

```
</details>
As you can see, it this parser is trying to extract most of the information possible from the header file. From the programmatically interesting ones (classes name, methods name, arguments type and so on...) to the contextual one (line number of declaration, doxygen documentation and so on).  

# Content details

The following documentation is not fully up to date, only to main (and most important) keys are present, feel free to provide any improvement to this documentation if needed.   
We are now going to detail the possible content of CppHeaderParser:

* [includes](#includes) 
* [defines](#defines) 
* [classes](#classes) 
    * [methods](#methods)
    * [properties](#properties)
* [functions](#functions)


## includes

"includes" is an array of string containing all the includes of the header file.

<details>
  <summary>example (Click to expand!)</summary>

~~~ cpp
// includeTest.hh
#include <vector>
#include <string>
#include <memory>
~~~  

~~~ python
cppHeader = CppHeaderParser.CppHeader("includeTest.hh") 
print("\nincludes are:")
for incl in cppHeader.includes:
    print(" %s"%incl)

## output :

#includes are:
# <vector>
# <string>
# <memory>
~~~  

</details>

## defines

"defines" is an array of string containing all the defines of the header file.

<details>
  <summary>example (Click to expand!)</summary>

~~~ cpp
// defineTest.hh
#define OKOK "I am a define"
#define VADOR "isDark"
~~~  

~~~ python
cppHeader = CppHeaderParser.CppHeader("defineTest.hh") 
print("\ndefines are:")
for define in cppHeader.defines:
    print(" %s"%define)

## output :

#defines are:
# OKOK "I am a define"
# VADOR "isDark"
~~~  

</details>

## classes

"classes" is stored as a map of className (string) on a python dictionaries containing the details about a specific class, those dictonnaries contains those [data](#class-data).

## class data

* **"name"**        : string : name of the class
* **"inherits"**    : array of string : containing all the class that the class inherit from     
* **"declaration_method"** : string : how the class has been declared (as a structure of a class)
* **"abstract"**    : bool  : set to true if the class is defined as abstract
* **"final"**       : bool  : set to true if the class is defined as final
* **"typedefs : "** : describe todo 
* **"structs : "**  : describe todo
* **"enums : "**    : describe todo
* **"nested_classes"** : describe todo
* **"line_number"** : int : line at which the class has been declared in the header file
* **"methods"**     : containing all the methods of the class, described in more details [here](#methods).
* **"properties"**  : containing all the properties of the class, described in more details [here](#properties).

## methods

"methods" is a dictionnary containing different array, those contains dictionaries with the details of a each specific method, this dictionary contains the keys representing the accessibility of the method (encapsulation):  
* **"public"**   : array containing all the public methods, described in more details [here](#functions)    
* **"private"**  : array containing all the private methods, described in more details [here](#functions)  
* **"protected"**: array containing all the protected methods, described in more details [here](#functions)  

<details>
  <summary>example (Click to expand!)</summary>

~~~ cpp
// TestingMethod.hh
class TestingMethod {
public:
    void pubMethod1();
    void pubMethod2();

private:
    void privMethod1();
    void privMethod2();
    void privMethod3();

protected:
    void protecMethod1();
};
~~~

~~~ python
header = CppHeaderParser.CppHeader("TestingMethod.hh") 
# access data
len(header.classes)                  # equal 1 (only one class defined)
len(header.classes[0]["public"])     # equal 2 (2 public methods in the first class defined)
len(header.classes[0]["private"])    # equal 3 (3 private methods in the first class defined)
len(header.classes[0]["protected"])  # equal 1 (1 protected method in the first class defined)
~~~

</details>

Those arrays are python dictionaries containing all the details about a specific method, those dictionaries contains the following keys:  
* **"parent"**      : [class data](#class-data) : data related to the class owning this method
* **"rtnType"**     : string : return type of the method
* **"name"**        : string : name of the method
* **"parameters"**  : custom : parameters of the function, described in more details [here](#parameter-type)
* **"doxygen"**     : string : documentation above the method  
* **"namespace"**   : string : namespace of the class (doesn't contains the name of the class)  
* **"path"**        : string : give the name composed of the namespace, the class name, and the method name.
* **"debug"**       : string : give the exact string representing the method declaration
  
* **"defined"**     : bool  : set to true if the method is directly defined in the header file  
* **"operator"**    : bool  : set to true if the method is an operator overload
* **"constructor"** : bool  : set to true if the method is the constructor of the class
* **"destructor"**  : bool  : set to true if the method is the destructor of the class
* **"pure_virtual"**: bool  : set to true if the method is a pure virtual method
* **"static"**      : bool  : set to true if the method is declared as static
* **"final"**       : bool  : set to true if the method is declared as final  
* **"explicit"**    : bool  : set to true if the method is declared as explicit
* **"template"**    : bool  : set to true if the method is templated 
* **"friend"**      : bool  : set to true if the method is declared as friend  
* **"inline"**      : bool  : set to true if the method is declared as inlined  
* **"extern"**      : boo   : set to true if the method is declared as extern
  
* **"returns_pointer"**     : bool  : set to true if the method return a pointer.  
* **"returns_fundamental"** : bool  : set to true if the method return a primitive type (fundamental).  
* **"returns_reference"**   : bool  : set to true if the method return a reference.
* **"returns_class"**       : bool  : set to true if the method return a class object.

* **"line_number"**         : int : line at which the method has been declared in the header file
  
## properties

"properties" is a dictionnary containing different array, those contains dictionaries with the details of a each specific property, this dictionary contains the keys representing the accessibility of the properties (encapsulation):  
* **"public"**   : array containing all the public properties    
* **"private"**  : array containing all the private properties  
* **"protected"**: array containing all the protected properties 

A property dictionary contained in those arrays contains the following keys:  
* **"name"**              : string : name of the property  
* **"type"**              : string : type of the property   
* **"constant"**          : bool   : 
* **"fundamental"**       : bool   : boolean to check if the type is a fundamental one (primitive type)  
* **"namespace"**         : string : namespace in which is the class that contains this property (doesn't contains the name of the class)  
* **"property_of_class"** : string : class name that owns this property (class name without namespace)  
* **"doxygen"**           : string : documentation above the property  
* **"line_number"**       : int    : line number of the declaration of the property  

## parameter type

## functions

"functions" is stored as an array of python dictionaries containing all the details about a specific function, those dictionaries contains the following keys:  
* **"returns"**     : string : return type   
* **""**
* **""**
* **"defined"**     : bool  : set to true if the function is directly defined in the header file  
* **"inline"**      : bool  : set to true if the function is declared as inlined  


## Used By

CppHeaderParser is currently used by different projects[^1]: 
* [FSeam](https://github.com/FreeYourSoul/FSeam/) : A mocking library using the parser in order to generate mocking version of a class
* []() 

[^1] if you also use CppHeaderParser, don't hesitate to provide a pull request in order to update the following list
