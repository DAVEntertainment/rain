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
#include <string>
#include <vector>
#include "rain/rain_api.h"
#include "rain/rain_macros.h"
#include "rain/i_string_logo.h"

RAIN_START()

class RAIN_API StringLogoFactory final {
 public:
    //!
    //! Create string logo
    //!
    IStringLogo* Create (
        const std::string& product
    );
    //!
    //! Destroy string logo
    //!
    bool Destroy (
        IStringLogo* logo
    );
    //!
    //! Get product list
    //!
    const std::vector<std::string> GetProducts() const;

 public:
    //!
    //! Product names
    //!
    const std::string kRain{"rain"};
};

RAIN_STOP()

