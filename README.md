# Resume-shorting-database
 Key Components & Their Purpose
1️ Firebase Authentication (firebase_auth.py)

    Handles user sign-up and login with Firebase.
    Stores new users in MongoDB after sign-up.
    Validates login credentials and returns a Firebase token.
    Prevents duplicate sign-ups by checking if an email is already registered.
    Handles authentication errors such as incorrect passwords or unregistered emails.

2️ MongoDB Models (models.py)

Defines the database schema using mongoengine. Models include:

    User: Stores Firebase UID, email, and name.
    Resume: Stores user-uploaded resumes with skills, experience, and education.
    InterviewSession: Tracks interview start and end times, links feedback.
    AIFeedback: Stores AI-generated feedback on grammar, clarity, and confidence.

 Uses MongoDB indexes for faster queries!
3️ API Testing (main.py)

    Creates a test user (signup_user()).
    Logs in the test user (login_user()).
    Prints results to verify authentication.

4️ Query Optimization (query_optimization.py)

Contains optimized database queries:

    get_top_users() → Retrieves users with the most interview sessions.
    get_user_feedback(uid) → Fetches all feedback for a given user.

 Uses aggregation and indexing for efficient queries!
5️ Database Backup & Restore (backup.py)

    Backs up MongoDB data using mongodump.
    Restores data using mongorestore.
    Loads MongoDB URI securely from .env
