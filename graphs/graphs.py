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

def get_all_algorithm_points(algorithms):
  results = {name: [] for name in algorithms}

  for n in range(input_range_min, input_range_max + 1, args.step):
    totals = {name: 0 for name in algorithms}
    
    for _ in range(test_runs):
      # generate ONE dataset
      _generate_length(n, n)
      file_path = f"{graph_batches_root}/batch_{n}.txt"

      # run all algorithms on the SAME dataset
      for name, (algo, kwargs) in algorithms.items():
        _, avg_turnaround = algo.run(file_path, **kwargs)
        totals[name] += avg_turnaround

    # avg results
    for name in algorithms:
      results[name].append(totals[name] / test_runs)

  x_values = list(range(input_range_min, input_range_max + 1, args.step))
  return x_values, results

algorithms = {
  "FCFS": (fcfs, {}),
  "SJF": (sjf, {}),
  "RR (TS=2)": (rr, {"slice": 2}),
  "RR (TS=5)": (rr, {"slice": 5})
}

fig1, axs = plt.subplots(2, 2)
fig1.suptitle("Scheduling Algorithms Comparison")

points_x, results = get_all_algorithm_points(algorithms)
axs[0, 0].plot(points_x, results["FCFS"], marker='o')
axs[0, 0].set_title("FCFS")
axs[0, 0].set_xlabel("Input Size")
axs[0, 0].set_ylabel("Average Turnaround Time for Input Size")

axs[0, 1].plot(points_x, results["SJF"], marker='o')
axs[0, 1].set_title("SJF")
axs[0, 1].set_xlabel("Input Size")
axs[0, 1].set_ylabel("Average Turnaround Time for Input Size")

axs[1, 0].plot(points_x, results["RR (TS=2)"], marker='o')
axs[1, 0].set_title("RR, Time Slice 2")
axs[1, 0].set_xlabel("Input Size")
axs[1, 0].set_ylabel("Average Turnaround Time for Input Size")

axs[1, 1].plot(points_x, results["RR (TS=5)"], marker='o')
axs[1, 1].set_title("RR, Time Slice 5")
axs[1, 1].set_xlabel("Input Size")
axs[1, 1].set_ylabel("Average Turnaround Time for Input Size")

fig2, ax = plt.subplots()
fig2.suptitle("All Algorithms Comparison")

ax.plot(points_x, results["FCFS"], label="FCFS", marker='o')
ax.plot(points_x, results["SJF"], label="SJF", marker='o')
ax.plot(points_x, results["RR (TS=2)"], label="RR (TS=2)", marker='o')
ax.plot(points_x, results["RR (TS=5)"], label="RR (TS=5)", marker='o')

ax.set_xlabel("Input Size")
ax.set_ylabel("Average Turnaround Time")
ax.legend()

plt.show()
