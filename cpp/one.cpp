#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

#include "nlohmann/json.hpp"

using namespace std;

using json = nlohmann::json;

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

enum class Color {
    GREEN, BLUE, RED, YELLOW, BLACK
};

int main() {

    // ofstream outfile;
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

    // json j;

    // j["pi"] = 3.1415926;
    // j["happy"] = true;
    // j["name"] = "Niels";
    // j["nothing"] = nullptr;

    // string s = j.dump();

    // cout << s << endl;

    // vector<string> list = {"java", "c++", "go", "python", "rust"};
    // for (int i = 0; i < list.size(); i++) {
    //     cout << list[i] << endl;
    // }

    // set<int> set1;
    // set1.insert(1);
    // set1.insert(2);
    // set1.insert(3);
    // set1.insert(1);

    // set<int>::iterator it;
    // for (it = set1.begin(); it != set1.end(); it++) {
    //     cout << *it << endl;
    // }

    // const int a = 7;
    // int *p = (int*)&a;
    // *p = 8;
    // a = 8;
    // cout << a << endl;

    int i = 10;
    cout << &i << endl;
    cout << *&i << endl;

    system("pause");

    cout << "+====================================+" << endl;
    cout << "|              hard seed             |" << endl;
    cout << "+------------------------------------+" << endl;
    cout << "|                                    |" << endl; 
    cout << "+====================================+" << endl;

    return 0;
}