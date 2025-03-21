import os
import pandas as pd 


REPORT_DIRECTORY = 'C:/Users/Andrew Petrulakis/Desktop/Reports/SEMAP/SEMAP 1/DHA/2025/Raw Data/July 24.xlsx'
OUTPUT_DIRECTORY = 'C:/Users/Andrew Petrulakis/Desktop/Reports/SEMAP/SEMAP 1/DHA/2025/Sampled Data/'

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
        
        full_file_path = os.path.join(OUTPUT_DIRECTORY, sampled_data)
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

random_audit(df,3,"test.xlsx")
