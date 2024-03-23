import pandas as pd
import numpy as np

# Link to edit the Google Sheet: https://docs.google.com/spreadsheets/d/1-zDC2v1XT9u9Q9L0e8pESvhuHruwgO7_KGY30vpROkE/edit?usp=sharing
# After you make edits you must downloaded it and replace the existing file in the assets/data folder.

# --- Load your spreadsheets ---
def load_data():
    price_matrix_df = pd.read_excel("assets/data/Text-Adventure.xlsx", sheet_name="Price Matrix", header=0, index_col=0)  
    base_prices_df = pd.read_excel("assets/data/Text-Adventure.xlsx", sheet_name="Base Prices", header=0, index_col=0) 
    events_df = pd.read_excel("assets/data/Text-Adventure.xlsx", sheet_name="Events", header=0, index_col=0)  

    return price_matrix_df, base_prices_df, events_df


# --- Core Calculation Function ---
def calculate_prices(price_matrix_df, base_prices_df, events_df, event_name, non_linear_function=None):
    base_prices = base_prices_df["Base Price"]    
    event_vector = events_df.loc[event_name]  

    # Linear impact calculation
    impact = price_matrix_df.dot(event_vector)  

    # Apply optional non-linear function (if provided)
    if non_linear_function:
        impact = non_linear_function(impact)

    new_prices = base_prices * (1+ impact)
    return new_prices


# --- Example Usage ---
if __name__ == "__main__":
    price_matrix, base_prices, events = load_data()

    # Example non-linear function (Diminishing returns)
    def log_effect(x):
        return np.log1p(x)

    new_prices = calculate_prices(price_matrix, base_prices, events, "Dragon Emergence", non_linear_function=log_effect) 
    print(new_prices) 
