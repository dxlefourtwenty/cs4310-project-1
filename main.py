from algorithm_files import fcfs, sjf, rr
import file_generator

test_runs = 20

small = "job_files/small_batch.txt"
medium = "job_files/medium_batch.txt"
large = "job_files/large_batch.txt"

# for each test, omit avg_wait
# (algorithms were written with avg_wait)
def test_fcfs():
  _, small_avg_turnaround = fcfs.run(small)
  _, medium_avg_turnaround = fcfs.run(medium)
  _, large_avg_turnaround = fcfs.run(large)

  print("\n---First Come, First Serve---")
  print(f">>Small batch \
        \nAverage Turnaround Time: {small_avg_turnaround:.2f}")
  print(f"\n>>Medium batch \
        \nAverage Turnaround Time: {medium_avg_turnaround:.2f}")
  print(f"\n>>Large batch \
        \nAverage Turnaround Time: {large_avg_turnaround:.2f}")

def test_sjf():
  _, small_avg_turnaround = sjf.run(small)
  _, medium_avg_turnaround = sjf.run(medium)
  _, large_avg_turnaround = sjf.run(large)

  print("\n---Shortest Job First---")
  print(f">>Small batch \
        \nAverage Turnaround Time: {small_avg_turnaround:.2f}")
  print(f"\n>>Medium batch \
        \nAverage Turnaround Time: {medium_avg_turnaround:.2f}")
  print(f"\n>>Large batch \
        \nAverage Turnaround Time: {large_avg_turnaround:.2f}")

def test_rr(time_slice):
  _, small_avg_turnaround = rr.run(small, time_slice)
  _, medium_avg_turnaround = rr.run(medium, time_slice)
  _, large_avg_turnaround = rr.run(large, time_slice)

  print(f"\n---Round Robin Slice = {time_slice}---")
  print(f">>Small batch \
        \nAverage Turnaround Time: {small_avg_turnaround:.2f}")
  print(f"\n>>Medium batch \
        \nAverage Turnaround Time: {medium_avg_turnaround:.2f}")
  print(f"\n>>Large batch \
        \nAverage Turnaround Time: {large_avg_turnaround:.2f}")

def print_batch_results(algorithm_name, small_total, medium_total, large_total):
  small_avg = small_total / test_runs 
  medium_avg = medium_total / test_runs
  large_avg = large_total / test_runs

  print(f"\n---{algorithm_name}---")
  print(">>Small batch")
  print(f"Average Turnaround Time For {test_runs} runs: {small_avg:.2f}")
  print(">>Medium batch")
  print(f"Average Turnaround Time For {test_runs} runs: {medium_avg:.2f}")
  print(">>Large batch")
  print(f"Average Turnaround Time For {test_runs} runs: {large_avg:.2f}")

def batch_test():
  fcfs_name = "First Come, First Serve"
  sjf_name = "Shortest Job First"
  rr_two_name = "Round Robin, Time Slice 2"
  rr_five_name = "Round Robin, Time Slice 5"

  small_fcfs_total = 0
  medium_fcfs_total = 0
  large_fcfs_total = 0

  small_sjf_total = 0
  medium_sjf_total = 0
  large_sjf_total = 0

  small_rr_two_total = 0
  medium_rr_two_total = 0
  large_rr_two_total = 0

  small_rr_five_total = 0
  medium_rr_five_total = 0
  large_rr_five_total = 0

  for i in range(test_runs):
    file_generator.generate()
    _, small_fcfs_avg = fcfs.run(small)
    _, medium_fcfs_avg = fcfs.run(medium)
    _, large_fcfs_avg = fcfs.run(large)

    small_fcfs_total += small_fcfs_avg
    medium_fcfs_total += medium_fcfs_avg
    large_fcfs_total += large_fcfs_avg

    _, small_sjf_avg = sjf.run(small)
    _, medium_sjf_avg = sjf.run(medium)
    _, large_sjf_avg = sjf.run(large)

    small_sjf_total += small_sjf_avg
    medium_sjf_total += medium_sjf_avg
    large_sjf_total += large_sjf_avg

    _, small_rr_two_avg = rr.run(small, 2)
    _, medium_rr_two_avg = rr.run(medium, 2)
    _, large_rr_two_avg = rr.run(large, 2)

    small_rr_two_total += small_rr_two_avg
    medium_rr_two_total += medium_rr_two_avg
    large_rr_two_total += large_rr_two_avg

    _, small_rr_five_avg = rr.run(small, 5)
    _, medium_rr_five_avg = rr.run(medium, 5)
    _, large_rr_five_avg = rr.run(large, 5)

    small_rr_five_total += small_rr_five_avg
    medium_rr_five_total += medium_rr_five_avg
    large_rr_five_total += large_rr_five_avg

  print_batch_results(fcfs_name, small_fcfs_total, medium_fcfs_total, large_fcfs_total)
  print_batch_results(sjf_name, small_sjf_total, medium_sjf_total, large_sjf_total)
  print_batch_results(rr_two_name, small_rr_two_total, medium_rr_two_total, large_rr_two_total)
  print_batch_results(rr_five_name, small_rr_five_total, medium_rr_five_total, large_rr_five_total)

# To run each test, just uncomment the section needed to run
# When doing python main.py
# NOTE:
# When running the correctness test,
# generate a batch with
# python file_generator.py
def main():
  print("[Correctness Test]")
  test_fcfs()
  test_sjf()
  test_rr(2)
  test_rr(5)

  # print("[Batch Test]")
  # batch_test()

main()


