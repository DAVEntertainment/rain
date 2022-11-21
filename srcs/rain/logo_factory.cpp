/*****************************************************************************
 * logo_factory.cpp: Logo Factory
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
#include "rain/misc/rain_macros.h"
#include "rain/misc/string_logo.h"
#include "rain/logo_factory.h"

START_RAIN()

std::string LogoFactory::CreateStringLogo() const {
    StringLogo logo;
    return logo.GetLogo();
}

STOP_RAIN()
