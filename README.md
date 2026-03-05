FastAPI Demo Project 🚀

## 📌 Project Description

This is a simple demo project built using **FastAPI**, a modern and fast web framework for building APIs with Python.

The project demonstrates how to create REST APIs, run a FastAPI server, and test endpoints using automatic documentation.

---

## 🛠 Tech Stack

* Python
* FastAPI
* Uvicorn

---

## 📂 Project Structure

```
Fastapidemo/
│
├── main.py
├── requirements.txt
├── README.md
└── app/
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/fastapi-demo.git
```

### 2. Go to the project folder

```
cd fastapi-demo
```

### 3. Create a virtual environment

```
python -m venv venv
```

### 4. Activate the environment

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

### 5. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the FastAPI Server

```
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## 📑 API Documentation

FastAPI automatically generates API docs.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## ✨ Example Endpoint

```
GET /
```

Response:

```
{
  "message": "Hello World"
}
```

---

## 👨‍💻 Author

Your Name

---

## 📜 License

This project is for learning and demonstration purposes.
