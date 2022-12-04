/*****************************************************************************
 * interpreter_factory.h: Interpreter factory
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
#include <vector>
#include <string>
#include "rain/rain_macros.h"
#include "rain/rain_api.h"
#include "rain/i_interpreter.h"

RAIN_START()

class RAIN_API InterpreterFactory final {
 public:
    //!
    //! Create interpreter
    //!
    IInterpreter* Create(
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
    const std::string kRain{"rain"};
};

RAIN_STOP()
