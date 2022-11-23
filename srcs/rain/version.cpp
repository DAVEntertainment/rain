/*****************************************************************************
 * version.cpp: Version
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
#include <sstream>
#include "rain/version.h"
#include "rain/version.def.h"

namespace rain {

std::string Version::GetFullVersion() const noexcept {
    std::stringstream ss;
    ss << GetMajor() << "." << GetMajor() << "." << GetMajor();
    return ss.str();
}

uint32_t Version::GetMajor() const noexcept {
    return RAIN_VERSION_MAJOR;
}

uint32_t Version::GetMinor() const noexcept {
    return RAIN_VERSION_MINOR;
}

uint32_t Version::GetPatch() const noexcept {
    return RAIN_VERSION_PATCH;
}

uint32_t Version::GetBuild() const noexcept {
    return RAIN_VERSION_BUILD;
}

std::string Version::GetTag() const noexcept {
    return RAIN_VERSION_TAG;
}

std::string Version::GetHash() const noexcept {
    return RAIN_VERSION_HASH;
}

}  // namespace rain
