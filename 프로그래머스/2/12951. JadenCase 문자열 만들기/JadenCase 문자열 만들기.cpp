#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    bool a = true;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == ' ')
        {
            answer += s[i];
            a = true;
        }
        else if ((a && isalpha(s[i]) || isdigit(s[i])))
        {
            answer += toupper(s[i]);
            a = false;
        }
        else if (isalpha(s[i]))
        {
            answer += tolower(s[i]);
        }
    }

    return answer;
}