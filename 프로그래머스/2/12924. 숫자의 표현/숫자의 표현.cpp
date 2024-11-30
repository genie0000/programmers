#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    for (int i = 1; i <= n; i++)
    {
        int sum = 0; 
        for (int a = i; a <= n; a++)        
        {
            sum += a;
            if (sum == n)
            {
                answer += 1;
                break;
            }                
            else if (sum > n)
            {
                break;
            }
        }
    }
    return answer;
}