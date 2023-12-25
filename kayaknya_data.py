import pandas as pd
import random
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
        "favorite color" : ['blue',"your mom"],
        "opnion about christmas" : ["its really cold, and a lot of people having fun",""],
        "your favorite man": ["my favorite main is ardan", ""]

    }

    return pd.DataFrame.from_dict(data)