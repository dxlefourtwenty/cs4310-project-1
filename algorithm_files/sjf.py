from . import parser

def _run_algorithm(processes):
  processes.sort(key=lambda p: p["burst"])

  process_count = len(processes)

  time = 0

  total_wait = 0
  total_turnaround_time = 0

  for process in processes:
    waiting_time = time

    time = time + process["burst"]

    turnaround_time = waiting_time + process["burst"]

    total_wait = total_wait + waiting_time
    total_turnaround_time = total_turnaround_time + turnaround_time

  avg_wait = total_wait / process_count
  avg_turnaround = total_turnaround_time / process_count

  return avg_wait, avg_turnaround

# returns avg_wait, then avg_turnaround
# in that order
# make sure parser.py is imported in the same dir as this
def run(file_path):
  return _run_algorithm(parser.parse_file(file_path))







