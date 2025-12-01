#include <string>
#include <vector>

using namespace std;
int solution(int a, int b) {
    int answer = 0;
    string s = to_string(a) + to_string(b);
    int num = stoi(s);
    if (2* a*b <= num)
        answer = num;
    else
        answer = 2*a * b;
    return answer;
}
