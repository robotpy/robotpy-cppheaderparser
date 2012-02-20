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
