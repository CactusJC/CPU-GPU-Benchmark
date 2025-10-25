import torch
import time

def run_gpu_benchmark(matrix_size=10000):
  """
  Runs a GPU benchmark using PyTorch.
  """
  if not torch.cuda.is_available():
    return "CUDA not available."

  device = torch.device("cuda")

  # Create two large random matrices on the GPU
  a = torch.randn(matrix_size, matrix_size, device=device)
  b = torch.randn(matrix_size, matrix_size, device=device)

  # Synchronize to ensure accurate timing
  torch.cuda.synchronize()

  # Start the timer and perform matrix multiplication
  start = time.time()
  torch.matmul(a, b)
  torch.cuda.synchronize()
  end = time.time()

  return round(end - start, 3)

if __name__ == '__main__':
  print("Running GPU benchmark...")
  gpu_time = run_gpu_benchmark()
  if isinstance(gpu_time, str):
    print(gpu_time)
  else:
    print(f"GPU time: {gpu_time} seconds")
