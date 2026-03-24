import matplotlib
matplotlib.use('QtAgg')

import matplotlib.pyplot as plt
import numpy as np
import random
import argparse

from algorithm_files import fcfs, sjf, rr

parser = argparse.ArgumentParser()
parser.add_argument("--step", type=int, default=1)
args = parser.parse_args()

burst_min = 1
burst_max = 20

input_range_min = 5
input_range_max = 15

test_runs = 20

graph_batches_root = "graph_batches"

def _process_algorithm(algorithm, processes, **kwargs):
  _, avg_turnaround = algorithm.run(processes, **kwargs)

  return avg_turnaround

def _process_algorithm_test_runs(algorithm, processes, **kwargs):
  turnaround_time_total = 0

  for i in range(test_runs):
    avg_turnaround = _process_algorithm(algorithm, processes, **kwargs)
    turnaround_time_total += avg_turnaround

  return turnaround_time_total / test_runs

def _generate_length(num_processes, batch_num):
  with open(f"{graph_batches_root}/batch_{batch_num}.txt", "w") as f:
    for i in range(1, num_processes + 1):
      f.write(f"Job{i}\n")
      f.write(f"{random.randint(burst_min, burst_max)}\n")

def get_algorithm_points(algorithm, **kwargs):
  points_x = []
  points_y = []

  for i in range(input_range_min, input_range_max + 1, args.step):
    y = _process_algorithm_test_runs(algorithm, f"{graph_batches_root}/batch_{i}.txt", **kwargs)

    points_x.append(i)
    points_y.append(y)

  return points_x, points_y

x = np.linspace(0, 10, 100)

# run this initially then comment out for non-changing comparison
# for i in range(input_range_min, input_range_max + 1):
#   _generate_length(i, i)

plt.title("Job Scheduling Algorithms")
plt.xlabel("Input Size")
plt.ylabel("Average Turnaround Time for Input Size")

points_x, points_y = get_algorithm_points(fcfs)
plt.plot(points_x, points_y, label="FCFS",marker='o')

points_x, points_y = get_algorithm_points(sjf)
plt.plot(points_x, points_y, label="SJF", marker='o')

points_x, points_y = get_algorithm_points(rr, slice=2)
plt.plot(points_x, points_y, label="RR, 2", marker='o')

points_x, points_y = get_algorithm_points(rr, slice=5)
plt.plot(points_x, points_y, label="RR, 5", marker='o')

plt.legend()
plt.show()
