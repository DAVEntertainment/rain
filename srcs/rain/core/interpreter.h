/*****************************************************************************
 * interpreter.h: Interpreter
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
