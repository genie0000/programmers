#include <iostream>
using namespace std;

int solution(int n)
{
    int ans = 0;
    while ( n > 0)
    {
        if (n % 2 == 1)
        {
            ans += 1;
            n -= 1;
        }
        else if (n % 2 == 0)
        {
            n = n/2;
        }
    }

    
    cout << ans << endl;

    return ans;
}