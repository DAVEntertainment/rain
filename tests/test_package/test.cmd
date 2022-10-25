set SOURCE_DIR=%~dp0
set BUILD_DIR=%SOURCE_DIR%\.build
set INSTALL_DIR=%BUILD_DIR%\.dist

set RAIN_SOURCE_DIR=%SOURCE_DIR%\..\..\srcs\
set RAIN_BUILD_DIR=%BUILD_DIR%\.build_rain

rmdir /s /q %BUILD_DIR%

cmake -S %RAIN_SOURCE_DIR% -B %RAIN_BUILD_DIR% -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR%
cmake --build %RAIN_BUILD_DIR% --config Release -j4 
cmake --install %RAIN_BUILD_DIR% --config Release

cmake -S %SOURCE_DIR% -B %BUILD_DIR% -DCMAKE_INSTALL_PREFIX=%INSTALL_DIR% -DCMAKE_PREFIX_PATH=%INSTALL_DIR%
cmake --build %BUILD_DIR% --config Release -j4
cmake --install %BUILD_DIR% --config Release

call %INSTALL_DIR%\bin\test_package.exe
