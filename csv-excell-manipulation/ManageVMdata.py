import json
import csv

# Load VM data from a JSON file
def load_vms_from_file(filename="vms.json"):
    with open(filename, "r") as file:
        return json.load(file)

vms = load_vms_from_file()

# Filtering: Get VMs with CPU usage above a threshold
def filter_high_cpu(vms, threshold=8.0):
    return [vm for vm in vms if vm["CPU Usage"] > threshold]

# Sorting: Sort VMs by memory usage
def sort_by_memory_usage(vms, descending=True):
    return sorted(vms, key=lambda vm: vm["Memory Usage"], reverse=descending)

# Aggregation: Calculate average CPU and memory usage
def calculate_averages(vms):
    total_cpu = sum(vm["CPU Usage"] for vm in vms)
    total_memory = sum(vm["Memory Usage"] for vm in vms)
    return {
        "Average CPU Usage": total_cpu / len(vms),
        "Average Memory Usage": total_memory / len(vms),
    }

# Exporting: Save VM data to CSV
def save_to_csv(vms, filename="vm_data.csv"):
    keys = vms[0].keys()
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(vms)

# Example Usage
filtered_vms = filter_high_cpu(vms)
sorted_vms = sort_by_memory_usage(vms)
averages = calculate_averages(vms)
save_to_csv(vms)

# Print results
print("Filtered VMs (High CPU):", filtered_vms)
print("Sorted VMs (By Memory Usage):", sorted_vms)
print("Averages:", averages)
