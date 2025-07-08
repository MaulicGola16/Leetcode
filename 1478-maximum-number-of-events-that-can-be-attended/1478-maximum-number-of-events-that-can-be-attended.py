from heapq import heappush, heappop
from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total = max(event[1] for event in events)
        pq = []
        i = 0
        day, cnt = 1, 0
        while day <= total:
            if not pq and i < len(events):
                day = max(day, events[i][0])
            while pq and pq[0] < day:
                heappop(pq)
            while i < len(events) and events[i][0] == day:
                heappush(pq, events[i][1])
                i += 1
            if pq:
                heappop(pq)
                cnt += 1
            elif i == len(events):
                break
            day += 1
        return cnt