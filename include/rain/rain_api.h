/*****************************************************************************
 * rain_api.h: RAIN_API
 *****************************************************************************
 * Copyright (C) 2022 DAV Entertainment. All rights reserved
 *
 * Authors: Wu Wei <wuwei_543333827@126.com>
 *
 * Use of this source code is governed by a MIT license that can be
 * found in the LICENSE file.
 *****************************************************************************
 * Change History:
 *  2022-11-15      Wu Wei          Created
 *****************************************************************************/
#pragma once

#ifdef RAIN_STATIC_DEFINE
#  define RAIN_API
#  define RAIN_NO_EXPORT
#else
#  ifndef RAIN_API
#    ifdef RAIN_EXPORTS
#      define RAIN_API __declspec(dllexport)
#    else
#      define RAIN_API __declspec(dllimport)
#    endif
#  endif

#  ifndef RAIN_NO_EXPORT
#    define RAIN_NO_EXPORT
#  endif
#endif

#ifndef RAIN_DEPRECATED
#  define RAIN_DEPRECATED __declspec(deprecated)
#endif

#ifndef RAIN_DEPRECATED_EXPORT
#  define RAIN_DEPRECATED_EXPORT RAIN_API RAIN_DEPRECATED
#endif

#ifndef RAIN_DEPRECATED_NO_EXPORT
#  define RAIN_DEPRECATED_NO_EXPORT RAIN_NO_EXPORT RAIN_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef RAIN_NO_DEPRECATED
#    define RAIN_NO_DEPRECATED
#  endif
#endif
