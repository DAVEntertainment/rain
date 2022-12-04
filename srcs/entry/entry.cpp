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
#include <fstream>
#include <sstream>
#include "rain/rain.h"

int main(int nargs, char* args[]) {
    if (1 == nargs) {
        rain::StringLogoFactory factory;
        auto logo = factory.Create(factory.kRain);
        std::cout << logo->ToString() << std::endl;
        delete logo;
    } else if (2 == nargs) {
        std::string file(args[1]);
        std::cout << "using " << file << std::endl;
        std::ifstream istm(file, std::ios::in | std::ios::binary);
        if (!istm.is_open()) {
            std::cout << "failed to open file" << std::endl;
        } else {
            std::stringstream ss;
            ss << istm.rdbuf();
            std::cout << ss.str() << std::endl;
        }
    } else {
        std::string version_tag("--version");
        for (int i = 0; i < nargs; ++i) {
            if (0 == version_tag.compare(args[i])) {
                rain::VersionFactory factory;
                auto v = factory.Create(factory.kCurrent);
                std::cout << v->GetFullVersion() << std::endl;
                delete v;
            }
        }
    }
    return 0;
}
