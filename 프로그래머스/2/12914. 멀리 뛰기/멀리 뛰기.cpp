#include <vector>

using namespace std;

long long solution(int n) {
    const int M = 1234567;
    vector<long long> a(n + 1, 0);
    a[1] = 1;
    if (n >= 2) 
    {
        a[2] = 2;
    }
    for (int i = 3; i <= n; i++) 
    {
        a[i] = (a[i - 1] + a[i - 2]) % M;
    }
    return a[n];
}
