import pandas as pd
import matplotlib.pyplot as plt
import json

def parse_json_file_for_fibonacci_verification(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    
    parsed_data = []
    for category in data["results"]:
        if category["name"] == "Fibonacci_Verification":  # Focus only on Fibonacci Verification data
            for result in category["results"]:
                parsed_data.append({
                    "Fibonacci Number": result["name"],
                    "Memory Usage (bytes)": result["metrics"].get("memory_usage_bytes", 0),
                    "Time (seconds)": result["time"]["secs"] + result["time"]["nanos"] / 1e9,
                })
    return parsed_data

def plot_fibonacci_verification_metrics(df, save_path):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_title('Fibonacci Verification Performance Metrics')
    ax1.set_xlabel('Fibonacci Number')
    ax1.set_ylabel('Memory Usage (bytes)', color='tab:red')
    ax1.plot(df["Fibonacci Number"], df["Memory Usage (bytes)"], color='tab:red', marker='o', linestyle='None', label='Memory Usage')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Time (seconds)', color='tab:blue')  # we already handled the x-label with ax1
    ax2.plot(df["Fibonacci Number"], df["Time (seconds)"], color='tab:blue', marker='x', linestyle='None', label='Time')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.savefig(save_path, format='png', dpi=300)

# Specify the file path to your JSON data for Fibonacci Verification
file_path_verification = "../benchmarks/risczero/fibonacci/bench.json"

# Read and parse the JSON data from the file
df_fibonacci_verification = pd.DataFrame(parse_json_file_for_fibonacci_verification(file_path_verification))

save_path_fibonacci_verification = "../benchmarks/graphs/risczero_fibonacci_verification_metrics.png"

# Generate and save the plots for Fibonacci Verification data
plot_fibonacci_verification_metrics(df_fibonacci_verification, save_path_fibonacci_verification)

# Note: Make sure to update "path_to_your_fibonacci_verification_json_file.json" with the actual path to your JSON file before running the script.

