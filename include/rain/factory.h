/*****************************************************************************
 * factory.h: Factory
 *****************************************************************************
 * Copyright (C) 2022 DAV Entertainment. All rights reserved
 *
 * Authors: Wu Wei <wuwei_543333827@126.com>
 *
 * Use of this source code is governed by a MIT license that can be
 * found in the LICENSE file.
 *****************************************************************************
 * Change History:
 *  2022-10-27      Wu Wei          Created
 *****************************************************************************/
#pragma once
#include "rain/rain_macros.h"
#include "rain/rain_api.h"

RAIN_START()

//!
//! class Factory
//!     Factory to create rain instance
//!
class RAIN_API Factory final {
 public:
    //! Create rain
    //! @fn void Factory::CreateRain()
    //! @brief Create default rain instance
    void CreateRain() {}
};

RAIN_STOP()
