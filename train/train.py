import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from transformers import BertModel, BertTokenizer

# Load the pre-trained tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Load the custom dataset
data = pd.read_csv('path/to/dataset.csv')

# Tokenize the input sentences and convert them to input IDs and attention masks
inputs = tokenizer(data['sentence'].tolist(), padding=True, truncation=True, return_tensors='pt')
labels = torch.tensor(data['sentiment'].tolist())

# Split the dataset into training and validation sets
train_inputs, train_labels = inputs[:800], labels[:800]
val_inputs, val_labels = inputs[800:], labels[800:]

# Initialize the model
model = BertForSentimentAnalysis(n_classes=3)

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=2e-5)

# Train the model
epochs = 10
batch_size = 32
for epoch in range(epochs):
    for i in range(0, len(train_inputs), batch_size):
        optimizer.zero_grad()
        batch_inputs = train_inputs['input_ids'][i:i+batch_size]
        batch_masks = train_inputs['attention_mask'][i:i+batch_size]
        batch_labels = train_labels[i:i+batch_size]
        outputs = model(batch_inputs, batch_masks)
        loss = criterion(outputs, batch_labels)
        loss.backward()
        optimizer.step()

    # Evaluate the model on the validation set
    with torch.no_grad():
        val_outputs = model(val_inputs['input_ids'], val_inputs['attention_mask'])
        val_loss = criterion(val_outputs, val_labels)
        val_acc = (val_outputs.argmax(1) == val_labels).sum().item() / len(val_labels)
        print(f'Epoch {epoch+1}: Val Loss = {val_loss:.4f}, Val Acc = {val_acc:.4f}')
