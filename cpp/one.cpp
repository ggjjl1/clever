#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main()
{
    stringstream ss;
    int i = 1;
    ss << i++;
    cout << ss.str().size() << endl;
    return 0;
}