import tkinter as tk
from tkinter import filedialog
import os


def save_inputs():
    # Get values from the entry fields
    REPORT_DIRECTORY = entry_file.get()
    sample_size = entry_sample.get()
    sampled_data = entry_sampled_data.get()
    OUTPUT_DIRECTORY = entry_output_dir.get()

    # Try converting sample_size to an integer
    try:
        sample_size = int(sample_size)
    except ValueError:
        print("Sample size must be an integer.")
        return

    # Save the values to a text file in the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input_values.txt")
    
    try:
        with open(file_path, "w") as f:
            f.write(f"{REPORT_DIRECTORY}\n{sample_size}\n{sampled_data}\n{OUTPUT_DIRECTORY}")
        print(f"Successfully saved inputs to: {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
    
    root.quit()  # Close the Tkinter window after saving inputs


def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    entry_file.delete(0, tk.END)
    entry_file.insert(0, filename)
    
def browse_output_directory():
    folder_selected = filedialog.askdirectory()
    entry_output_dir.delete(0, tk.END)
    entry_output_dir.insert(0, folder_selected)

# Tkinter GUI Setup
root = tk.Tk()
root.title("Input Collection")

# File selection
tk.Label(root, text="Select Excel File:").grid(row=0, column=0, padx=5, pady=5)
entry_file = tk.Entry(root, width=50)
entry_file.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=5, pady=5)

# Sample size input
tk.Label(root, text="Sample Size:").grid(row=1, column=0, padx=5, pady=5)
entry_sample = tk.Entry(root, width=10)
entry_sample.grid(row=1, column=1, padx=5, pady=5)

# Output file name input
tk.Label(root, text="Output Excel File Name (without extension):").grid(row=2, column=0, padx=5, pady=5)
entry_sampled_data = tk.Entry(root, width=30)
entry_sampled_data.grid(row=2, column=1, padx=5, pady=5)

# Output directory selection
tk.Label(root, text="Select Output Directory:").grid(row=3, column=0, padx=5, pady=5)
entry_output_dir = tk.Entry(root, width=50)
entry_output_dir.grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_output_directory).grid(row=3, column=2, padx=5, pady=5)

# Save button
tk.Button(root, text="Save Inputs", command=save_inputs).grid(row=4, column=1, padx=5, pady=10)

root.mainloop()