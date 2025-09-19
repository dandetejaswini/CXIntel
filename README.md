# CXIntel - Customer Experience Intelligence Platform  

## Project Overview  
**Industry:** Customer Experience / CRM + AI  
**Project Type:** B2B Salesforce + AI Integration  
**Target Users:** Businesses, Customer Support Teams, CX Managers  

The **CXIntel platform** is built to transform how organizations capture and analyze customer feedback.  
It combines **Salesforce Experience Cloud** for customer interaction, **secure authentication & registration flows**, and **Python-powered AI models** for real-time sentiment analysis.  

---

## Problem Statement  
Modern organizations face critical challenges in managing customer experience:  
- Feedback is collected but rarely analyzed in real-time.  
- Lack of secure and user-friendly customer portals.  
- Limited visibility into customer satisfaction trends.  
- Manual, error-prone feedback tracking processes.  
- No AI-driven insights for proactive customer engagement.  

**Solution Goal:** Build an integrated **CX Intelligence system** to collect structured feedback, analyze sentiment with AI, and surface insights directly inside Salesforce for agents.  

---

## Core Features  

### Registration & Login  
- Custom **LWC-based Registration & Login pages**.  
- **Password security with hashing** & validation rules.  
- Guest → Authenticated **user flow in Experience Cloud**.  

### Feedback Collection  
- Customer feedback portal built with **LWC in Experience Builder**.  
- Feedback stored in Salesforce **CustomerFeedback__c** object.  
- Email confirmation & thank-you automation using Salesforce Flows.  

### Sentiment Analysis (Python Integration)  
- Python + **TextBlob / Transformers** for polarity & classification.  
- Automated update of **Sentiment__c** and **Sentiment_Score__c** fields.  
- AI classifies feedback as **Positive, Negative, or Neutral**.  

### Dashboards & Reporting  
- Salesforce dashboards for **feedback trends, CSAT metrics**.  
- Agent console showing real-time customer sentiment.  
- Alerts for **Negative Feedback** → routed to service agents.  

---

## Expected Outcomes  
The CXIntel platform will:  
-  **Improve Customer Insights** – AI-driven sentiment detection.  
-  **Streamline Feedback Loops** – Faster response to complaints.  
-  **Secure Authentication** – Prevents unauthorized access.  
-  **Data-Driven Decisions** – Real-time dashboards & reports.  
-  **Unified Portal** – One-stop for feedback, support, and engagement.  

---

##  Tech Stack  
- **Salesforce Experience Cloud** – Customer portal  
- **Lightning Web Components (LWC)** – Custom UI for login/registration/feedback  
- **Apex Controllers** – Business logic & database interaction  
- **Salesforce Flows** – Process automation  
- **Python (TextBlob / Transformers)** – Sentiment analysis  
- **FastAPI + Docker** – For model serving (optional deployment)  
- **SQL** – Data storage / reporting integration  
- **REST APIs** – Python ↔ Salesforce integration  

---

