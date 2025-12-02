#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    string s = to_string(x);
    vector<int>value(s.size());
    int sum = 0;
    for (int i = 0; i < s.size(); i++){
        sum += s[i]-'0';
    }
    if (x % sum == 0){}
    else {answer = false;}
    return answer;
}