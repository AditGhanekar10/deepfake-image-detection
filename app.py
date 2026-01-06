import gradio as gr
import torch
import torchvision.models as models
import cv2
import numpy as np

# -----------------------------
# Load model
# -----------------------------
device = torch.device("cpu")

model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, 2)

model.load_state_dict(torch.load("model.pth", map_location=device))
model.eval()

# -----------------------------
# Prediction function
# -----------------------------
def predict(image):
    # Resize image
    image = cv2.resize(image, (224, 224))

    # Normalize
    image = image / 255.0

    # Convert to tensor
    image = torch.tensor(image).permute(2, 0, 1).unsqueeze(0).float()

    with torch.no_grad():
        outputs = model(image)
        probs = torch.softmax(outputs, dim=1)
        pred = torch.argmax(probs, dim=1).item()
        confidence = probs[0][pred].item()

    label = "FAKE ❌" if pred == 1 else "REAL ✅"
    return f"{label}  (confidence: {confidence:.2f})"

# -----------------------------
# Gradio UI
# -----------------------------
app = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="numpy", label="Upload a face image"),
    outputs=gr.Textbox(label="Result"),
    title="🧠 Deepfake Detector",
    description="Upload a face image and check if it is REAL or FAKE"
)

app.launch()

