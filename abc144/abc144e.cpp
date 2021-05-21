#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int i;
    char str[10], *a[10], *b[10], *c[10];
    while (cin >> str)
    {
        a[i] = strtok(str, ","); //","で分解
        b[i] = strtok(NULL, ",");
        c[i] = strtok(NULL, ",");
        cout << a[i] << b[i] << c[i] << "\n";
        i++;
    }
    return 0;
}