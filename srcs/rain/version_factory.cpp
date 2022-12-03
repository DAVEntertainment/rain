/*****************************************************************************
 * version_factory.h: Version factory
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
#include "rain/current_version.h"
#include "rain/version_factory.h"

RAIN_START()

IVersion* VersionFactory::Create(const std::string& product) const {
    if(product == kCurrent) {
        return new CurrentVersion();
    }
    return nullptr;
}

bool VersionFactory::Destroy(IVersion* version) const {
    delete version;
    return true;
}

const std::vector<std::string>& VersionFactory::GetProducts() const {
    std::vector<std::string> products {
        kCurrent
    };
    return products;
}

RAIN_STOP()
