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
#include "rain/misc/rain_macros.h"

START_RAIN()

//!
//! class StringLogo
//!     string logo creator
//!
class StringLogo final {
 public:
    //! Get Logo
    //! @fn void StringLogo::GetLogo()
    //! @brief Get string logo
    const std::string& GetLogo() const;
    //! Clone Logo
    //! @fn void StringLogo::CloneLogo()
    //! @brief Clone string logo
    std::string CloneLogo() const;
};

STOP_RAIN()
