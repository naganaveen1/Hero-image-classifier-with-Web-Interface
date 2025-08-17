import torch
import torch.nn as nn
from torchvision import models, transforms
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image

# ==================
# Flask Setup
# ==================
app = Flask(__name__)
CORS(app)

# ==================
# Load Model
# ==================
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, 4)  # 4 heroes
model.load_state_dict(torch.load("telugu_hero_model.pth", map_location="cpu"))
model.eval()

# Class labels
class_names = ['Akhil', 'Brahmi', 'Nani', 'RamCharan']

# Image transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

# ==================
# Routes
# ==================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    image = Image.open(file.stream).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image_tensor)
        predicted_idx = torch.argmax(outputs, dim=1).item()

    return jsonify({"prediction": class_names[predicted_idx]})

if __name__ == "__main__":
    app.run(debug=True)
