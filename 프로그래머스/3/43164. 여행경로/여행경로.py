def solution(tickets):
    answer = []
    tickets.sort()
    used = [False] * len(tickets)
    
    def dfs(route, depth):
        if depth == len(tickets):
            answer.append(route[:])
            return
        for i in range(len(tickets)):
            if not used[i] and route[-1] == tickets[i][0]:
                used[i] = True
                dfs(route + [tickets[i][1]], depth+ 1)
                used[i] = False
    
    dfs(["ICN"],0)
        
    
    return answer[0]