#include <iostream>
#include <fstream>
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

    ofstream outfile;
    // outfile.open("data.txt");

    // int array[10] = {100, 10, 1, 99, 77, 55, 33, 11, 2, 4};

    // for(int i = 0; i < 10; i++) {
    //     cout << array[i] << endl;
    // }
    
    // string str1 = gen_random();
    // cout << str1 << endl;

    string filename;

    cout << "请输入文件路径：";
    cin >> filename;
    cout << "输入的文件路径名为：" << filename << endl;

    outfile.open(filename);
    for (int i = 0; i < 1000; i++) {
        outfile << "test file write" << i << endl;
    }

    // 关闭文件
    outfile.close();

    return 0;
}