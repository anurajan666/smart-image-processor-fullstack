# 📸 Smart Image Processor (Full-Stack App)

A full-stack web application that allows users to upload and process images using powerful Python backend processing and a simple frontend interface.

---

## 🚀 Features

- Upload images from browser
- Apply image processing:
  - Grayscale
  - Blur
  - Edge Detection
- Instant preview of processed images
- Simple and clean UI
- REST API powered backend

---

## 🏗️ Tech Stack

### 🔹 Backend
- Python
- Flask
- OpenCV
- NumPy

### 🔹 Frontend
- HTML / JavaScript (can be upgraded to React)
- Fetch API

---

## 📁 Project Structure
smart-image-processor-fullstack/
│── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── uploads/
│ └── outputs/
│
│── frontend/
│ └── index.html
│
│── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/anurajan666/smart-image-processor-fullstack.git
cd smart-image-processor-fullstack

2️⃣ Setup Backend
cd backend
pip install -r requirements.txt
python app.py

Backend will run on:

http://localhost:5000
3️⃣ Run Frontend

Open this file in your browser:

frontend/index.html
🔌 API Endpoint
POST /process

Request:

Form Data:
image: file
operation: grayscale | blur | edges

Response:

Processed image file
🖼️ Example Workflow
Upload an image
Select processing type
Click Process
View the processed image instantly

---

📦 Future Improvements
Convert frontend to React (Vite)
Add drag & drop upload
Add authentication (JWT)
Deploy to AWS / VPS
Add more filters (AI-based enhancements)
Batch image processing

🌐 Deployment Ideas
Backend: AWS EC2 / Docker
Frontend: Netlify / Vercel
Reverse Proxy: Nginx

🤝 Contributing

Pull requests are welcome! Feel free to open issues for suggestions or improvements.

📄 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Anurajan
[GitHub](https://github.com/anurajan666) · [LinkedIn](https://linkedin.com/in/anurajanmariyathas) · [Upwork](https://www.upwork.com/freelancers/~018650b61246007c00)
