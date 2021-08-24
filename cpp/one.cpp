#include <iostream>
#include <fstream>
#include <string.h>
#include <vector>
#include <sstream>

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

    // string filename;

    // cout << "请输入文件路径：";
    // cin >> filename;
    // cout << "输入的文件路径名为：" << filename << endl;

    // outfile.open(filename);
    // for (int i = 0; i < 1000; i++) {
    //     outfile << "test file write" << i << endl;
    // }

    // 关闭文件
    // outfile.close();

    // int array[5] = {1, 2, 3, 4, 5};
    // vector<int> list(array, array + 5);
    // for (int i = 0; i < list.size(); i++) {
    //     cout << list[i] << endl;
    // }

    double pi = 3.1415926;
    float dollar = 1.00;
    int dozen = 12;
    int number = 35;

    stringstream ss;

    ss << "dozen: " << dozen << endl;

    // 显示小数
    ss.setf(ios::fixed);

    // 显示2位小数
    ss.precision(2);
    ss << "dollar: " << dollar << endl;

    // 显示10位小数
    ss.precision(10);
    ss << "pi: " << pi << endl;

    // 以十六进制显示整数
    ss.unsetf(ios_base::dec);
    ss.setf(ios::hex);
    ss << "number: " << number << endl;

    string text = ss.str();
    cout << text << endl;

    return 0;
}