#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    for (int i = 0; i <= discount.size() - 10; i++) 
    {
        vector<int> count(want.size(), 0);
        
        for (int j = 0; j < 10; j++) 
        {
            for (int k = 0; k < want.size(); k++) 
            {
                if (discount[i + j] == want[k]) 
                {
                    count[k]++;
                }
            }
        }
        bool valid = true;
        for (int k = 0; k < want.size(); k++) 
        {
            if (count[k] != number[k]) 
            {
                valid = false;
                break;
            }
        }
        if (valid) 
        {
            answer++;
        }
    }

    return answer;
}
