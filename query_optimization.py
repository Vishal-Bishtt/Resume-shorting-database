from models import User, Resume, InterviewSession, AIFeedback

def get_top_users():
    """Retrieve users with the most interview sessions using aggregation."""
    pipeline = [
        {"$lookup": {"from": "interviewsession", "localField": "_id", "foreignField": "user", "as": "sessions"}},
        {"$project": {"name": 1, "email": 1, "session_count": {"$size": "$sessions"}}},
        {"$sort": {"session_count": -1}},
        {"$limit": 5}
    ]
    return list(User.objects.aggregate(*pipeline))

def get_user_feedback(uid):
    """Retrieve all feedback for a given user."""
    return AIFeedback.objects(user=uid)

