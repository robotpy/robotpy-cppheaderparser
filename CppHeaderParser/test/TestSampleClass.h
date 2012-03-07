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
