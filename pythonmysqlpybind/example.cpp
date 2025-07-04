#include <pybind11/pybind11.h>
#include <tuple> // 引入 tuple 头文件以返回多个值
#include <random> // 引入 random 头文件以生成随机数
#include <string> // 引入 string 头文件

// 修改函数，返回一个 double 0.01、一个随机四位数 int 和一个 string "xauusd"
std::tuple<double, int, std::string> f()
{
    // 固定 double 值为 0.01
    double double_num = 0.01;

    // 使用随机设备生成种子
    std::random_device rd;
    // 使用 Mersenne Twister 算法作为随机数引擎
    std::mt19937 gen(rd());
    // 生成 1000 到 9999 之间的随机四位数
    std::uniform_int_distribution<> dis_int(1000, 9999);
    int int_num = dis_int(gen);

    // 固定字符串为 "xauusd"
    std::string str = "xauusd";

    return std::make_tuple(double_num, int_num, str);
}

PYBIND11_MODULE(handsome, m)
{
    m.doc() = "a function returning a double 0.01, a random four - digit int and a string \"xauusd\"";
    m.def("get_tick", &f, "return a double 0.01, a random four - digit int and a string \"xauusd\"");
}
