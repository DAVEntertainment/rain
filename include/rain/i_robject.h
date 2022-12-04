/*****************************************************************************
 * i_robject.h: RObject(Rain Object) interface
 *****************************************************************************
 * Copyright (C) 2022 DAV Entertainment. All rights reserved
 *
 * Authors: Wu Wei <wuwei_543333827@126.com>
 *
 * Use of this source code is governed by a MIT license that can be
 * found in the LICENSE file.
 *****************************************************************************
 * Change History:
 *  2022-12-04      Wu Wei          Created
 *****************************************************************************/
#pragma once
#include <string>
#include "rain/rain_macros.h"
#include "rain/i_string_convertible.h"

RAIN_START()

class IRObject:
    public IStringConvertible
{
 public:
    //!
    //! Get type name of RObject
    //!
    virtual std::string GetType() const noexcept = 0;
    //!
    //! Get class name of RObject
    //!
    virtual std::string GetClassName() const noexcept = 0;
    //!
    //! Get attribute
    //!
    virtual IRObject* GetAttribute(
        const std::string name
    ) const = 0;
    //!
    //! Set attribute
    //!
    virtual void SetAttribute(
        const std::string name,
        IRObject* value
    ) const = 0;
    //!
    //! Is RObject callable ?
    //!
    virtual bool IsCallable() const noexcept = 0;
    //!
    //! Call RObject as a function
    //!
    // virtual IRObject* Call() = 0;
};

RAIN_STOP()
