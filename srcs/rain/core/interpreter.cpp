/*****************************************************************************
 * interpreter.cpp: Interpreter
 *****************************************************************************
 * Copyright (C) 2022 DAV Entertainment. All rights reserved
 *
 * Authors: Wu Wei <wuwei_543333827@126.com>
 *
 * Use of this source code is governed by a MIT license that can be
 * found in the LICENSE file.
 *****************************************************************************
 * Change History:
 *  2022-10-27      Wu Wei          Created
 *****************************************************************************/
#include <iostream>
#include "rain/core/interpreter.h"

RAIN_START()

Interpreter::Interpreter() {}

Interpreter::~Interpreter() {}

void Interpreter::Interpret() {
    ::std::cout << "joker" << ::std::endl;
}

RAIN_STOP()
