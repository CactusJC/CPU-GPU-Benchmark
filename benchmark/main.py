import argparse
import json
import platform
import cpuinfo
from benchmark import cpu_benchmark, gpu_benchmark
from benchmark.reporting import generate_report, calculate_score
from benchmark.database import CPU_BENCHMARKS, GPU_BENCHMARKS

def main():
    """
    Runs the CPU and GPU benchmarks and displays the results.
    """
    parser = argparse.ArgumentParser(description="Simple CPU and GPU Benchmark Tool")
    parser.add_argument("--device", type=str, choices=["cpu", "gpu", "all"], default="all", help="Select the device to benchmark.")
    parser.add_argument("--runs", type=int, default=1, help="Number of times to run the benchmark.")
    parser.add_argument("--warmup-runs", type=int, default=0, help="Number of warm-up runs before the benchmark.")
    parser.add_argument("--output", type=str, help="Path to save the benchmark results in JSON format.")
    args = parser.parse_args()

    results = {
        "system_info": {
            "os": f"{platform.system()} {platform.release()}",
            "cpu": cpuinfo.get_cpu_info()['brand_raw'],
        },
        "benchmarks": []
    }

    print("Starting benchmark...")
    print("-" * 30)
    print("System Information:")
    print(f"  OS: {results['system_info']['os']}")
    print(f"  CPU: {results['system_info']['cpu']}")
    print("-" * 30)

    # Warm-up runs
    if args.warmup_runs > 0:
        print(f"Performing {args.warmup_runs} warm-up runs...")
        for _ in range(args.warmup_runs):
            if args.device in ["cpu", "all"]:
                cpu_benchmark.run_cpu_benchmark()
            if args.device in ["gpu", "all"]:
                gpu_benchmark.run_gpu_benchmark()
        print("Warm-up complete.")
        print("-" * 30)

    for i in range(args.runs):
        print(f"Run {i+1}/{args.runs}")
        run_results = {}

        if args.device in ["cpu", "all"]:
            print("Running CPU benchmark...")
            cores, avg_cpu_time = cpu_benchmark.run_cpu_benchmark()
            cpu_score = calculate_score(avg_cpu_time)
            run_results["cpu"] = {
                "cores": cores,
                "time": avg_cpu_time,
                "score": cpu_score
            }
            print(f"  Cores detected: {cores}")
            print(f"  Average CPU time: {avg_cpu_time} seconds")
            generate_report(cpu_score, CPU_BENCHMARKS.copy())
            print("-" * 30)

        if args.device in ["gpu", "all"]:
            print("Running GPU benchmark...")
            gpu_time = gpu_benchmark.run_gpu_benchmark()
            if isinstance(gpu_time, str):
                print(f"  {gpu_time}")
                run_results["gpu"] = {"error": gpu_time}
            else:
                gpu_score = calculate_score(gpu_time)
                run_results["gpu"] = {
                    "time": gpu_time,
                    "score": gpu_score
                }
                print(f"  GPU time: {gpu_time} seconds")
                generate_report(gpu_score, GPU_BENCHMARKS.copy())
            print("-" * 30)

        results["benchmarks"].append(run_results)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=4)
        print(f"Results saved to {args.output}")

    print("Benchmark finished.")

if __name__ == '__main__':
    main()
