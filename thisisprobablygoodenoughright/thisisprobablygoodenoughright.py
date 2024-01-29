class Solution:
    def countTime(self, time: str) -> int:
        answer = 1
        if time[4] == '?':
            answer = 10
        if time[3] == '?':
            answer = answer * 6
        if time[1] == '?' and time[0] == '?':
            answer = answer * 24
        elif time[1] == '?' and time[0] != '?':
            if time[0] == '2':
                answer = answer * 4
            else:
                answer = answer * 10
        elif time[1] != '?' and time[0] == '?':
            if int(time[1]) > 3:
                answer = answer * 2
            else:
                answer = answer * 3
        return answer
