#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int a = 0;
    int b = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (toupper(s[i]) == 'P')
        {
            a += 1;
        }
        else if (toupper(s[i]) == 'Y')
        {
            b += 1;
        }
    }
    if (a == b)
    {
        answer = true;
    }
    else
    {
        answer = false;
    }
    return answer;
}