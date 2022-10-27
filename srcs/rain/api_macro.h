/*****************************************************************************
 * api_macro.h: API Macros
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

#ifdef _WIN32
    #ifdef RAIN_EXPORT
        #define RAIN_API __declspec(dllexport)
    #else
        #define RAIN_API __declspec(dllimport)
    #endif
#else
    #define RAIN_API
#endif
