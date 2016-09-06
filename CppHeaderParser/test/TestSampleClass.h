#include <vector>
#include <string>
using namespace std;
class SampleClass: public BaseSampleClass
{
public:
	enum Elephant
	{
		EL_ONE = 1,
		EL_TWO = 2,
		EL_NINE = 9,
		EL_TEN,
	};

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
     * \param v1 Variable 1 with a really long
     * wrapping description
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
    void * meth5(){return NULL;}

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
    protected:
    	typedef enum
    	{
    		Z_A,
    		Z_B = 0x2B,
    		Z_C = 'j',
			Z_D,
    	} Zebra;
    };

    namespace Omega
    {
		class OmegaClass
		{
		public:
			OmegaClass();

			string omegaString;
		protected:
			///
			/// @brief Rino Numbers, not that that means anything
			///
			typedef enum
			{
				RI_ZERO,
				RI_ONE,
				RI_TWO
			} Rino;
		};
    };
}

//Sample class for bug 3488053
class Bug_3488053
{
	public:
	class Bug_3488053_Nested
	{
	public:
		int x;
	};
};

// Bug 3488360
namespace Citrus
{
  class BloodOrange { };
}

class Bananna: public Citrus::BloodOrange
{
};

class ExcellentCake: private Citrus::BloodOrange, Convoluted::Nested::Mixin
{
};

// Bug 3487551
class Bug_3487551
{
public:
    virtual int method();
};


// Feature Request 3488051
struct SampleStruct
{
    unsigned int meth();
private:
    int prop;
};

// Bug 3488049 & Feature Request 3488050
const int MAX_ITEM = 7;
class Bird
{
int items[MAX_ITEM];
int otherItems[7];
int oneItem;
};

// Bug 3488054
class Monkey {
private:
static void Create();
};
inline void Monkey::Create() { }

// Bug 3488275
class Chicken
{
template <typename T> static T Get();
};
template <typename T> T Chicken::Get() { return T(); }

// Bug 3491240
class Lizzard {
Lizzard();
explicit Lizzard( int a );
};

// Bug 3491178
class Owl {
private:
template <typename T> int* tFunc( int count );
};

template <typename T> int* Owl::tFunc( int count ) {
if (count == 0) {
return NULL;
}
return NULL;
}

// Bug 3491232
class GrapeClass {
private:
struct GrapeStruct { };
int x;
void f();
};


// Bug 3491319
struct AnonHolderClass {
struct {
int x;
} a;
};


// Feature Request 3491220
class CowClass {};
struct CowStruct {};

// Bug 3491334
class BaseMangoClass { };
class MangoClass: virtual public BaseMangoClass { };

// Bug 3492237
const long MAX_LEN = 7;
class EagleClass {
int a[(int)MAX_LEN];
};

// Bug 3497164
class FrogClass {

    struct {
        int a;
    } x;

    struct {
        int b;
    } y;

    struct {
        int c;
    } z;

};

// Bug 3497160
class DogClass;
class CatClass {
    friend DogClass;
};

// Bug 3497155
extern "C" {
int FishA( const char* strA );
int FishB( const char* strB );
}

// Bug 3497168
class PandaClass {
static const int CONST_A = (1 << 7) - 1;
static const int CONST_B = sizeof(int);
};

// Bug 3497166
class PotatoClass {
    struct FwdStruct;
    FwdStruct* ptr;
    struct FwdStruct {
    	int a;
    };
};

// Bug 3497162
class HogClass {
	union HogUnion {
		int a;
		float b;
	} u;
};

// Bug 3497158
class CherryClass {
	template< int ID >
public:
	void CherryClass ();
	struct NestStruct {
	    void FuncA();
	    int val;
	};
};

// Bug 3517308
template<class T>
class GarlicClass
{
public:
	GarlicClass();
    int fun1(T);
    int fun2(T);
};

// Bug 3514728
class CarrotClass
{
int var1;
#define FIRSTLINE \
SECONDLINE
void fun1();
};

// Bug 3517289
extern "C" void f(int i, char c, float x);

extern "C" {
	int fun1(SP1, SP2);
	int fun2(SP1, SP2);

	class ExternClass
	{
		ExternClass();
	}
};

// Bug 3514671
struct OliveStruct{
	struct other* a;
	void* b;
	boolean c;
	int d;
};

// Bug 3515330
namespace RoosterNamespace
{
    class RoosterOuterClass
    {
    public:
        int member1;

        class RoosterSubClass1
        {
        public:
            int publicMember1;
        private:
            int privateMember1;
        };

    private:
        int member2;
        class RoosterSubClass2
        {
        public:
            int publicMember2;
        private:
            int privateMember2;
        };
    };
}


// Bug 3514672
class OperatorClass
{
public:
    void operator= (const Sample25Class&);
    void operator-= (const Sample25Class&);
    void operator+=();
    void operator[]();
    bool operator == (const int &b);
    operator+();
    void operator-();
    void operator*();
    void operator\();
    void operator%();
    void operator^();
    void operator|();
    void operator&();
    void operator~();
    void operator<<();
    void operator>>();
    void operator!=();
    void operator<();
    void operator>();
    void operator>=();
    void operator<=();
    void operator!();
    void operator&&();
    void operator||();
    void operator+=();
    void operator-=();
    void operator*=();
    void operator\=();
    void operator%=();
    void operator&=();
    void operator|=();
    void operator^=();
    void operator<<=();
    void operator>>=();
    void operator++();
    void operator--();
    void operator()();
    void operator->();
    void operator,();
};

// Feature request 3519502 & 3523010
class CrowClass
{
public:
    int meth();

public slots:
    void testSlot(int i);
};

// Bug 3497170
struct DriverFuncs {
    void* (*init) ();
    void (*write) (void *buf, int buflen);
};

// Bug 3519178
template<class T> SnailTemplateClass
{
};

namespace SnailNamespace2
{
    class SnailClass
    {
    };
}

class Snail2Class
{
public:
    SnailNamespace::SnailClass meth(tr1::shared_ptr<SnailTemplateClass<SnailNamespace::SnailClass> >);
};

// Feature Request 3523198
class QualeClass : public QObject
{
    Q_OBJECT
    void func();
};

// Feature Request 3523235
class RockClass
{
    int getNum() const;
    int getNum2();
};

// Bug 3523196
class AlmondClass
{
public:
    std::map<unsigned, std::pair<unsigned, SnailTemplateClass<SnailNamespace::SnailClass> > > meth(bool flag,
            std::map<unsigned, std::pair<unsigned, SnailTemplateClass<SnailNamespace::SnailClass> > > bigArg);
};

// Bug 3524327
class StoneClass
{
    virtual int getNum2() const = 0;
    int getNum3();
};

// Bug 3531219
class Kangaroo
{
public:
    Kangaroo() {
    }
    class Joey
    {
    public:
        Joey();
    };
};


// Bug 3535465
class Ant
{
public:
    Ant(uint index, const FiniteElement& element, const ufc::cell& cell)
      : index(index), element(element), cell(cell) {}

	Ant(MeshEntity& entity) : MeshEntity(entity.mesh(), 1, entity.index())
	{}
};

// Bug 3536069
template <typename Plant> struct Onion<Red,Plant>
{
    int i;
};

template <typename Plant> struct Onion<Sweet,Plant>
{
    int i;
};

// Bug 3536067
class BlueJay : public Bird, public virtual Food
{
public:
    BlueJay() {}
};

// Bug 3536071
class Pea : public Vegetable<Green>
{
	int i;
}


// Bug 3567172
class Pear
{
	enum Stem stem_property;
}

// Bug 3567854 and 3568241
struct Beans
{
    UINT16 hdr;
    union
    {
        UINT16 typeA;
        UINT16 typeB;
        UINT16 raw[3];
    };
    UINT32 data[204];
    union
    {
        UINT16 typeC;
        UINT16 typeD;
        UINT16 raw[3];
    };
};

// Bug 3568629
void termite(void)
{
    return ((structA*) (Func())->element);
}

// Bug 3569622
class Japyx
{
public:
    enum enum1
    {
        e1, // 00
        e2, // 01
    };
    UINT32 a;
};

void japyxFunc(struct s1 *pS, Japyx::enum1 x, MYTYPE myVar);

// Bug 3570105
enum Author
{
    NAME = ('J' << 24 | \
    'A' << 16 | \
    'S' << 8 | \
    'H'),
};

// Bug 3577484
template <> class FruitFly<int>: public Fly { };

// Bug BitBucket #2
MAGIC_BEGIN_MACRO(glitter, int)
  NOT_FINISHED,
  FINISHED
MAGIC_END_MACRO(glitter)

class ClassAfterMagicMacro
{
public:
  ClassAfterMagicMacro();
}

// Bug BitBucket #4
typedef unsigned int uint;
typedef char ** string_array;
typedef std::tr1::shared_ptr< ObjPtr > SmartObjPtr;
typedef std::map<std::string, std::string> StrStrMap;

class AfterTypedefClass
{
  public:
}

// Bug BitBucket #6
class LineNumAfterDivide
{
  static int func1(float alpha_num)
  { return funcX(alpha_num /
                 beta_num); }
  void func2();
};

// Bug BitBucket #5
class Herb
{
};

class Herb::Cilantro : public Plant
{
};

// Bug BitBucket #7
#include <iostream>
int print_statement() {
    cout << "Heyyy" << endl;
}

// Bug BitBucket #8
class Garlic {
public:
    friend int genNum(C& a)
    {
      return obj.meth().num();
    }
};

// Bug SourceForge #54
enum Wheat
{
   w1,
   w2,
   w3,
} __attribute__((packed));


// Bug SourceForge #55
class Peach
{
  int abc;
};

class Plumb
{
  class Peach * doSomethingGreat( class Peach * pInCurPtr );
  class Peach * var;
};

class Peach * Plumb::myMethod( class Peach * pInPtr )
{
  return pInPtr;
}

// Bug BitBucket #9
class Grape
{
public:
    int a, b,c;
    map<string, int> d;
    map<string, int> e, f;
};

// Bug BitBucket #14
struct Avacado {
    uint8_t foo() { return 4;}
    ::uint8_t bar() { return 0; }
};

// Bug BitBucket #13
typedef struct
{
    int anon_struct_variable;
};

typedef struct
{
    int a;
} Raspberry;

// Bug BitBucket #15 & 16
class Hen
{
public:
	void add(int a=100, b=0xfd, float c=1.7e-3, float d=3.14);
	void join(string s1="", string s2="nothing");
}

// Bug BitBucket #19
template<typename VALUE,
         typename VALUE_SET_ITERATOR,
         typename ACCESOR=Raddish::SimpleAccessor<VALUE,VALUE_SET_ITERATOR> >
class Raddish_SetIterator : public Raddish_Iterator<VALUE>
{
protected:
  VALUE_SET_ITERATOR _beg, _end;
public:
  Raddish_SetIterator(const VALUE_SET_ITERATOR & begin,
                   const VALUE_SET_ITERATOR & end)
  { init ( begin, end ); }

};

// Bug 57
typedef enum{StarFruit = (2 + 2) / 2} Carambola;

// Add support for globals
extern int externVar;
int globalVar;

// BitBucket bug 22
typedef char TenCharArray[10];

// Support typedef structs
typedef struct SUPER_MAGIC_FILE MAGIC_FILE;
typedef struct _IO_FILE FILE;

// Sourceforge issue #10: Multi dimensional array sizes
struct Picture
{
    char name[25];
    unsigned int pdata[128][128];
};

// SourceForge bug 58
typedef union apricot_t
{
   int i;
   float f;
   char s[20];
}Apricot;

// SourcForge bug 59
struct Lemon
{
    virtual void foo() final;
    virtual void foo2();
};
 
struct Lime final : Lemon
{
    void abc();
    void foo2() override;
};

// BitBucket bug 24
namespace MouseNS
{
  class MouseClass
  {
   public:
    typedef std::vector<int> mouse_typedef;
    void meth(mouse_typedef *tptr) {};
  };
};

// BitBucket bug 26
typedef struct Fig {
    int a;
} Fig;

// BitBucket bug 27
union olive {
    int x;
};

// Sourceforge bug 61
typedef struct
{ 
    enum BeetEnum : int 
    { 
        FAIL = 0,
        PASS = 1
    }; 
} BeetStruct;