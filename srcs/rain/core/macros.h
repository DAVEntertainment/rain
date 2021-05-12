#ifdef _WIN32
    #ifdef RAIN_EXPORT
        #define RAIN_API __declspec(dllexport)
    #else
        #define RAIN_API __declspec(dllimport)
    #endif
#else
    #define RAIN_API
#endif

#define START_RAIN()    namespace rain {
#define STOP_RAIN()     }
