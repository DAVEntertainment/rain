/*****************************************************************************
 * entry.cpp: Rain Entry
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

    if (nargs == 1) {
        // this output will eat the last line before this,
        //  don't know why, not digging
        std::cout << rain::StringLogo().GetLogo() << std::endl;
    } else {
        std::string version_tag("--version");
        for (int i = 0; i < nargs; ++i) {
            if (0 == version_tag.compare(args[i])) {
                auto v = rain::Version::CurrentVersion().GetFullVersion();
                std::cout << v << std::endl;
            }
        }
    }
    return 0;
}
