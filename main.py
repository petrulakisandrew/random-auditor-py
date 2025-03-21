import os
import pandas as pd 
import subprocess


# REPORT_DIRECTORY = 'C:/Users/Andrew Petrulakis/Desktop/Reports/SEMAP/SEMAP 1/DHA/2025/Raw Data/July 24.xlsx'
# OUTPUT_DIRECTORY = 'C:/Users/Andrew Petrulakis/Desktop/Reports/SEMAP/SEMAP 1/DHA/2025/Sampled Data/'

# Run the GUI script first to collect the inputs
subprocess.run(["python", "C:/Users/Andrew Petrulakis/Development/random-auditor-py/Input_GUI.py"], check=True)

# After the GUI finishes, read the input values from the text file
input_file = os.path.join(os.path.dirname(__file__), "input_values.txt")  

try:
    with open(input_file, "r") as f:
        lines = f.readlines()
        print(f"Debug: File contents: {lines}")  # Show what’s read in console
        if len(lines) < 4:
            raise ValueError(f"Input file has {len(lines)} lines, expected 4.") #There should be 5 exact lines for input
        
        REPORT_DIRECTORY = lines[0].strip()
        sample_size = int(lines[1].strip())# This must be a number
        sample_data = lines[2].strip()
        OUTPUT_DIRECTORY = lines[3].strip()
        print(f"Debug: Parsed inputs: {REPORT_DIRECTORY}, {sample_size}, {sample_data}, {OUTPUT_DIRECTORY}") 

except FileNotFoundError:
    print(f"Error: The file {input_file} was not found.")
except ValueError as ve:
    print(f"Value error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    


def random_audit(dataframe: str, sample_size: int, sampled_data: str) -> str:
    """ Generate a random sample based on excel column criteria.
        - data: active excel dataframe being used for the sample
        - sample_size: number of excel rows to be sampled.
        - sampled_data: name of newly created dataframe (for saving)
    """

    try:
    
    #Check to make sure sample size is not greater than the population in the excel spreadhseet
        if sample_size > len(dataframe):
            raise ValueError(
                f"Sample size ({sample_size}) cannot be greater than the ppulation size ({len(dataframe)})."
            )
        
        sampled_df = dataframe.sample(n=sample_size)
        
        print(sampled_df)
        
        full_file_path = os.path.join(OUTPUT_DIRECTORY, f"{sampled_data}.xlsx")
        sampled_df.to_excel(full_file_path, index = False)
        print(f"DataFrame saved to {full_file_path}")
        
    except FileNotFoundError:
        return "Error: The specified Excel file could not be found. Please check the file path."
    
    except ValueError as e:
        return f"Error: {e}"
    
    except Exception as e:
        return f"An unexpected error occurred: {e}"
        
df = pd.read_excel(REPORT_DIRECTORY)
df.fillna('N/A', inplace=True)

random_audit(df,sample_size,sample_data)
