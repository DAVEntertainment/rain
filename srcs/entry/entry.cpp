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


const char* logo = " It's raining ...                                 \n"
"                                                                     \n"
"                                                                     \n"
"                    |   |                      |                     \n"
"                  |      |         |                                 \n"
"                        |             |                              \n"
"                |                         |                          \n"
"                      |         |        |                           \n"
"                     |    ___---___                                  \n"
"                  __---```  `   `   ```---__                         \n"
"         |__---```     `   `     `    `     ```---__                 \n"
"  ___---``         `      `       `       `         ``---___         \n"
"         ```  ---  ___   `         `   ___   ---    ```              \n"
"                         ````|| ````                                 \n"
"                             ||                   ___     ____       \n"
"                             ||                 /    /   /    /      \n"
"                             ||                |    /   |    /       \n"
"                             ||               |    |___|    |        \n"
"                             ||             /                 \\     \n"
"                             ||            / ____       ____   \\    \n"
"                             ||            /   /x\\   /   /x\\  |    \n"
"                            _||             \\__\\x/    \\__\\x/     \n"
"                           | ||`             \\                /     \n"
"                            ```                                      \n"
"                                                                     \n";


int main(int nargs, char* args[]) {
    rain::Factory factory;
    factory.CreateRain();
    if (nargs == 1) {
        std::cout << logo << std::endl;
    }
    return 0;
}
