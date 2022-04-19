#include <iostream>
#include <vector>
#include <string>

using namespace std;

int add(int a, int b) {
    return;
}

int main()
{
    vector<string> msg {"Java", "C++", "Python", "Go", "JavaScript", "PHP"};

    for(const string& word : msg) {
        cout << word << " ";
    }
    cout << "\n";
}
