import streamlit as st
import re

def check_password_strength(password):
    feedback = []
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        feedback.insert(0, "✅ Strong Password!")
    elif score == 3:
        feedback.insert(0, "⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.insert(0, "❌ Weak Password - Improve it using the suggestions below.")
    
    return feedback


# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    results = check_password_strength(password)
    for line in results:
        st.write(line)
