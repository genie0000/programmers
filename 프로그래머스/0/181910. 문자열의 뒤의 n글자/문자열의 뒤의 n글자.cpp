#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
    string answer = "";
    int len = my_string.length();
    for (int i = len - n; i < len; i++)
        answer += my_string[i];
    return answer;
}

