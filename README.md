# 🧠 Deepfake Detection App (Local Prototype)

This project is a **local deepfake detection prototype** built using **Python, PyTorch, and Gradio**.

The goal of this project is to:
- Build an end-to-end ML pipeline
- Load a trained model
- Run inference on uploaded images
- Display REAL / FAKE predictions via a simple UI

---

## ✅ Current Status

✔ Project setup in VS Code  
✔ Virtual environment created  
✔ Gradio app running locally  
✔ Model loading and inference pipeline working  
✔ Predictions displayed in browser  

⚠️ Note:  
The current model is a **placeholder / lightly trained model**.  
Proper training using FaceForensics++ (C23) will be added later.

---

## 📁 Project Structure

deepfake_app/
│
├── app.py # Gradio application
├── model.pth # Model weights (currently placeholder)
├── create_model.py # One-time helper to create model.pth
├── README.md # Project documentation
├── data/
│ ├── real/ # Real face images (for training)
│ └── fake/ # Fake face images (for training)
└── venv/ # Python virtual environment

deepfake_app/
│
├── app.py # Gradio application
├── model.pth # Model weights (currently placeholder)
├── create_model.py # One-time helper to create model.pth
├── README.md # Project documentation
├── data/
│ ├── real/ # Real face images (for training)
│ └── fake/ # Fake face images (for training)
└── venv/ # Python virtual environment

2. Run the app:
3. Open browser and upload an image.

---

## 🔮 Next Steps (Planned)

- Train model properly using FaceForensics++ faces
- Add face detection (MTCNN)
- Improve accuracy
- Deploy to Hugging Face Spaces

---

## 🧑‍💻 Author

Built step-by-step as a learning-focused ML project.
