#include <iostream>
#include <vector>
#include <string>

using namespace std;

int add(int a, int b) {
    return a + b;
}

int main()
{
    vector<string> msg {"Java", "C++", "Python", "Go", "JavaScript", "PHP"};

    for(const string& word : msg) {
        cout << word << endl;
    }
    
    return 0;
}
