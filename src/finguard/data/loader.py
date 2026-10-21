import pandas as pd
from pathlib import Path

# file_path = Path("data/raw/creditcard.csv")




def load_data(file_path: str) -> pd.DataFrame:
    """
    Load financial transaction data from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame containing transaction records.
    """

    #  Convert file_path into a Path object
    file_path = Path(file_path)

    #  Check whether the file exists
    file_exists = file_path.exists()
    # print(f"File exists: {file_exists}")

    # Raise FileNotFoundError if it doesn't exist
    if not file_exists:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Load CSV using pandas
    data = pd.read_csv(file_path)
    print(f"Data loaded successfully. Shape: {data.shape}")

    
    return data






