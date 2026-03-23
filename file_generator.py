import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--generate", action="store_true")
args = parser.parse_args()

small_batch = "job_files/small_batch.txt"
medium_batch = "job_files/medium_batch.txt"
large_batch = "job_files/large_batch.txt"

small_batch_size = 5
medium_batch_size = 10
large_batch_size = 15

burst_range_min = 1
burst_range_max = 20

def generate(verbose=False):
  if args.verbose or verbose:
    print("writing small_batch.txt...")
  generate_small()

  if args.verbose or verbose:
    print("writing medium_batch.txt...")
  generate_medium()

  if args.verbose or verbose:
    print("writing large_batch.txt...")
  generate_large()

def generate_small():
  with open(small_batch, "w") as f:
    for i in range(1, small_batch_size + 1):
      f.write(f"Job{i}\n")
      f.write(f"{random.randint(burst_range_min, burst_range_max)}\n")

def generate_medium():
  with open(medium_batch, "w") as f:
    for i in range(1, medium_batch_size + 1):
      f.write(f"Job{i}\n")
      f.write(f"{random.randint(burst_range_min, burst_range_max)}\n")

def generate_large():
  with open(large_batch, "w") as f:
    for i in range(1, large_batch_size + 1):
      f.write(f"Job{i}\n")
      f.write(f"{random.randint(burst_range_min, burst_range_max)}\n")

if args.generate:
  generate()

