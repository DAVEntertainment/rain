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
#include "rain/rain_macros.h"
#include "rain/i_version.h"

RAIN_START()

//!
//! Version class, contains Rain Version Info
//!
class Version:
   public IVersion
{
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
       const std::string& hash = "0000000000000000000000000000000000000000")
    noexcept;

    virtual ~Version();

 public:
    //!
    //! Get current version
    //!
    static const Version& CurrentVersion() noexcept;
    //!
    //! Get full version
    //!
    virtual std::string GetFullVersion() const noexcept override;
    //!
    //! Get major version
    //!
    virtual uint32_t GetMajor() const noexcept override;
    //!
    //! Get minor version
    //!
    virtual uint32_t GetMinor() const noexcept override;
    //!
    //! Get patch version
    //!
    virtual uint32_t GetPatch() const noexcept override;
    //!
    //! Get build version
    //!
    virtual uint64_t GetBuild() const noexcept override;
    //!
    //! Get tag
    //!
    virtual const std::string& GetTag() const noexcept override;
    //!
    //! Get hash
    //!
    virtual const std::string& GetHash() const noexcept override;

 public:
    // TODO(Wu Wei): support version compare
};

RAIN_STOP()
