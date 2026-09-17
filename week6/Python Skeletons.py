class Patient:
    def __init__(self, patient_id, name, address, contactdetails):
        self.patientid = patient_id
        self.name = name
        self.address = address
        self.contactdetails = contactdetails

    def viewPatientRecord(self):
        pass
    def UpdateInfo(self):
        pass
    def CheckAvailability(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name, address, contactinformation, specialtyofcare):
        self.practitioner_id = practitioner_id
        self.name = name
        self.address = address
        self.contactinformation = contactinformation
        self.specialtyofcare = specialtyofcare

    def ViewRecords(self):
        pass
    def ViewSchedule(self):
        pass
    def acceptAppointment(self):
        pass
    def CancelAppointment(self):
        pass
    def PatientRecord(self):
        pass

class Appointment:
    def __init__(self, appointment_id, patient_id, practitioner_id, receptionist_id, appointment_datetime):
        self.appointmnet_id = appointment_id
        self.patient_id = patient_id
        self.practitioner_id = practitioner_id
        self.receptionist_id = receptionist_id
        self.appointment_datetime = appointment_datetime

    def schedule(self):
        pass
    def Cancel(Self)
        pass
    def ModifyAppointmentSchedule(self):
        pass      