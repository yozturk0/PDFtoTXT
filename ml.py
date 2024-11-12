import torch.nn as nn
import torch.optim as optim

class CRNN(nn.Module):
    def __init__(self, num_classes):
        super(CRNN, self).__init__()
        self.cnn = nn.Sequential(
            # Add convolutional layers for feature extraction
            nn.Conv2d(1, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
        )
        self.rnn = nn.LSTM(128 * 16, 256, bidirectional=True, batch_first=True)
        self.fc = nn.Linear(512, num_classes)

    def forward(self, x):
        x = self.cnn(x)
        x = x.permute(0, 2, 3, 1)  # rearrange for RNN
        x, _ = self.rnn(x)
        x = self.fc(x)
        return x

# Load the dataset
# text_recognition_dataset = TextRecognitionDataset(...)
# text_loader = DataLoader(text_recognition_dataset, batch_size=32, shuffle=True)

# Initialize the CRNN model
num_classes = 36  # 26 letters + 10 digits
model = CRNN(num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(10):
    for images, labels in text_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch + 1}, Loss: {loss.item()}")
