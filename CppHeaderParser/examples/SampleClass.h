#include <vector>
#include <string>
using namespace std;
class SampleClass
{
public:
    SampleClass();
    string meth1();
    int meth2(int v1);
    void meth3(const string & v1, vector<string> & v2);
    unsigned int meth4();
private:
    void * meth5(){return NULL};
    string prop1;
    int prop5;
};