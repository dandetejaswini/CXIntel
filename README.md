# CXIntel – Customer Experience Intelligence Platform  

## Project Summary  
CXIntel is a Salesforce-based **Customer Experience Intelligence Platform** that centralizes customer feedback, applies **AI-powered sentiment analysis**, and provides **real-time insights** to agents, managers, and executives.  

The application replaces fragmented spreadsheets and manual processes with a **secure, automated, and intelligent platform** that improves feedback handling, reduces churn, and enhances overall customer experience.  

---

## Features & Technologies  

| Feature Implemented       | Technology Used |
|----------------------------|-----------------|
| **Data Model**             | Custom Object: `CustomerFeedback__c`, Fields: `Feedback_Text__c`, `Sentiment__c`, `Sentiment_Score__c`, `Processed__c` |
| **Security & Sharing**     | Experience Cloud Guest Access, Profiles, Permission Sets |
| **Business Logic**         | Validation Rules, Salesforce Flow (case creation), Apex Classes |
| **Backend Development**    | Apex Triggers (auto case creation), Python Scripts (TextBlob/Hugging Face NLP) |
| **Frontend Development**   | Lightning Web Components (Registration, Login, Feedback Form, Dashboard UI) |
| **Integration**            | Salesforce REST API, Python (`simple-salesforce`), Hugging Face/TextBlob |
| **Deployment**             | GitHub Actions CI/CD, Salesforce DX, VS Code |
| **Analytics**              | Custom Reports & Dashboards (Sentiment Trends, Feedback Volume, Agent Performance) |
| **AI Extensions**          | Einstein Bots (auto-replies), Google Speech-to-Text API |

---

## The Development Journey  

### Phase 1 & 2: Foundation & Configuration  
- Defined requirements for **customer feedback lifecycle**.  
- Set up Salesforce **Experience Cloud site** for external customers.  
- Configured **secure sharing settings** for guest and registered users.  

### Phase 3: Data Modeling  
- Built `CustomerFeedback__c` object.  
- Added fields for **feedback text, sentiment, score, and processed flag**.  
- Established lookup relationships for agent assignment.  

### Phase 4: Process Automation  
- Validation Rule → Feedback text must be provided.  
- Record-Triggered Flow → Create Case automatically if sentiment is **Negative**.  

### Phase 5: Python AI Integration  
- Developed Python script with **TextBlob/Hugging Face** for sentiment analysis.  
- Used `simple-salesforce` for CRUD operations on Salesforce records.  
- Automated updates for sentiment score & classification.  
- Scheduled with **Windows Task Scheduler / GitHub Actions**.  

### Phase 6: User Authentication (Registration & Login)  
- Custom **Registration & Login LWCs** integrated with `Registration__c` object.  
- Implemented **password hashing (SHA-256)** for secure storage.  
- Enforced password rules: 10+ chars, uppercase, number, special character.  

### Phase 7: User Interface Development  
- Built **Feedback Portal** with Lightning Web Components.  
- Added Registration ↔ Login redirects.  
- Created UI for feedback submission, FAQs, and discussion forums.  

### Phase 8: Advanced AI Extensions  
- Integrated **Einstein Bots** for automated responses.  
- Experimented with **GPT-powered suggestions** for agent replies.  

### Phase 9: Reporting & Dashboards  
- Dashboards created for:  
  - Sentiment distribution (Positive, Neutral, Negative).  
  - Feedback volume trends.  
  - Agent resolution performance.  
- Reports for executives to monitor **CX health** and prevent churn.  

### Phase 10: Final Delivery & Demo  
- Full demo flow:  
  1. Customer registers → logs in → submits feedback.  
  2. Python script analyzes feedback → updates Salesforce.  
  3. Negative feedback → auto case creation for agent.  
  4. Dashboard updates in real-time.  
- Demonstrated **business impact**: faster resolutions, AI-driven insights, improved customer satisfaction.  

---

## Expected Outcome  
- **Prevent Missed Feedback:** Automated processing and sentiment analysis.  
- **Streamline Operations:** Centralized customer feedback system.  
- **Enhance Compliance & Security:** Encrypted authentication & secure guest access.  
- **AI-Powered Insights:** Predict churn, identify customer pain points, improve service quality.  

---

## Tech Stack  
- **Salesforce** (Experience Cloud, Apex, LWC, Flows, Reports & Dashboards)  
- **Python** (TextBlob, Hugging Face Transformers, simple-salesforce)  
- **Deployment Tools:** GitHub Actions, VS Code, Salesforce DX  
- **AI Extensions:** Einstein Bots, Google Speech-to-Text API  

---

## 📌 Author  
👤 **Tejaswini Dande**  
Intern @ LG India Pvt Ltd | Salesforce & Python Developer | AI-ML Enthusiast  
