/*****************************************************************************
 * string_logo.h: String logo interface
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
#include "rain/i_string_convertible.h"

RAIN_START()

class IStringLogo:
    public IStringConvertible
{
};

RAIN_STOP()

