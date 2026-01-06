import torch
import torchvision.models as models

# Load a pretrained ResNet18 model
model = models.resnet18(pretrained=True)

# Change final layer to 2 classes (REAL / FAKE)
model.fc = torch.nn.Linear(model.fc.in_features, 2)

# Save the model
torch.save(model.state_dict(), "model.pth")

print("✅ model.pth created successfully")
