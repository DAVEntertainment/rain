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
#include <memory>
#include "rain/rain.h"

int main(int nargs, char* args[]) {
    if (1 == nargs) {
        rain::StringLogoFactory factory;
        std::shared_ptr<rain::IStringLogo> logo(factory.Create(factory.kRain));
        std::cout << logo->ToString() << std::endl;
        return 0;
    }

    std::string versionTag("--version");
    for (int i = 0; i < nargs; ++i) {
        if (0 == versionTag.compare(args[i])) {
            rain::VersionFactory factory;
            std::shared_ptr<rain::IVersion> v(factory.Create(factory.kCurrent));
            std::cout << v->GetFullVersion() << std::endl;
            return 0;
        }
    }

    std::string file(args[1]);
    std::cout << "using " << file << std::endl;
    std::ifstream istm(file, std::ios::in | std::ios::binary);
    if (!istm.is_open()) {
        std::cout << "failed to open file" << std::endl;
    } else {
        std::stringstream ss;
        ss << istm.rdbuf();
        istm.close();
        std::string content = ss.str();
        std::cout << content << std::endl;
        rain::InterpreterFactory factory;
        std::shared_ptr<rain::IInterpreter> interpreter(
            factory.Create(factory.kRain));
        interpreter->Parse(content);
    }
    return 0;
}
