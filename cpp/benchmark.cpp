#include <iostream>
// #include <ctime>
#include<sys/timeb.h>
using namespace std;

long long millitime() {
    timeb t;
    ftime(&t);
    return t.time * 1000 + t.millitm;
}

int main() {
    // 获取当前时间戳
    // time_t t1 = time(0);
    long long start = millitime();

    int counter = 0;

    // 循环1.5亿次
    for (int i = 0; i < 150000000; i++) {
        counter = counter + 1;
    }

    // time_t t2 = time(0);
    // cout << "执行时间：" << (t2 - t1) << "秒" << endl;
    long long end = millitime();
    cout << "执行时间：" << end - start << "毫秒" << endl;

    return 0;
}
