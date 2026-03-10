from . import parser

def _run_algorithm(processes):
  time = 0

  for process in processes:
    print(process["job"], process["burst"])

def run(file_path):
  _run_algorithm(parser.parse_file(file_path))






