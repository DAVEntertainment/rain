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
#include "rain/rain_macros.h"

RAIN_START()

//!
//! Version class, contains Rain Version Info
//!
class RAIN_API Version final {
 private:
    uint32_t m_major{0};
    uint32_t m_minor{0};
    uint32_t m_patch{0};
    uint64_t m_build{0};
    std::string m_tag{""};
    std::string m_hash{"0000000000000000000000000000000000000000"};

 public:
    explicit Version(
       uint32_t major = 0,
       uint32_t minor = 0,
       uint32_t patch = 0,
       uint64_t build = 0,
       const std::string& tag = "",
       const std::string& hash = "")
    noexcept;

 public:
    //!
    //! Get current version
    //!
    static const Version& CurrentVersion() noexcept;
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
    uint64_t GetBuild() const noexcept;
    //!
    //! Get tag
    //!
    const std::string& GetTag() const noexcept;
    //!
    //! Get hash
    //!
    const std::string& GetHash() const noexcept;

 public:
    // TODO(Wu Wei): support version compare
};

RAIN_STOP()
