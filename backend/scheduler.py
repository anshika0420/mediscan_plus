# Very small in-memory scheduler for demo purposes.
import datetime
SAMPLE_SLOTS = [
    "2025-09-10T09:00:00",
    "2025-09-10T10:00:00",
    "2025-09-10T11:00:00",
    "2025-09-11T09:00:00",
]

def schedule_appointment(patient: dict, preferred_date: str = None) -> dict:
    # naive scheduling: pick first free slot
    slot = SAMPLE_SLOTS[0]
    # Ideally, you would integrate with a DB and mark the slot taken
    return {"patient": patient, "slot": slot, "method":"demo"}
