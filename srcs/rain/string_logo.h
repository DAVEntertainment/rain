/*****************************************************************************
 * string_logo.h: String logo
 *****************************************************************************
 * Copyright (C) 2022 DAV Entertainment. All rights reserved
 *
 * Authors: Wu Wei <wuwei_543333827@126.com>
 *
 * Use of this source code is governed by a MIT license that can be
 * found in the LICENSE file.
 *****************************************************************************
 * Change History:
 *  2022-11-22      Wu Wei          Created
 *****************************************************************************/
#pragma once
#include <string>
#include "rain/rain_macros.h"
#include "rain/i_string_logo.h"

RAIN_START()

class StringLogo final:
    public IStringLogo
{
 public:
    std::string ToString() const override;
};

RAIN_STOP()
