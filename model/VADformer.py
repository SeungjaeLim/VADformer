import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from transformers import BertModel, BertTokenizer

# Define the model architecture
class BertForSentimentAnalysis(nn.Module):
    def __init__(self, n_classes):
        super(BertForSentimentAnalysis, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.dropout = nn.Dropout(0.2)
        self.fc1 = nn.Linear(768, 256)
        self.fc2 = nn.Linear(256, n_classes)

    def forward(self, input_ids, attention_mask):
        _, pooled_output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        x = self.dropout(pooled_output)
        x = nn.functional.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x