#ifdef _WIN32
    #ifdef RAIN_EXPORT
        #define RAIN_API __declspec(dllexport)
    #else
        #define RAIN_API __declspec(dllimport)
    #endif
#else
    #define RAIN_API
#endif


#define START_NAMESPACE(ns)     namespace ns {
#define END_NAMESPACE()         }
