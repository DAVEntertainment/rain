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

RAIN_START()

Version::Version(
    uint32_t major,
    uint32_t minor,
    uint32_t patch,
    uint64_t build,
    const std::string& tag,
    const std::string& hash
) noexcept :
    m_major(major),
    m_minor(minor),
    m_patch(patch),
    m_build(build),
    m_tag(tag),
    m_hash(hash) {
}

std::string Version::GetFullVersion() const noexcept {
    std::stringstream ss;
    ss  << GetMajor() << "." << GetMinor() << "." << GetPatch();
    if (m_tag.size() > 0) {
        ss << "-" << m_tag;
    }
    if (m_hash.size() > 0) {
        ss << "[" << m_hash << "]";
    }
    if (m_build != 0) {
        ss << "(" << m_build << ")";
    }
    return ss.str();
}

uint32_t Version::GetMajor() const noexcept {
    return m_major;
}

uint32_t Version::GetMinor() const noexcept {
    return m_minor;
}

uint32_t Version::GetPatch() const noexcept {
    return m_patch;
}

uint64_t Version::GetBuild() const noexcept {
    return m_build;
}

const std::string& Version::GetTag() const noexcept {
    return m_tag;
}

const std::string& Version::GetHash() const noexcept {
    return m_hash;
}

RAIN_STOP()
