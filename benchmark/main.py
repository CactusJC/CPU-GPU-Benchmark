import cpu_benchmark
import gpu_benchmark
import platform
import cpuinfo

def main():
  """
  Runs the CPU and GPU benchmarks and displays the results.
  """
  print("Starting benchmark...")
  print("-" * 30)

  # System Information
  print("System Information:")
  print(f"  OS: {platform.system()} {platform.release()}")
  print(f"  CPU: {cpuinfo.get_cpu_info()['brand_raw']}")
  print("-" * 30)

  # CPU Benchmark
  print("Running CPU benchmark...")
  avg_cpu_time = cpu_benchmark.run_cpu_benchmark()
  print(f"  Average CPU time: {avg_cpu_time} seconds")
  print("-" * 30)

  # GPU Benchmark
  print("Running GPU benchmark...")
  gpu_time = gpu_benchmark.run_gpu_benchmark()
  if isinstance(gpu_time, str):
    print(f"  {gpu_time}")
  else:
    print(f"  GPU time: {gpu_time} seconds")
  print("-" * 30)

  print("Benchmark finished.")

if __name__ == '__main__':
  main()
