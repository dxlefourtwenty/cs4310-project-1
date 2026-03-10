def parse_file(file_path):

  processes = []

  try:
    with open(file_path, 'r') as file:
      lines = [line.strip() for line in file]

    for i in range(0, len(lines), 2):
      job = lines [i]
      value = int(lines[i + 1])

      processes.append({
        "job": job,
        "burst": int(value)
      })

  except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

  return processes
