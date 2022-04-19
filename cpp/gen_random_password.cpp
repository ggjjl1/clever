#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>

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
	
	string str1 = gen_random();
	cout << str1 << endl;
	return 0;
}