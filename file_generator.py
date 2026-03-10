import random

small_batch = "job_files/small_batch.txt"
medium_batch = "job_files/medium_batch.txt"
large_batch = "job_files/large_batch.txt"

small_batch_size = 10
medium_batch_size = 20
large_batch_size = 30

def generate():
  generate_small()
  generate_medium()
  generate_large()

  print("done.")

def generate_small():
  print("writing small_batch.txt...")

  with open(small_batch, "w") as f:
    for i in range(1, small_batch_size + 1):
      f.write(f"Job{i}\n")
      f.write(f"{random.randint(1, 20)}\n")

def generate_medium():
  print("writing medium_batch.txt...")

  with open(medium_batch, "w") as f:
    for i in range(1, medium_batch_size + 1):
      f.write(f"Job{i}\n")
      f.write(f"{random.randint(1, 20)}\n")

def generate_large():
  print("writing large_batch.txt...")

  with open(large_batch, "w") as f:
    for i in range(1, large_batch_size + 1):
      f.write(f"Job{i}\n")
      f.write(f"{random.randint(1, 20)}\n")


