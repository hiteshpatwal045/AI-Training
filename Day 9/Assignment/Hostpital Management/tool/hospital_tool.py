from langchain.tools import tool

PATIENTS = {}
APPOINTMENTS = {}


@tool
def register_patient(full_name: str, age: int, phone: str, symptoms: str = "") -> dict:
    """Register a new patient."""

    patient_id = f"P{1001 + len(PATIENTS)}"

    PATIENTS[patient_id] = {
        "full_name": full_name,
        "age": age,
        "phone": phone,
        "symptoms": symptoms
    }

    return {
        "status": "success",
        "patient_id": patient_id,
        "message": "Patient registered successfully"
    }


@tool
def check_doctor_availability(specialization: str, preferred_date: str = "") -> dict:
    """Check doctor availability."""
    
    return {
        "status": "success",
        "doctor_id": "D201",
        "doctor_name": "Dr Hitesh",
        "specialization": specialization,
        "available_slots": ["10:00", "11:00", "12:00"]
    }


@tool
def book_appointment(patient_id: str, doctor_id: str, appointment_date: str, time_slot: str) -> dict:
    """Book an appointment."""

    if patient_id not in PATIENTS:
        raise ValueError("Record Not Found")

    appointment_id = f"A{2001 + len(APPOINTMENTS)}"

    APPOINTMENTS[appointment_id] = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "appointment_date": appointment_date,
        "time_slot": time_slot
    }

    return {
        "status": "success",
        "appointment_id": appointment_id,
        "message": "Appointment booked successfully"
    }


@tool
def get_patient_medical_records(patient_id: str, authorized_role: str) -> dict:
    """Get patient medical records."""

    if authorized_role not in ["doctor", "nurse"]:
        raise ValueError("Unauthorized access")
    if patient_id not in PATIENTS:
        raise ValueError("Record Not Found")
    return {
        "patient_id": patient_id,
        "history": "Diabetes"
    }


@tool
def calculate_hospital_bill(patient_id: str, consultation_fee: float, lab_charges: float, treatment_charges: float, discount_percent: float = 0) -> dict:
    """Calculate hospital bill."""

    subtotal = (consultation_fee + lab_charges + treatment_charges)
    discount = subtotal * discount_percent / 100
    total = subtotal - discount

    return {
        "patient_id": patient_id,
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "total": round(total, 2)
    }
