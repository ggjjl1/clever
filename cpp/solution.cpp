#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

/**
 * poj 1061 青蛙的约会
 */

// 最大公约数
int gcd(int a, int b)
{
    if (a % b == 0)
        return b;
    return gcd(b, a % b);
}

// 最小公倍数
int lcm(int a, int b)
{
    if (a % b == 0)
        return a;
    return lcm(b, a % b) / (a % b) * a;
}

int main()
{
    // // 1, 2, 3, 4, 5
    // long long x, y, m, n, L;
    // cin >> x >> y >> m >> n >> L;
    // // cout << "x = " << x << ", y = " << y << ", m = " << m << ", n = " << n << ", L = " << L << endl;
    // long long S; // speed
    // long long D; // distance
    // if (m > n)
    // {
    //     S = m - n;
    //     D = y - x;
    // }
    // else
    // {
    //     S = n - m;
    //     D = x - y;
    // }
    // set<int> s;
    // long long i = 0;
    // // i * S - D = j * L
    // while (true)
    // {
    //     if (D + i * L < 0)
    //     {
    //         i = i + 1;
    //         continue;
    //     }
    //     int r = (D + i * L) % S;
    //     int q = (D + i * L) / S;
    //     if (r == 0)
    //     {
    //         cout << q << endl;
    //         break;
    //     }
    //     if (s.count(r))
    //     {
    //         cout << "Impossible" << endl;
    //         break;
    //     }
    //     s.insert(r);
    //     i = i + 1;
    // }

    cout << lcm(10, 3) << endl;
    return 0;
}