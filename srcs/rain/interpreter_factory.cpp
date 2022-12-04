/*****************************************************************************
 * interpreter_factory.cpp: Interpreter factory
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
#include "rain/interpreter_factory.h"

RAIN_START()

IInterpreter* InterpreterFactory::Create(
    const std::string& product
) {
    if(product == kRain) {
        return nullptr;
    }
    return nullptr;
}

const std::vector<std::string> InterpreterFactory::GetProducts() const {
    std::vector<std::string> products {
        kRain
    };
    return products;
}

RAIN_STOP()
