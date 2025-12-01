#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    string sa = to_string(a);
    string sb = to_string(b);
    int SA = stoi(sa+sb);
    int SB = stoi(sb+sa);
    if (SA >= SB)
        answer = SA;
    else
        answer = SB;
    
    return answer;
}