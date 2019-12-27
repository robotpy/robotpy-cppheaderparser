#include <string.h>

#define DEBUG_PRINT(x)           \
	printf("---------------\n"); \
	printf("DEBUG: %d\n", x);    \
	printf("---------------\n");

#define DEBUG_PRINT2(x)          \
	printf("---------------\n"); \
	printf("DEBUG2: %d\n", x);   \
	printf("---------------\n");

void function1();

extern "c"
{
  int function2();
}

class Worm
{
public:
	Worm(string name);
	string getName()
	{
		return name;
	}
private:
	string name;
};
