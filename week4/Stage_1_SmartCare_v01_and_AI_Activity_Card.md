SmartCare v0.1 - Initial Engineering Brief and AI Activity Card

A2 Case Study Stage 1 student resource

# SmartCare scenario

SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments.

# Initial Engineering Brief

## 1\. Problem summary

Currently SmartCare clinic is using spreadsheets and paper records to handle patient records and appointments. The client has claimed to need a software solution to help manage patients, practitioners and appointments. Currently the client has only requested a manageable system to start with that should not be complex. However not all information has been provided at this time and will need follow-up with the client to get a full idea of the system they have in mind such as who can have access, what information will be gathered and stored, and any other important requirements. More key points to discuss will involve on-site storage or cloud solutions.

## 2\. Initial stakeholders

| Stakeholder          | Possible need                                                      |
| -------------------- | ------------------------------------------------------------------ |
| Patient              | Have information stored and used currently and by laws.            |
| System administrator | Maintain the system and fix errors.                                |
| Practitioner         | View patient information and see current calendar of appointments. |
| Receptionist         | Record/edit patient information and manage appointment schedule.   |

## 3\. Initial features

| Feature                   | Confirmed or provisional? | Why?                                                                                                                                    |
| ------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Manage appointments       | Confirmed                 | The client wants to use software instead of paper to manage appointments.                                                               |
| View/edit patient records | Confirmed                 | Reception and the practitioner will need access to modify records.                                                                      |
| Cancel appointment        | Confirmed                 | If a patient can book an appointment, then they need to be able to cancel that appointment themselves or over the phone with reception. |
| Practitioner calendar     | Provisional               | Practitioner may want this, but it was not requested at this point of time.                                                             |

## 4\. Questions for the client

1\. Who can make changes to patient data?

2\. What patient information is required to book an appointment?

3\. If an appointment is cancelled how long until that time slot becomes available?

4\. How will patient data be stored?

5\. Can the patient have more than one appointment scheduled at the same time?

## 5\. What we do not yet know

1\. We don't know how the system will operate features such as the rules for appointment times, availability, and how many practitioner.

2\. We don't know if this software will run locally at reception or on a web-based service.

3\. We do not know who can cancel appointments and rebook.

# AI Activity Card - Ask, Check, Explain

## Before AI

What do I think the code does? What problems can I already identify?

I think the program will create an empty list that stores appointment details such as time and date and with what practitioner with patient name. The book appointment function will check for a value error (empty name input) then add it to the list. Then the appointment function will print those details back to the person as a format string.

Problems I can see are information not being validated, patient booking not being stored, and finally no information of current availability for practitioner's schedule to choose booking times without just guessing.

## AI request

Act as a tutor. Explain this code and identify potential problems. Do not provide a complete replacement. Ask me questions that help me with the reason for the solution.

I asked Copilot to act as a tutor. Explain this code and identify potential problems. Do not provide a replacement. Can you help me identify issues that can be improved and reduce human error?

## Evaluate

| Suggestion                             | Useful | Unclear | Incorrect | Out of scope |
| -------------------------------------- | ------ | ------- | --------- | ------------ |
| Validation of names                    | Yes    |         |           |              |
| Appointment time is just text          | Yes    |         |           |              |
| No duplicate appointment checks        | Yes    |         |           |              |
| No patient schedule conflict detection | Yes    |         |           |              |
| No way to update or cancel             | Yes    |         |           |              |

## Decide

For each significant suggestion: Accept / Modify / Reject / Keep unverified.

| **Suggestion**                         | **Decision** | **Why**                                                                                                   |
| -------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------- |
| Validation of names                    | Accept       | Basic functionality of getting patient names is needed.                                                   |
| Appointment time is just text          | Modify       | Change from string to time format.                                                                        |
| No duplicate appointment checks        | Modify       | Current appointments have duplicate bookings and they want to change that so needs to be added I believe. |
| No patient schedule conflict detection | Modify       | A patient can double book themselves currently.                                                           |
| No way to update or cancel             | Modify       | There needs to be a way to cancel appointments for patients that need to reschedule or cannot make it.    |

## Verify

- Run the code
- Test normal input
- Test unusual input
- Compare with requirements
- Ask tutor/peer
- Check documentation

I tested the code as standard then with normal input, then attempted with blank inputs and it all worked without any errors. I compared to the ai suggestions to add ways to cancel or add but that's currently out of scope until more contact with the client.

## Explain

Can I explain the final code without reading the AI response? What do I still need to understand?

Yes, I can understand the code and explain it to something that has some understanding of code, but it is simple in design so currently its easy to explain but with more functionality and error handling it will be harder.