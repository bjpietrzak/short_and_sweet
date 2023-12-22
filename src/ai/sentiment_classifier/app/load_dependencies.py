from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import json


tokenizer = DistilBertTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english")
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english")

config = json.load(open('config.json'))