Stage 1 Tutorial Activity

\- Why Software Engineering Still Matters

Stage 1 | Introducing Software Technology Case Study with Python and Guided AI use

# Learning goals

- Explain why software engineering is broader than coding.
- Identify stakeholders in a simple software problem.
- Recognise missing requirements.
- Critically evaluate AI-generated feature suggestions.
- Explain why AI output should not automatically be treated as correct.

# Activity 1 - Think-Pair-Share (10 minutes)

If ChatGPT or Copilot can produce a 100-line Python application very quickly, what knowledge does a software engineer still need?

1\. How to interact with customers to get requirements to decide how the software will work and what goals they want to achieve.

2\. A software engineer still needs to think long term such as, maintenance a year from now and what cyber security will be implemented, that brings design implementation into question and all things require a human input at some point so it needs a human thinking when designing important software solutions.

3\. Cost limitations of the customer and scope of current and future business needs. Software would need to work on many OS systems and be updated constantly for security/feature updates.

# Activity 2 - Is This Software Engineering? (10 minutes)

Scenario A: A student writes a 50-line Python calculator.  
Scenario B: A team develops a payroll system used by 5,000 employees.  
Scenario C: An AI assistant generates a simple appointment application from one prompt.

| Scenario | Programming? | Software engineering? | Why?                                                                                                                                                                                    |
| -------- | ------------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A        | Yes          | Maybe                 | A student can learn to create the python calculator for ana assignment or for fun. But the software engineer has no real need for it unless they use it for testing use.                |
| B        | Yes          | Yes                   | For such a large project a team will be need to program the software. Meanwhile the software engineer will need to get the requirements and design and all other aspects of deployment. |
| C        | Yes          | No                    | It may spew out some code but there are bound to be some issues such as requirements not met or extra features not requested.                                                           |

# Activity 3 - SmartCare Problem Analysis (20 minutes)

Client statement: SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The clinic wants new software to improve these processes.

## Task 1 - Identify stakeholders

| **Stakeholder**      | **What do they need?**                                           |
| -------------------- | ---------------------------------------------------------------- |
| Receptionist         | Create new patient profile and manage appointments/cancelations. |
| Patient              | Appointment information and record/update details                |
| Practitioner         | Patient appointment time, and any relevant history records       |
| System administrator | Handle the users and system software.                            |

## Task 2 - Identify current problems

1\. duplicate appointments, leading to confusion and availability

2\. limited status of practitioner's availability, making it hard to plan schedule.

3\. Cancellations are done manually so are prone to mistakes

4\. Record keeping has proven difficult to handle

## Task 3 - Ask client questions

1\. How much information can each stakeholder access

2\. What information of the patient do you require?

3\. Can the patient see different practitioners?

4\. What do you want to happen if they are late for an appointment (some sort of notice or penalty)?

5\. What is the minimum time they can cancel an appointment before they are scheduled?

# Activity 4 - Critique an AI Response (15 minutes)

An AI assistant suggests: appointment management; facial-recognition login; AI diagnosis recommendations; patient search; online payment; practitioner schedule view; insurance processing; automatic treatment-plan generation.

| Suggestion                   | Client evidence?  | In scope?                                          | Decision                                                                  |
| ---------------------------- | ----------------- | -------------------------------------------------- | ------------------------------------------------------------------------- |
| Appointment management       | Yes               | Yes                                                | Accept as a Key feature requested that manages appointments for patients. |
| Facial recognition login     | No                | No<br><br>(Could change depending on current laws) | Reject as the client wants something simple to start with.                |
| AI diagnosis recommendations | No                | No                                                 | Reject as that could lead to liability and life-threatening outcomes.     |
| Patient search               | No                | Yes                                                | Accept practitioner will need to search the patient's history on record.  |
| Online payment               | No                | No<br><br>(possible next iteration)                | Reject for now unless requested                                           |
| Practitioner schedule view   | Indirect/possible | Yes                                                | Accept: to book appointments the system will need availability schedule.  |
| Insurance processing         | No                | NO                                                 | Reject: not currently needed                                              |
| Treatment-plan generation    | No                | NO                                                 | Reject: would making appointments redundant.                              |

# Exit question

Write one activity that a software engineer must perform and that cannot safely be delegated entirely to AI.

Risk management to prevent stolen identity information is a constant battle that requires human thinking to counter.