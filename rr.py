import parser
from collections import deque

def _run_algorithm(processes, slice):
  time = 0
  ready_queue = deque()

  total_wait = 0
  total_turnaround_time = 0

  n = len(processes)

  for process in processes:
    process["remaining"] = process["burst"]
    ready_queue.append(process)

  while len(ready_queue) > 0:
    current = ready_queue.popleft()

    current["turnaround"] = 0
    current["waiting"] = 0

    if current["remaining"] > slice:
      time = time + slice 
      current["remaining"] = current["remaining"] - slice

      ready_queue.append(current)

    else:
      time = time + current["remaining"]  
      current["remaining"] = 0

      current["turnaround"] = time 
      current["waiting"] = current["turnaround"] - current["burst"]  

    total_wait = total_wait + current["waiting"]
    total_turnaround_time = total_turnaround_time + current["turnaround"]

  avg_wait = total_wait / n 
  avg_turnaround = total_turnaround_time / n

  return avg_wait, avg_turnaround

# returns avg_wait, then avg_turnaround
# in that order
# make sure parser.py is imported in the same dir as this
def run(file_path, slice):
  return _run_algorithm(parser.parse_file(file_path), slice)






