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
#include "rain/rain_api.h"

namespace rain {

//!
//! class StringLogo
//!     string logo creator
//!
class RAIN_API StringLogo final {
 public:
    //! Get Logo
    //! @fn void StringLogo::GetLogo()
    //! @brief Get string logo
    std::string GetLogo() const noexcept;
};

}  // namespace rain
