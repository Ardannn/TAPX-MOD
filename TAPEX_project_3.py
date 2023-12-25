# main_script.py

from transformers import TapexTokenizer, BartForConditionalGeneration
from assistant_spacy import speak
from kayaknya_data import get_data
import pandas as pd

def main():
    tokenizer = TapexTokenizer.from_pretrained("microsoft/tapex-large-finetuned-wtq")
    model = BartForConditionalGeneration.from_pretrained("microsoft/tapex-large-finetuned-wtq")

    table = get_data()

    query = input("Prompt: ")
    encoding = tokenizer(table=table, query=query, return_tensors="pt")

    outputs = model.generate(**encoding)

    print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

    speak(tokenizer.batch_decode(outputs, skip_special_tokens=True))

if __name__ == "__main__":
    main()
