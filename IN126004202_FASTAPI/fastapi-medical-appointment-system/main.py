from fastapi import FastAPI, Query, Response, status
from pydantic import BaseModel, Field

app = FastAPI()

# ═══════════════════════════════════════════════════════════════
# MODELS
# ═══════════════════════════════════════════════════════════════

class AppointmentRequest(BaseModel):
    patient_name: str = Field(..., min_length=2, max_length=100)
    doctor_id: int = Field(..., gt=0)
    date: str = Field(..., min_length=8)
    reason: str = Field(..., min_length=5)
    appointment_type: str = Field("in-person", min_length=2)
    senior_citizen: bool = False


class NewDoctor(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    specialization: str = Field(..., min_length=2)
    fee: int = Field(..., gt=0)
    experience_years: int = Field(..., gt=0)
    is_available: bool = True


# ═══════════════════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════════════════

doctors = [
    {
        "id": 1,
        "name": "Dr. Ananya Rao",
        "specialization": "Cardiologist",
        "fee": 800,
        "experience_years": 12,
        "is_available": True
    },
    {
        "id": 2,
        "name": "Dr. Rahul Mehta",
        "specialization": "Dermatologist",
        "fee": 600,
        "experience_years": 8,
        "is_available": True
    },
    {
        "id": 3,
        "name": "Dr. Sneha Iyer",
        "specialization": "Pediatrician",
        "fee": 700,
        "experience_years": 10,
        "is_available": False
    },
    {
        "id": 4,
        "name": "Dr. Kiran Patel",
        "specialization": "General",
        "fee": 400,
        "experience_years": 6,
        "is_available": True
    },
    {
        "id": 5,
        "name": "Dr. Vikram Shah",
        "specialization": "Cardiologist",
        "fee": 950,
        "experience_years": 15,
        "is_available": True
    },
    {
        "id": 6,
        "name": "Dr. Neha Kapoor",
        "specialization": "Dermatologist",
        "fee": 550,
        "experience_years": 7,
        "is_available": False
    }
]

appointments = []
appt_counter = 1


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def find_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor
    return None


def find_appointment(appointment_id: int):
    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:
            return appointment
    return None


def calculate_fee(base_fee: int, appointment_type: str, senior_citizen: bool = False):
    original_fee = base_fee

    if appointment_type.lower() == "video":
        calculated_fee = int(base_fee * 0.80)
    elif appointment_type.lower() == "emergency":
        calculated_fee = int(base_fee * 1.50)
    else:
        calculated_fee = base_fee

    discounted_fee = calculated_fee

    if senior_citizen:
        discounted_fee = int(calculated_fee * 0.85)

    return {
        "original_fee": original_fee,
        "final_fee": discounted_fee
    }


def filter_doctors_logic(
    specialization=None,
    max_fee=None,
    min_experience=None,
    is_available=None
):
    result = doctors

    if specialization is not None:
        result = [d for d in result if d["specialization"].lower() == specialization.lower()]

    if max_fee is not None:
        result = [d for d in result if d["fee"] <= max_fee]

    if min_experience is not None:
        result = [d for d in result if d["experience_years"] >= min_experience]

    if is_available is not None:
        result = [d for d in result if d["is_available"] == is_available]

    return result


# ═══════════════════════════════════════════════════════════════
# DAY 1 - GET ROUTES
# FIXED ROUTES FIRST
# ═══════════════════════════════════════════════════════════════

@app.get("/")
def home():
    return {"message": "Welcome to MediCare Clinic"}


@app.get("/doctors")
def get_all_doctors():
    available_count = len([d for d in doctors if d["is_available"]])

    return {
        "doctors": doctors,
        "total": len(doctors),
        "available_count": available_count
    }


@app.get("/appointments")
def get_all_appointments():
    return {
        "appointments": appointments,
        "total": len(appointments)
    }


@app.get("/doctors/summary")
def doctors_summary():
    total_doctors = len(doctors)
    available_count = len([d for d in doctors if d["is_available"]])
    most_experienced = max(doctors, key=lambda d: d["experience_years"])
    cheapest_fee = min(d["fee"] for d in doctors)

    specialization_count = {}
    for doctor in doctors:
        spec = doctor["specialization"]
        specialization_count[spec] = specialization_count.get(spec, 0) + 1

    return {
        "total_doctors": total_doctors,
        "available_count": available_count,
        "most_experienced_doctor": most_experienced["name"],
        "cheapest_consultation_fee": cheapest_fee,
        "doctors_per_specialization": specialization_count
    }


@app.get("/doctors/filter")
def filter_doctors(
    specialization: str = Query(None),
    max_fee: int = Query(None),
    min_experience: int = Query(None),
    is_available: bool = Query(None)
):
    result = filter_doctors_logic(
        specialization=specialization,
        max_fee=max_fee,
        min_experience=min_experience,
        is_available=is_available
    )

    return {
        "filtered_doctors": result,
        "count": len(result)
    }


@app.get("/appointments/active")
def get_active_appointments():
    active = [
        appt for appt in appointments
        if appt["status"] in ["scheduled", "confirmed"]
    ]

    return {
        "active_appointments": active,
        "count": len(active)
    }


@app.get("/appointments/search")
def search_appointments(patient_name: str = Query(...)):
    result = [
        appt for appt in appointments
        if patient_name.lower() in appt["patient"].lower()
    ]

    if not result:
        return {
            "message": f"No appointments found for patient: {patient_name}",
            "appointments": []
        }

    return {
        "patient_name": patient_name,
        "total_found": len(result),
        "appointments": result
    }


@app.get("/appointments/sort")
def sort_appointments(
    sort_by: str = Query("fee"),
    order: str = Query("asc")
):
    if sort_by not in ["fee", "date"]:
        return {"error": "sort_by must be 'fee' or 'date'"}

    if order not in ["asc", "desc"]:
        return {"error": "order must be 'asc' or 'desc'"}

    reverse = order == "desc"
    sorted_appointments = sorted(appointments, key=lambda a: a[sort_by], reverse=reverse)

    return {
        "sort_by": sort_by,
        "order": order,
        "appointments": sorted_appointments
    }


@app.get("/appointments/page")
def paginate_appointments(
    page: int = Query(1, ge=1),
    limit: int = Query(3, ge=1, le=20)
):
    start = (page - 1) * limit
    end = start + limit
    paged_data = appointments[start:end]

    total_pages = -(-len(appointments) // limit)

    return {
        "page": page,
        "limit": limit,
        "total": len(appointments),
        "total_pages": total_pages,
        "appointments": paged_data
    }


@app.get("/doctors/search")
def search_doctors(keyword: str = Query(...)):
    result = [
        doctor for doctor in doctors
        if keyword.lower() in doctor["name"].lower()
        or keyword.lower() in doctor["specialization"].lower()
    ]

    if not result:
        return {
            "message": f"No doctors found for keyword: {keyword}",
            "results": []
        }

    return {
        "keyword": keyword,
        "total_found": len(result),
        "results": result
    }


@app.get("/doctors/sort")
def sort_doctors(
    sort_by: str = Query("fee"),
    order: str = Query("asc")
):
    if sort_by not in ["fee", "name", "experience_years"]:
        return {"error": "sort_by must be 'fee', 'name', or 'experience_years'"}

    if order not in ["asc", "desc"]:
        return {"error": "order must be 'asc' or 'desc'"}

    reverse = order == "desc"
    sorted_doctors = sorted(doctors, key=lambda d: d[sort_by], reverse=reverse)

    return {
        "sort_by": sort_by,
        "order": order,
        "doctors": sorted_doctors
    }


@app.get("/doctors/page")
def paginate_doctors(
    page: int = Query(1, ge=1),
    limit: int = Query(3, ge=1, le=20)
):
    start = (page - 1) * limit
    end = start + limit
    paged_data = doctors[start:end]

    total_pages = -(-len(doctors) // limit)

    return {
        "page": page,
        "limit": limit,
        "total": len(doctors),
        "total_pages": total_pages,
        "doctors": paged_data
    }


@app.get("/doctors/browse")
def browse_doctors(
    keyword: str = Query(None),
    sort_by: str = Query("fee"),
    order: str = Query("asc"),
    page: int = Query(1, ge=1),
    limit: int = Query(4, ge=1, le=20)
):
    data = doctors

    if keyword:
        data = [
            d for d in data
            if keyword.lower() in d["name"].lower()
            or keyword.lower() in d["specialization"].lower()
        ]

    if sort_by not in ["fee", "name", "experience_years"]:
        return {"error": "sort_by must be 'fee', 'name', or 'experience_years'"}

    if order not in ["asc", "desc"]:
        return {"error": "order must be 'asc' or 'desc'"}

    reverse = order == "desc"
    data = sorted(data, key=lambda d: d[sort_by], reverse=reverse)

    total_found = len(data)
    total_pages = -(-total_found // limit)

    start = (page - 1) * limit
    end = start + limit

    return {
        "keyword": keyword,
        "sort_by": sort_by,
        "order": order,
        "page": page,
        "limit": limit,
        "total_found": total_found,
        "total_pages": total_pages,
        "results": data[start:end]
    }


@app.get("/appointments/by-doctor/{doctor_id}")
def get_appointments_by_doctor(doctor_id: int):
    doctor = find_doctor(doctor_id)

    if not doctor:
        return {"error": "Doctor not found"}

    doctor_appointments = [
        appt for appt in appointments
        if appt["doctor_id"] == doctor_id
    ]

    return {
        "doctor_id": doctor_id,
        "doctor_name": doctor["name"],
        "appointments": doctor_appointments,
        "total": len(doctor_appointments)
    }


# ═══════════════════════════════════════════════════════════════
# DAY 4 - CRUD
# FIXED ROUTES ABOVE VARIABLE ROUTES
# ═══════════════════════════════════════════════════════════════

@app.post("/appointments")
def create_appointment(appointment_data: AppointmentRequest):
    global appt_counter

    doctor = find_doctor(appointment_data.doctor_id)

    if not doctor:
        return {"error": "Doctor not found"}

    if not doctor["is_available"]:
        return {"error": f"{doctor['name']} is not available"}

    fee_data = calculate_fee(
        base_fee=doctor["fee"],
        appointment_type=appointment_data.appointment_type,
        senior_citizen=appointment_data.senior_citizen
    )

    appointment = {
        "appointment_id": appt_counter,
        "patient": appointment_data.patient_name,
        "doctor_id": doctor["id"],
        "doctor_name": doctor["name"],
        "date": appointment_data.date,
        "reason": appointment_data.reason,
        "type": appointment_data.appointment_type,
        "original_fee": fee_data["original_fee"],
        "fee": fee_data["final_fee"],
        "senior_citizen": appointment_data.senior_citizen,
        "status": "scheduled"
    }

    appointments.append(appointment)
    doctor["is_available"] = False
    appt_counter += 1

    return {
        "message": "Appointment created successfully",
        "appointment": appointment
    }


@app.post("/doctors", status_code=201)
def add_doctor(new_doctor: NewDoctor, response: Response):
    for doctor in doctors:
        if doctor["name"].lower() == new_doctor.name.lower():
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Doctor with this name already exists"}

    new_entry = {
        "id": max(d["id"] for d in doctors) + 1,
        "name": new_doctor.name,
        "specialization": new_doctor.specialization,
        "fee": new_doctor.fee,
        "experience_years": new_doctor.experience_years,
        "is_available": new_doctor.is_available
    }

    doctors.append(new_entry)

    return {
        "message": "Doctor added successfully",
        "doctor": new_entry
    }


@app.post("/appointments/{appointment_id}/confirm")
def confirm_appointment(appointment_id: int, response: Response):
    appointment = find_appointment(appointment_id)

    if not appointment:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Appointment not found"}

    appointment["status"] = "confirmed"

    return {
        "message": "Appointment confirmed",
        "appointment": appointment
    }


@app.post("/appointments/{appointment_id}/cancel")
def cancel_appointment(appointment_id: int, response: Response):
    appointment = find_appointment(appointment_id)

    if not appointment:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Appointment not found"}

    appointment["status"] = "cancelled"

    doctor = find_doctor(appointment["doctor_id"])
    if doctor:
        doctor["is_available"] = True

    return {
        "message": "Appointment cancelled",
        "appointment": appointment
    }


@app.post("/appointments/{appointment_id}/complete")
def complete_appointment(appointment_id: int, response: Response):
    appointment = find_appointment(appointment_id)

    if not appointment:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Appointment not found"}

    appointment["status"] = "completed"

    doctor = find_doctor(appointment["doctor_id"])
    if doctor:
        doctor["is_available"] = True

    return {
        "message": "Appointment completed",
        "appointment": appointment
    }


@app.put("/doctors/{doctor_id}")
def update_doctor(
    doctor_id: int,
    response: Response,
    fee: int = Query(None),
    is_available: bool = Query(None)
):
    doctor = find_doctor(doctor_id)

    if not doctor:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Doctor not found"}

    if fee is not None:
        doctor["fee"] = fee

    if is_available is not None:
        doctor["is_available"] = is_available

    return {
        "message": "Doctor updated successfully",
        "doctor": doctor
    }


@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, response: Response):
    doctor = find_doctor(doctor_id)

    if not doctor:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Doctor not found"}

    active_appointments = [
        appt for appt in appointments
        if appt["doctor_id"] == doctor_id and appt["status"] == "scheduled"
    ]

    if active_appointments:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Cannot delete doctor with scheduled appointments"}

    doctors.remove(doctor)

    return {
        "message": f"Doctor '{doctor['name']}' deleted successfully"
    }


# ═══════════════════════════════════════════════════════════════
# VARIABLE ROUTES LAST
# ═══════════════════════════════════════════════════════════════

@app.get("/doctors/{doctor_id}")
def get_doctor_by_id(doctor_id: int):
    doctor = find_doctor(doctor_id)

    if not doctor:
        return {"error": "Doctor not found"}

    return {"doctor": doctor}