import time
from multiprocessing import Process, Manager, cpu_count

def run_single_core_benchmark(thread_id, load, return_dict):
  """
  Runs a single-core CPU benchmark.
  """
  start_benchmark = int(load)
  start = time.time()

  for _ in range(start_benchmark):
    for x in range(1, 1000):
      3.141592 * 2**x
    for x in range(1, 10000):
      float(x) / 3.141592
    for x in range(1, 10000):
      float(3.141592) / x

  end = time.time()
  duration = round(end - start, 3)
  return_dict[thread_id] = (thread_id, duration)

def run_cpu_benchmark(processes=None, load=50000):
  """
  Runs a multi-core CPU benchmark.
  """
  if processes is None:
    processes = cpu_count()

  manager = Manager()
  return_dict = manager.dict()
  jobs = []

  for i in range(processes):
    proc = Process(target=run_single_core_benchmark, args=(i, load / processes, return_dict))
    jobs.append(proc)
    proc.start()

  for proc in jobs:
    proc.join()

  total_time = 0
  for _, duration in return_dict.values():
    total_time += duration

  return round(total_time / processes, 3)

if __name__ == '__main__':
  print("Running CPU benchmark...")
  avg_time = run_cpu_benchmark()
  print(f"Average CPU time: {avg_time} seconds")
