/*****************************************************************************
 * i_version.h: Version interface
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
#include <string>
#include "rain/rain_macros.h"

RAIN_START()

class IVersion {
 public:
    //!
    //! Get full version
    //!
    virtual std::string GetFullVersion() const noexcept = 0;
    //!
    //! Get major version
    //!
    virtual uint32_t GetMajor() const noexcept = 0;
    //!
    //! Get minor version
    //!
    virtual uint32_t GetMinor() const noexcept = 0;
    //!
    //! Get patch version
    //!
    virtual uint32_t GetPatch() const noexcept = 0;
    //!
    //! Get build version
    //!
    virtual uint64_t GetBuild() const noexcept = 0;
    //!
    //! Get tag
    //!
    virtual const std::string& GetTag() const noexcept = 0;
    //!
    //! Get hash
    //!
    virtual const std::string& GetHash() const noexcept = 0;
};

RAIN_STOP()
