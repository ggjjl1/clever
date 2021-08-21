#include <iostream>
#include <string.h>

using namespace std;

string gen_random() {
    char s[64];
    memset(s,0,sizeof(s));
    int len = 16;

    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i < len; ++i) {
        s[i] = alphanum[rand() % (sizeof(alphanum) - 1)];
    }

    s[len] = 0;
    return string(s);
}

int main() {

    // ofstream outfile;
    // outfile.open("data.txt");
    
    // for (int i = 0; i < 1000; i++) {
    //     outfile << "test file write" << endl;
    // }

    // 关闭文件
    // outfile.close();

    // int array[10] = {100, 10, 1, 99, 77, 55, 33, 11, 2, 4};

    // for(int i = 0; i < 10; i++) {
    //     cout << array[i] << endl;
    // }
    
    // string str1 = gen_random();
    // cout << str1 << endl;

    int var1;
    char var2[10];

    cout << "变量var1内存地址：" << &var1 << endl;
    cout << "变量var2内存地址：" << &var2 << endl;

    return 0;
}