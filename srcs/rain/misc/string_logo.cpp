/*****************************************************************************
 * string_logo.cpp: String logo
 *****************************************************************************
 * Copyright (C) 2022 DAV Entertainment. All rights reserved
 *
 * Authors: Wu Wei <wuwei_543333827@126.com>
 *
 * Use of this source code is governed by a MIT license that can be
 * found in the LICENSE file.
 *****************************************************************************
 * Change History:
 *  2022-11-22      Wu Wei          Created
 *****************************************************************************/
#include "rain/misc/string_logo.h"

START_RAIN()

static const char logo[] = "It's raining ...                          \n"
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

const std::string& StringLogo::GetLogo() const {
    return logo;
}

std::string StringLogo::CloneLogo() const {
    return logo;
}

STOP_RAIN()
