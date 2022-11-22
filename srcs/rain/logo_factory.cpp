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
#include "rain/misc/string_logo.h"
#include "rain/logo_factory.h"

namespace rain {

std::string LogoFactory::CreateStringLogo() const {
    return StringLogo().GetLogo();
}

}  // namespace rain
