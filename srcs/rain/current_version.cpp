/*****************************************************************************
 * current_version.cpp: Current Version
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
#include "rain/version.def.h"
#include "rain/current_version.h"

RAIN_START()

CurrentVersion::CurrentVersion():
   Version(
      RAIN_VERSION_MAJOR,
      RAIN_VERSION_MINOR,
      RAIN_VERSION_PATCH,
      RAIN_VERSION_BUILD,
      RAIN_VERSION_TAG,
      RAIN_VERSION_HASH
   )
{

}

RAIN_STOP()
