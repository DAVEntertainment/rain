/*****************************************************************************
 * i_string_convertible.h: Interpreter interface
 *****************************************************************************
 * Copyright (C) 2022 DAV Entertainment. All rights reserved
 *
 * Authors: Wu Wei <wuwei_543333827@126.com>
 *
 * Use of this source code is governed by a MIT license that can be
 * found in the LICENSE file.
 *****************************************************************************
 * Change History:
 *  2022-12-01      Wu Wei          Created
 *****************************************************************************/
#pragma once
#include <string>
#include "rain/rain_macros.h"

RAIN_START()

class IStringConvertible {
 public:
    virtual std::string ToString() const = 0;
};

RAIN_STOP()
