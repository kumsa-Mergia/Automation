import json
import pandas as pd
import os

# Load VM data from a JSON file
def load_vms_from_file(filename="./output-CSV-JSON.json"):
    with open(filename, "r") as file:
        return json.load(file)

vms = load_vms_from_file()

# Filtering: Get VMs with Memory usage above a threshold
def filter_high_memory(vms, threshold=32.0):  # Adjust the threshold as needed
    filtered_vms = []
    for vm in vms:
        try:
            # Ensure the key exists and the value is a valid number
            memory_usage_str = vm.get("Memory\nUsage", "").strip('%')
            if memory_usage_str:
                memory_usage = float(memory_usage_str)
                print(f"VM: {vm['VM Name']}, Memory Usage: {memory_usage}%")  # Print memory usage to debug
                if memory_usage > threshold:
                    filtered_vms.append(vm)
        except (ValueError, KeyError, AttributeError) as e:
            print(f"Skipping VM due to invalid data: {vm} (Error: {e})")
    return filtered_vms

# Save filtered VMs to an Excel file
def save_to_excel(vms, filename="filtered_vms_memory.xlsx"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(vms)
    df.to_excel(filename, index=False)

# Example Usage
filtered_vms = filter_high_memory(vms)
save_to_excel(filtered_vms, filename="./Output/filtered_vms_memory.xlsx")

# Print results
print("Filtered VMs (High Memory Usage) saved to Excel.")
