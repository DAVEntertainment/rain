#pragma once
#include "rain/misc/rain_macros.h"

START_RAIN();

class Interpreter final
{
public:
    Interpreter();
    ~Interpreter();
    void Interpret();
};

STOP_RAIN();
