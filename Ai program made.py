# List to store appointments
appointments = []

def add_appointment(patient_name, doctor_name, appointment_time):
    if not appointment_time:
        raise ValueError("A Time must be chosen")
    appointment = {
        "patient": patient_name,
        "doctor": doctor_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    print("Appointment added successfully!")

# Example usage
add_appointment("John Smith", "Dr Brown", "10:00 AM")
add_appointment("Sarah Lee", "Dr Jones", "2:30 PM")

#Part F - Verify Behaviour
# •	Two appointments for the same practitioner/time
# •	Strange input such as patient_name=None or appointment_time=None

print (f"Normal appointment")
add_appointment("Jimbo tuka", "Dr Donothing", "14:20 PM")
print (f"Blank patient name")
add_appointment("", "Dr Jones", "10:00 AM")
print("\n")
print (f"Two appointments for the same practitioner/time")
add_appointment("John Smith", "Dr Brown", "10:00 AM")
add_appointment("John Smith", "Dr Brown", "10:00 AM")
print("\n")
print (f"testing > Strange input such as patient_name=None or appointment_time=None ")
add_appointment("", "Dr Jones", "10:00 AM")
add_appointment("kang", "Dr roo", "")




# Display all appointments
for appt in appointments:
    print(
        f"Patient: {appt['patient']}, "
        f"Doctor: {appt['doctor']}, "
        f"Time: {appt['time']}"
    )

add_appointment("Jimmy car", "Dr Dolittle", "14:20 PM")