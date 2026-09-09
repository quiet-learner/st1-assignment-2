Assignment 2 Case Study

Stage 2 Tutorial From Problems to Requirements

Week 5 | 60 minutes

# Learning goals

- Analyse stakeholders.
- Distinguish functional and non-functional requirements.
- Recognise ambiguity and unsupported requirements.
- Define scope.
- Develop user stories and acceptance criteria.
- Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

| **Stakeholder**      | **Need**                                                                  | **Potential conflict**                                                                                            |
| -------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Receptionist         | Access to create, modify, and cancel patient data and appointments.       | May be resistant to change in workflow, from paper to computer software requires training and computer knowledge. |
| Patient              | Book appointments and change information.                                 | May want off site access for convenience but clients may want on site access only.                                |
| Practitioner         | Access to their calendar of appointments.                                 | Needs information that's current/up to date, including patient records.                                           |
| System administrator | Access to change privileges to staff and troubleshoot problems.           | May not have the funds for full-time service so they outsource an agreement with a separate company.              |
| Clinic manager       | Wants basic operational control over appointments so there are no errors. | Wants something simple so they may not get the functions that need and only want the minimum to start.            |

# Activity 2 - Functional or Non-Functional?

✔️ Functional □ Non-functional The system shall allow staff to cancel an appointment.

□ Functional ✔️ Non-functional The system should remain responsive for the course-scale dataset.

✔️ Functional □ Non-functional The system shall retain cancelled appointments.

✔️Functional □ Non-functional Core business logic should be independently testable.

✔️ Functional □ Non-functional The system shall search for a patient by ID.

# Activity 3 - Repair Ambiguous Requirements

The system should be easy to use.

**Problem**: easy to use can mean many things. **Clarification question**: Can you clarify how the system should be easy to use? For example simple navigation or accessibility options for staff that have trouble with computers.

Patient search should be fast.

**Problem**: does not say how they can search for that patient. **Clarification question**: With there be a database implementation with unique id's? Or as simple as name search with verify of date of birth?

The system should securely manage data.

**Problem**: Does not explain how the system will ensure that data is managed securely. **Clarification question**: What security will be implemented, examples such as access controls, and two-factor authentication?

Appointments should normally be easy to cancel.

**Problem**: no explanation on who can cancel these appointments **Clarification question**: Who do you want access to cancel appointments? Such as reception, practitioners, patients.

# Activity 4 - AI Requirements Audit

Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.

| AI suggestion                             | Classification                   | Evidence / reason                                                                                                                                                                                       |
| ----------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Patients receive SMS reminders.           | Assumption requiring validation. | Useful for patients but not required. Clinic wants something simple to use. Client may request to add this later. Can ask client for clarification.                                                     |
| Facial recognition login.                 | unsupported                      | Facial recognition sounds out of scope for this project as they want something for a small clinic.                                                                                                      |
| Receptionists create appointments.        | Confirmed                        | Receptionists are the first line of contact for patients, and they answer the phones to patients, so access is needed for this staff member.                                                            |
| Online payment.                           | Assumption requiring validation. | Payments have not been discussed if they are cash/card or a payment online. Client verification required.                                                                                               |
| Practitioners view schedules.             | Confirmed                        | Practitioners need schedule to know who to call in the office next.                                                                                                                                     |
| AI recommends treatments.                 | Out of Scope                     | Ai should not be giving recommendations for treatments.                                                                                                                                                 |
| Cancelled appointments remain in history. | Assumption requiring validation. | My assumption is the canceled appointment becomes available for use and just talking to storing that canceled history for record keeping. Unknown if client wants to store that information in records. |

# Exit question

Why is 'AI suggested it' not sufficient evidence for a requirement?

An ai suggestion is based on other clinic/businesses across the world may use but not all features will benefit this clinic requirements. Ai suggestion may be useful to implement on a case-by-case basis depending on client and business needs.