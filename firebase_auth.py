import os
from dotenv import load_dotenv
import pyrebase
from models import User

# Load environment variables
load_dotenv()

# Firebase Configuration
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def signup_user(email, password):
    """Registers a user with Firebase and saves details in MongoDB."""
    try:
        # Check if the email already exists
        existing_user = None
        try:
            existing_user = auth.sign_in_with_email_and_password(email, password)
        except:
            pass  # Ignore login failure since we're checking existence

        if existing_user:
            return {"error": "Email already exists. Please log in instead."}

        # Proceed with user creation if email is not found
        user = auth.create_user_with_email_and_password(email, password)
        firebase_uid = user['localId']

        # Save user in MongoDB
        new_user = User(uid=firebase_uid, email=email, name=email.split("@")[0])
        new_user.save()

        return {"message": "User created successfully", "uid": firebase_uid}
    except Exception as e:
        return {"error": str(e)}

def login_user(email, password):
    """Authenticates a user with Firebase and returns an auth token."""
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return {"message": "Login successful", "token": user['idToken']}
    except Exception as e:
        error_message = str(e)
        
        # Handle known errors
        if "INVALID_LOGIN_CREDENTIALS" in error_message:
            return {"error": "Invalid email or password. Please check your credentials and try again."}
        elif "EMAIL_NOT_FOUND" in error_message:
            return {"error": "This email is not registered. Please sign up first."}
        elif "TOO_MANY_ATTEMPTS_TRY_LATER" in error_message:
            return {"error": "Too many failed login attempts. Try again later."}
        else:
            return {"error": f"Login failed: {error_message}"}



