Assignment 2 – Case Study Lab

Stage 2 Lab Activities

SmartCare Requirements Engineering

AI OFF -> AI ON -> VERIFY | 1 hour

# Learning objectives

- Analyse the SmartCare client brief.
- Identify stakeholders and scope.
- Write functional and non-functional requirements.
- Develop user stories and Given-When-Then acceptance criteria.
- Use AI to critique requirements without allowing it to invent stakeholder needs.
- Produce SmartCare Requirements Specification v1.0.

# Part A - Client Brief: AI OFF

SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. Management wants a small, maintainable patient, practitioner and appointment system.

# Part B - Stakeholders and Scope: AI OFF

Identify at least four stakeholders. Create In Scope and Out of Scope lists. Label uncertain features as provisional rather than confirmed.

| **Stakeholders**     |
| -------------------- |
| Receptionist         |
| Patient              |
| Practitioner         |
| System administrator |

| **In Scope**                | **Provision/Confirmed** |
| --------------------------- | ----------------------- |
| Patient information         | Confirmed               |
| Book Appointments           | Confirmed               |
| Cancel appointments         | Confirmed               |
| Patient records             | Confirmed               |
| Practitioner schedule       | Confirmed               |
| Online appointment handling | Provision               |
| Appointment status          | Provision               |

| **Out of Scope**           | **Provision/Confirmed** |
| -------------------------- | ----------------------- |
| Online Payments            | Provision               |
| SMs reminders              | Provisional             |
| Facial recognition         | Provisional             |
| Prescription printing      | Provisional             |
| Specialist recommendations | Provisional             |

# Part C - Functional Requirements: AI OFF

Write 8-12 numbered functional requirements using FR-01, FR-02 and so on. Each should describe one observable capability.

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

# Part D - Non-Functional Requirements: AI OFF

Write 4-6 numbered non-functional requirements covering appropriate qualities such as reliability, maintainability, usability, data integrity or testability.

**NFR – 1:** **usability**: The system should have some custom features to make it simple and easy to use for this clinic.

**NFR – 2: Maintainability:** maintenance should be done at non-work hours and not disrupt work conditions.

**NFR – 3: Reliability:** The system will not allow double booking and work seamlessly every day.

**NFR – 4: Data Integrity:** The system should store the patient data securely and safely, with minimal access to staff as needed. Access should be checked on regularly to double check all personal that has access level control.

# Part E - User Stories and Acceptance Criteria: AI OFF

Write 4-6 user stories. For at least three, create Given-When-Then acceptance criteria including one negative or failure scenario.

**US -1:** As a receptionist, I want to search patients by name and match their date of birth so that I can find their information quickly.

Acceptance Criteria 1:

**GIVEN –** a patient with name jimmy jumper and date of birth 1988 exists on record

**When –** the receptionist searches that name and provided date of birth

**Then –** the system displays the patients profile record.

Acceptance Criteria 2 negative:

**Given –** a patient with name carrion lock with date of birth 1999 exists on record

**When –** the reception searches that name and provided date of birth

**Then -** the system displays no patient on record matching data provided

**US -2:** As a practitioner, I want to view my appointments, so that I can see my daily schedule.

Acceptance Criteria 1:

**GIVEN –** the practitioner has twelve schedules' appointments today

**When –** the practitioner opens the calendar with listed appointments

**Then –** The system will display patient identities and time slots booked for the day.

Acceptance Criteria 2 negative:

**Given –** the practitioner has twelve schedules' appointments today

**When –** the practitioner opens the calendar with listed appointments

**Then -** the system displays a different calendar day rather than today's.

**US-3:** As a receptionist, I want to cancel an appointment, so that the patient can reschedule.

Acceptance Criteria 1:

**GIVEN –** an existing appointment is currently scheduled in the system

**When –** the receptionist cancels the appointment

**Then –** the system will provide feedback to user and make that time slot available for another patient.

**US-4:** As a receptionist, I can create a new patient profile, so a new user can book appointments.

Acceptance Criteria 1:

**GIVEN –** a new patient wants to book a appointment

**When –** the receptionist will input patient information in a new patient record

**Then –** the patient can book an appointment.

# Part F - AI Requirements Review: AI ON

Prompt: Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

**Ai requirement review**

<div class="joplin-table-wrapper"><table><tbody><tr><th><p><strong>Requirment</strong></p></th><th><p><strong>Ai suggestion/finding</strong></p></th><th><p><strong>Issue Type</strong></p></th><th><p><strong>Evidence or validation?</strong></p></th></tr><tr><td><p><strong>FR-01</strong></p></td><td><p>The information required for appoints are not specified.</p></td><td><p>Ambiguity / clarification needed. Testability</p></td><td><p>Validation question: What information is required to book an appointment?</p></td></tr><tr><td><p><strong>FR-02</strong></p></td><td><p>It is unclear what appointment can be cancelled.</p></td><td><p>Similar relationship to <strong>FR-10;</strong></p><p>Further clarification needed.</p></td><td><p>Validation question: is a cancellation reason required?</p></td></tr><tr><td><p><strong>FR-03</strong></p></td><td><p>Contact information is vague</p></td><td><p>Ambiguity: missing access Rules</p></td><td><p>Validation question: how does the system ensure that a patient updates only their details?</p></td></tr><tr><td><p><strong>FR-04</strong></p></td><td><p>the Schedule has not been defined.</p></td><td><p>Ambiguity</p></td><td><p>Validation question: does it show cancelled appointments.</p></td></tr><tr><td><p><strong>FR-05</strong></p></td><td><p>The term "patient records" is not defined.</p></td><td><p>Ambiguity</p></td><td><p>Validation question: are practitioners allowed to view all patients or only their own patients?</p></td></tr><tr><td><p><strong>FR-06</strong></p></td><td><p>The phrase "availability schedule" is not defined. FR-06 appears closely related to FR-04 schedule and availability schedule can refer to different things.</p></td><td><p>Ambiguity</p></td><td><p>Validation question: what is the difference between:</p><ul><li>Viewing a practitioner's schedule (FR-04)?</li><li>Viewing practitioner availability (FR-06)?</li></ul></td></tr><tr><td><p><strong>FR-07</strong></p></td><td><p>The term double booking is not defined: without a definition for a double booking testing cannot determine expected behavior.</p></td><td><p>Ambiguity/testability</p></td><td><p>Assumption / Validation question: does double booking mean?</p><ul><li>Same practitioner and same time?</li><li>Same patient and same time?</li><li>Same room and same time?</li></ul></td></tr><tr><td><p><strong>FR-08</strong></p></td><td><p>References a "unique identifier" without any evidence of creating it.</p></td><td><p>Potential consistence concern</p></td><td><p>Validation question: will the database store use unique identifier? Will the reception just use names for searching patients info or other identifiers?</p></td></tr><tr><td><p><strong>FR-09</strong></p></td><td><p>Patent profiles contents are not defined</p></td><td><p>Ambiguity</p></td><td><p>Validation question: What information is required create a profile?</p></td></tr><tr><td><p><strong>FR-10</strong></p></td><td><p>Availability is not defined</p></td><td><p>Testability/Ambiguity</p></td><td><p>Valdiation Question: What availability changes after a cancelled appointment?</p></td></tr></tbody></table></div>

**Cross-Requirement Findings:**

Several business terms are not defined or are ambiguous, thus making testing difficult to test objectively.

# Part G - VERIFY the AI Review

Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence used.

| **AI Suggestion:**                                                                                                                                                     | **Classification:** | **Evidence:**                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **FR-01** Needs the information required for appointments is not specified.                                                                                            | Accepted            | The brief wants the software to manage appointments but does not specify what information is required to create one.                                                                                   |
| **FR-02:** is unclear what appointment can be cancelled.                                                                                                               | Accepted            | The brief mentions a manual cancellation process but does not specify those rules.                                                                                                                     |
| **FR-03:** Contact information is vague                                                                                                                                | Accepted            | Contact information, is not defined by the client yet (i.e. email, phone, mobile, work, secondary email).                                                                                              |
| **FR-04:** The schedule has not been defined yet.                                                                                                                      | Modified            | No mention of a schedule but assumption would be that the practitioner will use the software to all in patients rather than speak with the reception for every appointment to find out who to call in. |
| **FR-05:** The term "patient records" is not defined.                                                                                                                  | accepted            | Brief does not state who can access patient records but needs to be asked to implement a basic system security.                                                                                        |
| **FR-06:** The phrase "availability schedule" is not defined. FR-06 appears closely related to FR-04 schedule and availability schedule can refer to different things. | accepted            | Brief has no mention of schedule but when moving from paper records to software its assumed that scheduling will use the software for calendar purposes.                                               |
| **FR-07:** The term double booking is not defined: without a definition for a double booking testing cannot determine expected behavior.                               | Accepted            | Brief mentions duplicate bookings but does not specify the conflict reasons.                                                                                                                           |
| **FR-08:** References a "unique identifier" without any evidence of creating it.                                                                                       | modified            | The unique identifyer can be used for data storage purposes but the form of a patient search method would be needed by staff as an assumption.                                                         |
| **FR-09:** Patent profiles contents are not defined                                                                                                                    | Accepted            | The brief has no mention of who can book appointments (i.e. members, people with profile, people that have id, walk ins) but does accept appointments.                                                 |
| **FR-10:** Availability is not defined                                                                                                                                 | Modified            | For test purposes opening hours of the clinic is needed.                                                                                                                                               |

# Part H - Finalise SmartCare v0.2

Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user stories, acceptance criteria, assumptions/open questions and selected AI review evidence.

# Reflection

In 150-250 words: What did AI notice that you missed? What did AI invent or overreach on? Which requirement changed after review? Why must requirements have evidence?

**Reflection:**

This activity has helped me understand that being vague can have consequences for testing. The software requirements don't just describe what the system should do but how to define, be clear, be specific so that developers can test issues that can be defined. What I thought was clear for functional requirements, but the ai review has identified many areas of improvement for further clarification such as, availability, patient records and so on.

Using ai requirements as a reviewer has helped me identify missing information that's required for the software to operate. However not all ai requirements are so black and white and can be assumed to function at minimal usage for the clinics functionality. Some suggestions were based on fact from the brief but some are people basic expectation when using software for any clinic appointments

Verification is important because it acts like a feedback loop, clarifications need to be available to make decisions. Without clarification from the client it can quickly get out of scope for the budget and time required.

Human judgement and stakeholder validations are required to test productivity of the system functionality and day to day use.