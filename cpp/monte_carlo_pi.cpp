#include <iostream>
#include <ctime>
using namespace std;

double monte_carlo_pi(int n)
{
    srand(static_cast<unsigned int>(time(0)));
    int acc = 0;
    for(int i = 0; i < n; i++) 
    {
        double x = static_cast<double>(rand()) / RAND_MAX;
        double y = static_cast<double>(rand()) / RAND_MAX;
        if(x * x + y * y <= 1.0) 
        {
            acc = acc + 1;
        }
    }

    return 4.0 * acc / n;
}

int main()
{
    time_t timep;
    struct tm *p;
    time(&timep);

    int start = timep;

    double pi = monte_carlo_pi(100000000);
    printf("PI is %f\n", pi);

    time(&timep);
    int end = timep;

    printf("运行时间 %d秒\n",(end - start));

    return 0;
}
