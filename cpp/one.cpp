#include <stdio.h>

#ifndef ARRAY_SIZE
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))
#endif

using namespace std;

int main(int argc, char *argv[])
{
    char *message = "Hello World!";
    printf("%s\n", message);
    while (*message != '\0')
    {
        printf("%c ", *message++);
    }
    printf("\n");
    return 0;
}
