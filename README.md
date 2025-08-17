# 🎬 Telugu Hero Classifier

A deep learning project that classifies Telugu movie heroes from images using **PyTorch** and a **Flask web app**. The model is trained on a custom dataset of Telugu actors and deployed with a simple yet professional front‑end built with **HTML, CSS, and JavaScript**.

---

## 🚀 Features

* Upload an image of a Telugu hero.
* Classifies into one of the supported hero categories.
* Interactive front‑end with live image preview.
* Backend powered by Flask & PyTorch.
* Ready for deployment (local or cloud).

---

## 🏗️ Tech Stack

* **Deep Learning**: PyTorch, ResNet‑18
* **Backend**: Flask, TorchVision
* **Frontend**: HTML, CSS, JavaScript
* **Deployment**: Flask server (can be extended to Render, HuggingFace Spaces, or Heroku)

---

## 📂 Project Structure

```
project/
│ app.py                   # Flask backend
│ telugu_hero_model.pth    # Trained PyTorch model
│
├── templates/
│   └── index.html         # Frontend HTML
│
└── static/
    ├── style.css          # Styling
    └── script.js          # Client-side logic
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/telugu-hero-classifier.git
   cd telugu-hero-classifier
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Flask app**

   ```bash
   python app.py
   ```

4. **Open in browser**

   ```
   http://127.0.0.1:5000/
   ```

---

## 🧠 Model Details

* Base architecture: **ResNet‑18**
* Modified final layer for 4 Telugu heroes:

  * Akhil
  * Brahmanandam (Brahmi)
  * Nani
  * Ram Charan
* Trained with transfer learning on custom dataset.

---

## 📸 Demo

![App Screenshot](demo.png)


https://github.com/user-attachments/assets/6a0bf54b-1a10-4532-ab0f-bbb3be97437d


---

## 🚀 Deployment

You can deploy this project on:

* **Render** (free Flask hosting)
* **HuggingFace Spaces** (Gradio/Flask)
* **Heroku** (requires Procfile)

---

## 🤝 Contributing

Contributions are welcome! If you’d like to improve the model or frontend:

1. Fork the repo
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

* PyTorch team for the ResNet model.
* Flask for backend simplicity.
* Inspiration from Telugu Cinema ❤️
