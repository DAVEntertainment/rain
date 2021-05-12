#include <iostream>

#include "rain/core/interpreter.h"

using namespace std;

START_RAIN()

Interpreter::Interpreter(){}

Interpreter::~Interpreter(){}

void Interpreter::Interpret(){
    cout << "joker" << endl;
}

STOP_RAIN()
