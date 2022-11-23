/*****************************************************************************
 * version.h: Version
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
//! Version class, contains Rain Version Info
//!
class RAIN_API Version final {
 public:
    //!
    //! Get current version
    //!
    
    //!
    //! Get full version
    //!
    std::string GetFullVersion() const noexcept;
    //!
    //! Get major version
    //!
    uint32_t GetMajor() const noexcept;
    //!
    //! Get minor version
    //!
    uint32_t GetMinor() const noexcept;
    //!
    //! Get patch version
    //!
    uint32_t GetPatch() const noexcept;
    //!
    //! Get build version
    //!
    uint32_t GetBuild() const noexcept;
    //!
    //! Get tag
    //!
    std::string GetTag() const noexcept;
    //!
    //! Get hash
    //!
    std::string GetHash() const noexcept;
};

}  // namespace rain
