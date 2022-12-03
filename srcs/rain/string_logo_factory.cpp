/*****************************************************************************
 * string_logo_factory.h: String logo factory
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
#include "rain/string_logo_factory.h"
#include "rain/string_logo.h"

RAIN_START()

IStringLogo* StringLogoFactory::Create (
    const std::string& product
) const {
    if (product == kRain) {
        return new StringLogo();
    }
    return nullptr;
}

bool StringLogoFactory::Destroy(
    IStringLogo* logo
) const {
    if (nullptr != logo) {
        delete logo;
    }
    return true;
}

const std::vector<std::string>& StringLogoFactory::GetProducts() const {
    std::vector<std::string> products {
        kRain
    };
    return products;
}

RAIN_STOP()
