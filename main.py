from firebase_auth import signup_user, login_user

# Test User Signup
response = signup_user("max134543@sam.com", "Test@1#234")
print(response)

# Test User Login
response = login_user("max134543@sam.com", "Test@1#234")
print(response)
