from transformers import TapexTokenizer, BartForConditionalGeneration
import pandas as pd
from assistant_spacy import speak
tokenizer = TapexTokenizer.from_pretrained("microsoft/tapex-large-finetuned-wtq")
model = BartForConditionalGeneration.from_pretrained("microsoft/tapex-large-finetuned-wtq")

data = {
    "owner": ["ardan", "lyra"],
    "city": ["mamasa", "makassar"],
    "favorite food" : ["nasi goreng", "babi"],
    "favorite anime" : ["gintama", "naruto"]
}
table = pd.DataFrame.from_dict(data)

# tapex accepts uncased input since it is pre-trained on the uncased corpus
query = "do you know what what is ardan's favorite anime?"
encoding = tokenizer(table=table, query=query, return_tensors="pt")

outputs = model.generate(**encoding)


print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

speak(query)
speak(tokenizer.batch_decode(outputs, skip_special_tokens=True))

