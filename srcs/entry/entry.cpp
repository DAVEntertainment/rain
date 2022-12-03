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

    if (1 == nargs) {
        rain::StringLogoFactory factory;
        auto logo = factory.Create(factory.kRain);
        std::cout << logo->ToString() << std::endl;
        factory.Destroy(logo);
    } else {
        std::string version_tag("--version");
        for (int i = 0; i < nargs; ++i) {
            if (0 == version_tag.compare(args[i])) {
                rain::VersionFactory factory;
                auto v = factory.Create(factory.kCurrent);
                std::cout << v->GetFullVersion() << std::endl;
                factory.Destroy(v);
            }
        }
    }
    return 0;
}
