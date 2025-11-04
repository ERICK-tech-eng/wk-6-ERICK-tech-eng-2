CleanCity Test Plan
Project Name: CleanCity - Waste Pickup Scheduler
Document ID: CleanCity-TEST PLAN
Version: 1.0
Date: 11/04/2025
Prepared by: Erick Omondi, Henok Girma, Lydia Awuor
Introduction
This Test Plan describes the testing approach for the CleanCity Waste Pickup Scheduler web application. The goal is to verify that the system functions as expected and meets user and business requirements. This web app is designed for waste pickup requests, dashboard management, feedback submission, awareness information, and admin panel operations.

---

1. Objectives and Tasks
   Objectives:
   • Verify the required functionalities work
   • Identify and fix defects early
   • Validate performance and usability
   • Confirm security features prevent unauthorized access
   • Ensure cross-browser and cross-platform compatibility
   • Verify implementation of data persistence and access control mechanisms
   • Provide thorough coverage using automated and manual tests with traceability to FRS
   Tasks:
   • Requirement review and clarification
   • Test case design and review
   • Environment set-up
   • Test execution (manual + automation)
   • Defect logging and reporting
   • Regression testing
   • Test closure and documentation

---

2. Scope
   In-scope:
   • User Registration/login: Email verification, password validation, login/logout, forgot password
   • Waste pickup scheduling & management
   • Dashboard analytics & gamification features
   • Content management: Blogs, awareness section
   • Community features & admin functions
   • UI/UX responsiveness & accessibility
   • Data validation & localStorage handling
   • Performance & Load Responsiveness: Response time under normal and peak load
   Out of Scope:
   • Integration with third-party logistics (beyond API connectivity)
   • Penetration Testing: Outside current scope but recommended post-deployment
   • Backend/Database validation
   • Payment processing (not applicable)

---

3. Test Items
   • Authentication System
   • Waste Management
   • Dashboard & Analytics
   • Content Management
   • Community Features
   • User Interface
   • Administrative Functions
   • Data & Security
   • Performance & Compatibility
   • Error Handling
   • Notifications

---

4. Features to be Tested
   Feature Description
   Authentication System Registration, Login, Password change, Logout, Role-based access enforcement
   Waste Management Pickup scheduling flow and input validations, User’s pickup request history, Pickup request statuses and updates
   Dashboard & Analytics Personalized user dashboard rendering, Environmental impact metrics calculations, leaderboards, analytics graphs, and trends, Export functionality, Badging system and gamification features
   Content Management Blog creation & interaction, eco tips rotation & display, Awareness Section, Quizzes: Scoring, Answer Feedback, Infographics & Actionable links, Community Feed Features
   Community Features User Profile Management, Profile picture upload and display, Social Interactions (like & commenting), Deletion & Saving
   User Interface Responsive Design Check, Accessibility compliance, navigations, search, breadcrumbs
   Administrative Functions _Backend System_ Pickup request management, user management, content moderation (deleting post/flagging)
   Data & Security Localstorage handling, input validation
   Performance & Compatibility Browser compatibility, Load Times
   Error Handling Form validation, Network error recovery, Error message display

---

5. Features Not to be Tested
   • Live Support
   • Third-party Integration
   • Penetration Testing
   • Backend validation

---

6. Entry and Exit Criteria
   Entry Criteria:
   • Instructors’ signs user stories
   • Ready Test environment
   • Creation of test data (Instructor)
   • Test Cases reviewed
   Exit Criteria:
   • All high and critical defects are fixed and verified
   • 100% FR coverage
   • 90% test case pass rate
   • Regression testing completed
   • Test summary report approved

---

7. Test Strategy
   • Functional Testing: User workflows, verify each functional requirement in the FRS
   • Unit Testing: Component-level testing for individual functions (handled by QAs using Jest)
   • Smoke Testing: Initial build verification across major flows
   • Regression Testing: Ensure new changes don’t break existing features (in case of new development changes)
   • Usability Testing: Validate navigation, accessibility (WCAG2.1 AA), keyboard navigability, validate screen reader, buttons, forms
   • UI Testing: Layout, Responsiveness on different devices/resolutions
   • Regression Testing: After each new feature
   • Integration Testing: Integration of various features or modules
   • Performance Testing: Page load times, interaction delays
   • Security Testing: localStorage exposure, role restrictions
   • Cross-Browser Testing: Validate behavior on Chrome, Safari, Edge, Firefox, Mobile Devices

---

8. Test Deliverables
   • Test Plan Document
   • Test cases and Test Scripts
   • Defect Reports (with priority, severity)
   • Weekly Status Reports
   • Test Summary Report
   • Requirement Traceability Matrix (RTM)
   • Final Test Sign-off

---

9. Testing Tools
   Category Tool
   Test Management Jira
   Automation Selenium, PyTest
   Unit Testing Jest
   Performance JMeter
   Bug Tracking Jira/GitHub issues
   Communication Email, WhatsApp, Google Meet, Mobile Calls
   Documentation Markdown in GitHub, Word Doc (PDF Format), Video, ReadMe
   Accessibility Checks Lighthouse, ScreenReader, Narrator
   Browser Testing BrowserStack, Manual Testing

---

10. Environmental Needs
    • Frontend App: Hosted on Netlify
    • Hardware: MacBook Pro, iPhone, Samsung, Windows
    • Software: Safari, Chrome, Edge, Firefox, VS Code
    • Test Data: Provided by instructors
    • Storage: Browser localStorage (manually cleared per test cycle)
    • Test Environment: User Acceptance Testing (UAT) environment, Netlify, localhost 3000

---

12. Defect Lifecycle
    • Open → Logged by QA with screenshot, logs, screen recording
    • Triage → Assigned severity and owner
    • In Progress → Developer starts fix
    • Ready for Retest → QA verifies fix
    • Closed → Passed in retest, marked resolved
    • Reopen → If issue persists

---
