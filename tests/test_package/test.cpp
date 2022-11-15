/*****************************************************************************
 * test.h: Test package entry
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
#include <iostream>
#include "rain/rain.h"

int main(int nargs, char* args[]) {
    rain::Factory factory;
    factory.CreateRain();
    std::cout << "factory called" << std::endl;
    return 0;
}
