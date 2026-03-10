from algorithm_files import fcfs, sjf# rr
import file_generator

small = "job_files/small_batch.txt"
medium = "job_files/medium_batch.txt"
large = "job_files/large_batch.txt"

def test_fcfs():
  small_avg_wait, small_avg_turnaround = fcfs.run(small)
  medium_avg_wait, medium_avg_turnaround = fcfs.run(medium)
  large_avg_wait, large_avg_turnaround = fcfs.run(large)

  print("\n---First Come, First Serve---")
  print(f">>Small batch \
        \nAverage Waiting Time: {small_avg_wait:.2f} \
        \nAverage Turnaround Time: {small_avg_turnaround:.2f}")
  print(f"\n>>Medium batch \
        \nAverage Waiting Time: {medium_avg_wait:.2f} \
        \nAverage Turnaround Time: {medium_avg_turnaround:.2f}")
  print(f"\n>>Large batch \
        \nAverage Waiting Time: {large_avg_wait:.2f} \
        \nAverage Turnaround Time: {large_avg_turnaround:.2f}")

def test_sjf():
  small_avg_wait, small_avg_turnaround = sjf.run(small)
  medium_avg_wait, medium_avg_turnaround = sjf.run(medium)
  large_avg_wait, large_avg_turnaround = sjf.run(large)

  print("\n---Shortest Job First---")
  print(f">>Small batch \
        \nAverage Waiting Time: {small_avg_wait:.2f} \
        \nAverage Turnaround Time: {small_avg_turnaround:.2f}")
  print(f"\n>>Medium batch \
        \nAverage Waiting Time: {medium_avg_wait:.2f} \
        \nAverage Turnaround Time: {medium_avg_turnaround:.2f}")
  print(f"\n>>Large batch \
        \nAverage Waiting Time: {large_avg_wait:.2f} \
        \nAverage Turnaround Time: {large_avg_turnaround:.2f}")

def main():
  file_generator.generate()        

  test_fcfs()
  test_sjf()

main()


