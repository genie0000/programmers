#include <string>
#include <vector>

using namespace std;

int solution(int n, int k) {
    int answer = 0;
    if (n >= 10)
    {
        answer = n * 12000 + k * 2000 - 2000* (n/10);
    }
    else
    {
        answer = n * 12000 + k * 2000;
    }
    return answer;
}