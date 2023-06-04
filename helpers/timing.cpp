#include <chrono>
#include <utility>



template<typename F, typename... Args>
double func_time_ms(F func, Args&&... args) {
    auto t1 = std::chrono::high_resolution_clock::now();

    func(std::forward<Args>(args)...);

    auto duration = std::chrono::high_resolution_clock::now() - t1;
    return std::chrono::duration_cast<std::chrono::milliseconds>(duration).count();
}


template<typename F, typename... Args>
double func_time_ns(F func, Args&&... args) {
    auto t1 = std::chrono::high_resolution_clock::now();

    func(std::forward<Args>(args)...);

    auto duration = std::chrono::high_resolution_clock::now() - t1;
    return std::chrono::duration_cast<std::chrono::nanoseconds>(duration).count();
}
