#include <iostream>
#include "rain/rain.h"

using namespace std;
using namespace rain;

int main(int nargs, char* args[])
{
    Factory factory;
    factory.Call();
    cout << "factory called" << endl;
    return 0;
}
