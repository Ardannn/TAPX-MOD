import pandas as pd
import numpy as np
def get_data():
    data = {
        "your" : ["Ardan's bot","a"],
        "owner": ["ardan", "lyra"],
        "city": ["mamasa", "makassar"],
        "favorite food": ["nasi goreng", "babi"],
        "favorite anime": ["gintama", "naruto"],
        "name": ["Ardan's bot",""],
        "hometown": ["mamasa",""],
        "good morning" : ["hello good morning",""],
        "hello" : ["Hello, how are you?",""],
        "favorite color" : ['blue',"your mom"]
    }
    df = pd.DataFrame.from_dict(data)

   # Randomly select a row with a non-empty "favorite anime" value
    df = df[df['favorite anime'].notnull()]  # Filter out rows with empty "favorite anime"
    random_index = np.random.randint(0, len(df))  # Generate a random index within the filtered DataFram
    random_row = df.iloc[random_index]  # Select the row at the random index
    return pd.DataFrame.from_dict(random_row)