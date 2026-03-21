# Medical Appointment System - FastAPI Project

This is a FastAPI-based Medical Appointment System project developed to manage doctors, appointments, filtering, searching, sorting, pagination, and appointment workflow operations.

## Project Structure

- `main.py` - Main FastAPI application
- `requirements.txt` - Required Python packages
- `README.md` - Project documentation
- `screenshots/` - Swagger API testing screenshots

## Features Implemented

### Day 1 - GET APIs
- Home route
- List all doctors
- Get doctor by ID
- List all appointments
- Doctors summary

### Day 2 - POST + Pydantic
- Appointment creation using request body
- Pydantic validation using `Field()`

### Day 3 - Helper Functions
- `find_doctor()`
- `find_appointment()`
- `calculate_fee()`
- `filter_doctors_logic()`

### Day 4 - CRUD Operations
- Add new doctor
- Update doctor
- Delete doctor

### Day 5 - Multi-Step Workflow
- Create appointment
- Confirm appointment
- Cancel appointment
- Complete appointment
- View active appointments
- View appointments by doctor

### Day 6 - Advanced APIs
- Search doctors
- Sort doctors
- Paginate doctors
- Search appointments
- Sort appointments
- Paginate appointments
- Combined browse endpoint

## Doctors Dataset

The project uses a custom dataset of doctors with:
- id
- name
- specialization
- fee
- experience_years
- is_available

## Appointment Logic

Appointments include:
- appointment_id
- patient name
- doctor details
- date
- reason
- appointment type
- fee calculation
- senior citizen discount
- status tracking

## Fee Calculation Rules

- `video` consultation = 80% of base fee
- `in-person` consultation = full fee
- `emergency` consultation = 150% of base fee
- senior citizen = additional 15% discount after calculation

## API Testing

All APIs were tested using Swagger UI:

`http://127.0.0.1:8000/docs`

Screenshots for all required questions are included in the `screenshots/` folder.

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
