# 🩺 Medical Appointment System

A FastAPI-based backend project to manage doctors, appointments, consultations, filtering, searching, sorting, pagination, and appointment workflow.

---

## ✨ Project Overview

The **Medical Appointment System** is a mini clinic management API built using **FastAPI**.  
It allows users to:

- view doctors
- book appointments
- confirm, cancel, and complete appointments
- filter doctors
- search doctors and appointments
- sort and paginate data
- manage doctor availability

This project was built as a complete FastAPI practice project covering **Day 1 to Day 6 concepts**.

---

## 🚀 Features

### ✅ Day 1 — GET APIs
- Home route
- Get all doctors
- Get doctor by ID
- Get all appointments
- Doctors summary endpoint

### ✅ Day 2 — POST + Pydantic
- Appointment booking using request body
- Pydantic model validation
- Field constraints like `min_length`, `gt`, `default`

### ✅ Day 3 — Helper Functions
- `find_doctor()`
- `find_appointment()`
- `calculate_fee()`
- `filter_doctors_logic()`

### ✅ Day 4 — CRUD Operations
- Add a new doctor
- Update doctor details
- Delete doctor
- Proper status handling with `201` and `404`

### ✅ Day 5 — Multi-Step Workflow
- Schedule appointment
- Confirm appointment
- Cancel appointment
- Complete appointment
- View active appointments
- View appointments by specific doctor

### ✅ Day 6 — Advanced APIs
- Search doctors
- Sort doctors
- Paginate doctors
- Search appointments
- Sort appointments
- Paginate appointments
- Combined browse endpoint

---

## 🏥 Doctors Data

Each doctor contains:

- `id`
- `name`
- `specialization`
- `fee`
- `experience_years`
- `is_available`

Specializations used in the project:
- Cardiologist
- Dermatologist
- Pediatrician
- General

---

## 📅 Appointment Data

Each appointment stores:

- `appointment_id`
- `patient`
- `doctor_id`
- `doctor_name`
- `date`
- `reason`
- `type`
- `original_fee`
- `fee`
- `senior_citizen`
- `status`

Appointment statuses:
- `scheduled`
- `confirmed`
- `cancelled`
- `completed`

---

## 💰 Fee Rules

Consultation fees are calculated using appointment type:

- **video** → 80% of base fee
- **in-person** → full fee
- **emergency** → 150% of base fee

Extra rule:
- **senior citizen** → additional **15% discount** after fee calculation

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **Swagger UI**

---

## 📂 Project Structure

```bash
fastapi-medical-appointment-system/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
````

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the server

```bash
uvicorn main:app --reload
```

### 3. Open Swagger UI

```bash
http://127.0.0.1:8000/docs
```

---

## 🧪 API Testing

All APIs were tested in **Swagger UI**.

Screenshots for all required questions are stored inside the **screenshots** folder.

Example screenshot names:

* `Q1_home_route.png`
* `Q5_doctors_summary.png`
* `Q8_create_appointment.png`
* `Q14_confirm_appointment.png`
* `Q20_browse_doctors.png`

---

## 📌 Concepts Covered

This project includes:

* GET APIs
* POST with Pydantic
* Helper functions
* Query parameters
* CRUD operations
* Validation and error handling
* Multi-step workflow
* Search
* Sort
* Pagination
* Combined browse logic

---

## 🎯 Learning Outcome

By building this project, I practiced:

* FastAPI route design
* request and response handling
* Pydantic validation
* helper function design
* filtering with query parameters
* business logic implementation
* CRUD workflow
* API testing using Swagger

---

## 👩‍💻 Author

**Kirthika R S**

---

## 🌟 Final Note

This project is a complete **FastAPI Medical Appointment System** designed to simulate a real-world clinic booking workflow in a simple and structured way.

````

