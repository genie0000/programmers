#include <iostream>
#include<string>
#include<stack>
using namespace std;

int solution(string s)
{
    int answer = -1;
    stack<char> a;
    for (char c: s)
    {
        if(!a.empty() && a.top() == c)
        {
            a.pop();
        }
        else
        {
            a.push(c);
        }
    }
    answer = a.empty()? 1: 0;
    return answer;
}