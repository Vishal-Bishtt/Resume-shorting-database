import mongoengine as me
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to MongoDB Atlas
mongo_uri = os.getenv("MONGODB_URI")
me.connect(host=mongo_uri)

# User Model
class User(me.Document):
    uid = me.StringField(required=True, unique=True)  # Firebase UID
    email = me.EmailField(required=True, unique=True)
    name = me.StringField(required=True)
    created_at = me.DateTimeField(default=datetime.utcnow)

    meta = {"indexes": ["email"]}

# Resume Model
class Resume(me.Document):
    user = me.ReferenceField(User, required=True)
    skills = me.ListField(me.StringField())  # Extracted skills
    experience = me.StringField()
    education = me.StringField()
    uploaded_at = me.DateTimeField(default=datetime.utcnow)

    meta = {"indexes": ["user"]}

# Interview Session Model
class InterviewSession(me.Document):
    user = me.ReferenceField(User, required=True)
    start_time = me.DateTimeField(default=datetime.utcnow)
    end_time = me.DateTimeField()
    feedback = me.ReferenceField('AIFeedback')

    meta = {"indexes": ["user"]}

# AI Feedback Model
class AIFeedback(me.Document):
    user = me.ReferenceField(User, required=True)
    interview_session = me.ReferenceField(InterviewSession)
    grammar_score = me.FloatField()
    clarity_score = me.FloatField()
    confidence_score = me.FloatField()
    feedback_text = me.StringField()
    created_at = me.DateTimeField(default=datetime.utcnow)

    meta = {"indexes": ["user"]}

