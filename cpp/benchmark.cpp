#include <iostream>
#include <ctime>

using namespace std;

int main() {
    // 获取当前时间戳
    time_t t1 = time(0);

    int counter = 0;

    // 循环15亿次
    for (int i = 0; i < 1500000000; i++) {
        counter = counter + 1;
    }

    time_t t2 = time(0);
    cout << "执行时间：" << (t2 - t1) << "秒" << endl;

    return 0;
}
