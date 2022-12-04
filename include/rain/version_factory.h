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
#include <string>
#include <vector>
#include "rain/rain_api.h"
#include "rain/rain_macros.h"
#include "rain/i_version.h"

RAIN_START()

class RAIN_API VersionFactory final {
 public:
    //!
    //! Create version
    //!
    IVersion* Create(
        const std::string& product
    );
    //!
    //! Get product list
    //!
    const std::vector<std::string> GetProducts() const;

 public:
    //!
    //! Product names
    //!
    const std::string kCurrent{"current"};
};

RAIN_STOP()

