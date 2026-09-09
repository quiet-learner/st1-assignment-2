SmartCare v0.2 - Requirements Specification Template

# Problem and Scope

SmartCare is a small clinic that is using paper based booking system, with paper records and manual preccesess. The clinic has experienced multiple operational issues including, duplicate bookings, limited status of practitioner availability, and manually canceling appointments. The clinic is now requesting a simple software system to handle these issues to get away from physical paperwork.

# 2\. Stakeholders

| Stakeholder          | Need                                                                      | Evidence                                                                                              |
| -------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Receptionist         | Access to create, modify, and cancel patient data and appointments.       | Receptionist are key staff that will handle appointments.                                             |
| Patient              | Book appointments and change information.                                 | Patients are the people attending appointments so they need a method to book them.                    |
| Practitioner         | Access to their calendar of appointments.                                 | Assumption: practitioner can access their calendar to view next appoints and the next person to call. |
| System administrator | Access to change privileges to staff and troubleshoot problems.           | Need someone that can handle administrator duties to give and take away privileges to the system.     |
| Clinic manager       | Wants basic operational control over appointments so there are no errors. | Has access to the system to override potential issue in day to day work hours.                        |

# 3\. Functional Requirements

**FR-01:** The system will allow the receptionist book appointments for patients.

**FR-02:** The system will allow the receptionist to cancel appointments.

**FR-03:** The system will allow patients to update their contact information.

**FR-04:** The system will allow practitioners to view their schedule.

**FR-05:** The system will allow practitioners to view patient records.

**FR-06:** The system will show practitioners availability schedule.

**FR-07:** The system will stop the receptionist from double booking an appointment.

**FR-08:** The system will allow receptionists to search patient records by name or a unique identifier.

**FR-09:** The system will allow receptionists to create new patient profiles.

**FR-10:** The system will update its availability if an appointment is cancelled.

# 4\. Non-Functional Requirements

NFR-01: **usability:** The system should have some custom features to make it simple and easy to use for this clinic.

NFR-02: **Maintainability:** maintenance should be done at non-work hours and not disrupt work conditions.

NFR-03: **Reliability:** The system will not allow double booking and work seamlessly every day.

NFR-04: **Data Integrity:** The system should store the patient data securely and safely, with minimal access to staff as needed. Access should be checked on regularly to double check all personal that has access level control.

# 5\. User Stories

US-01: As a receptionist, I want to search patients by name and match their date of birth, so that I can find their information quickly.

US-02: As a practitioner, I want to view my appointments, so that I can see my daily schedule.

US-03: As a receptionist, I want to cancel an appointment, so that the patient can reschedule.

US-04: As a receptionist, I can create a new patient profile, so a new user can book appointments.

# 6\. Acceptance Criteria

Acceptance Criteria 1:

**GIVEN –** a patient with name jimmy jumper and date of birth 1988 exists on record

**When –** the receptionist searches that name and provided date of birth

**Then –** the system displays the patients profile record.

Acceptance Criteria 2 negative:

**Given –** a patient with name carrion lock with date of birth 1999 exists on record

**When –** the reception searches that name and provided date of birth

**Then -** the system displays no patient on record matching data provided

Acceptance Criteria 1:

**GIVEN –** the practitioner has twelve schedules' appointments today

**When –** the practitioner opens the calendar with listed appointments

**Then –** The system will display patient identities and time slots booked for the day.

Acceptance Criteria 2 negative:

**Given –** the practitioner has twelve schedules' appointments today

**When –** the practitioner opens the calendar with listed appointments

**Then -** the system displays a different calendar day rather than today's.

Acceptance Criteria 1:

**GIVEN –** an existing appointment is currently scheduled in the system

**When –** the receptionist cancels the appointment

**Then –** the system will provide feedback to user and make that time slot available for another patient.

Acceptance Criteria 1:

**GIVEN –** a new patient wants to book a appointment

**When –** the receptionist will input patient information in a new patient record

**Then –** the patient can book an appointment.

# 7\. Assumptions and Open Questions

Basic assumptions include how data will be stored such as, using identifiers for patients. But its assumed when searching patients in the system with just the name and date of birth required. More assumptions include how the software will function in day to day operations with scheduling and handling bookings.

Open Questions that require further clarification by the client include terms that are vague or need more specifications. Anything vague needs clarification as the client should have a more understanding of what hey actually need compared to the developer.

# 8\. AI Requirements Review Record

| AI suggestion                                                                                                                 | Evidence?                                                                                                                                                                                              | Decision                    | Reason                                                | Verification |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | ----------------------------------------------------- | ------------ |
| information required for appointments is not specified.                                                                       | The brief wants the software to manage appointments but does not specify what information is required to create one.                                                                                   | Requires validation/testing | Needed for functionality and testing                  | Needed       |
| It is unclear what appointment can be cancelled.                                                                              | The brief mentions a manual cancellation process but does not specify those rules.                                                                                                                     | Requires validation         | Needed to specify requirements to cancel appointment. | Needed       |
| The schedule has not been defined yet.                                                                                        | No mention of a schedule but assumption would be that the practitioner will use the software to all in patients rather than speak with the reception for every appointment to find out who to call in. | Requires validation         | Schedule required to use a software booking system.   | Needed       |
| The term double booking is not defined: without a definition for a double booking testing cannot determine expected behavior. | Brief mentions duplicate bookings but does not specify the conflict reasons.                                                                                                                           | Accepted                    | Should not be possible to double book appointments    | Needed       |
| Patent profiles contents are not defined                                                                                      | The brief has no mention of who can book appointments (i.e. members, people with profile, people that have id, walk ins) but does accept appointments.                                                 | Accepted                    | Needed to set requirements.                           | Needed       |