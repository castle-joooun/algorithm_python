# https://school.programmers.co.kr/learn/courses/30/lessons/42627?language=python3
import heapq


def solution(jobs):
    jobs.sort()

    heap = []

    cur_time, completed_jobs, total_time = 0, 0, 0
    jobs_idx = 0

    while completed_jobs < len(jobs):
        while jobs_idx < len(jobs) and jobs[jobs_idx][0] <= cur_time:
            start, duration = jobs[jobs_idx]
            heapq.heappush(heap, (duration, start))
            jobs_idx += 1

        if heap:
            duration, start = heapq.heappop(heap)
            cur_time += duration
            total_time += (cur_time - start)
            completed_jobs += 1
        else:
            cur_time = jobs[jobs_idx][0]

    return total_time // completed_jobs

print(solution([[0, 3], [1, 9], [3, 5]]))

