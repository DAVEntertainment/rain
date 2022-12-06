/*****************************************************************************
 * current_version.h: Current Version
 *****************************************************************************
 * Copyright (C) 2022 DAV Entertainment. All rights reserved
 *
 * Authors: Wu Wei <wuwei_543333827@126.com>
 *
 * Use of this source code is governed by a MIT license that can be
 * found in the LICENSE file.
 *****************************************************************************
 * Change History:
 *  2022-12-02      Wu Wei          Created
 *****************************************************************************/
#pragma once
#include <string>
#include "rain/version.h"

RAIN_START()

class CurrentVersion final:
       public Version {
 public:
    explicit CurrentVersion();
};

RAIN_STOP()
