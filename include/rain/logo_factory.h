/*****************************************************************************
 * logo_factory.h: Logo Factory
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
#include <string>
#include "rain/rain_api.h"

namespace rain {

//!
//! class LogoFactory
//!     Logo Factory
//!
class RAIN_API LogoFactory final {
 public:
    //! Create string logo
    //! @fn void LogoFactory::CreateStringLogo()
    //! @brief Create string logo
    std::string CreateStringLogo() const;
};

}  // namespace rain
