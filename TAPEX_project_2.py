# main_script.py

from transformers import TapexTokenizer, BartForConditionalGeneration
from assistant_spacy import speak
from kayaknya_data import get_data
import pandas as pd

tokenizer = TapexTokenizer.from_pretrained("microsoft/tapex-large-finetuned-wtq")
model = BartForConditionalGeneration.from_pretrained("microsoft/tapex-large-finetuned-wtq")

table = get_data()

query = "what is your opnion about christmas"
encoding = tokenizer(table=table, query=query, return_tensors="pt")

outputs = model.generate(**encoding)

print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

speak(query)
speak(tokenizer.batch_decode(outputs, skip_special_tokens=True))
