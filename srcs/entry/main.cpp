#include <iostream>
#include "rain/core/macros.h"
#include "rain/core/interpreter.h"

using namespace std;
using namespace rain;

int main(int nargs, char* args[])
{
    for(int i = 0; i < nargs; ++i) {
        cout << "arg " << i << " " << args[i] << endl;
    }
    Interpreter it;
    it.Interpret();
    return 0;
}
