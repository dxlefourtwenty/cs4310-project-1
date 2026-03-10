from . import parser

def _run_algorithm(processes):
  process_count = len(processes)

  time = 0

  total_wait = 0
  total_turnaround = 0

  for process in processes:
    waiting_time = time

    time = time + process["burst"]

    turnaround_time = waiting_time + process["burst"]
    
    total_wait = total_wait + waiting_time
    total_turnaround = total_turnaround + turnaround_time

  avg_wait = total_wait / process_count
  avg_turnaround = total_turnaround / process_count

  return avg_wait, avg_turnaround

def run(file_path):
  return _run_algorithm(parser.parse_file(file_path))






