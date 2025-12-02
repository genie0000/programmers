using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = 0;
    long long value = 0;
    for (int i = 1; i <= count; i++)
        value += price * i;
    if (money - value >= 0)
        answer = 0;
    else
        answer = value - money;

    return answer;
}