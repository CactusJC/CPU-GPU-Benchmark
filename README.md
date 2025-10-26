# Simple CPU and GPU Benchmark Tool

This is a simple benchmark tool to measure the performance of your CPU and GPU.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can run the benchmark from the command line:

```bash
python -m benchmark.main
```

## Output

The benchmark will output the following information:

- **System Information:** The OS and CPU model.
- **CPU Benchmark:** The number of detected cores and the average time to complete the benchmark.
- **GPU Benchmark:** The time to complete the GPU benchmark. If a CUDA-enabled GPU is not available, it will report that.
- **Comparison Report:** A comparison of your system's performance against a database of other systems.

The benchmark score is a relative value calculated from the execution time. A higher score indicates better performance.
