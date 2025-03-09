import streamlit as st
import random
import string
import re

# Function to evaluate password strength
def password_strength(password):
    score = 0
    feedback = []
    weights = {'length': 1, 'uppercase': 1.5, 'lowercase': 1.0, 'digits': 1.0, 'special': 1.5}

    # Check length
    if len(password) >= 8:
        score += weights['length']
    else:
        feedback.append('Password must be at least 8 characters long.')

    # Check uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += weights['uppercase'] + weights['lowercase']
    else:
        feedback.append('Password must contain both uppercase and lowercase letters.')

    # Check for digits
    if re.search(r'[0-9]', password):
        score += weights['digits']
    else:
        feedback.append('Password must contain at least one digit.')

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += weights['special']
    else:
        feedback.append('Password must contain at least one special character.')

    # Check for common passwords
    common_passwords = ["password123", "123456", "qwerty", "letmein", "123qwe"]
    if password.lower() in common_passwords:
        feedback.append('Password is too weak (common password).')

    # Evaluate password strength
    if score >= 7:
        strength = 'Strong'
        feedback.append('Your password is strong.')
    elif score >= 3:
        strength = 'Moderate'
        feedback.append('Your password is moderate.')
    else:
        strength = 'Weak'
        feedback.append('Your password is weak.')

    return strength, score, feedback

# Function to generate a strong password
def strong_password():
    length = 12  # You can change the length of the password
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Main Streamlit UI
def main():
    st.title('Password Strength Meter and Generator')

    # Input for password
    password = st.text_input("Enter your password:")

    if password:
        # Evaluate password strength
        strength, score, feedback = password_strength(password)

        # Display the results
        st.write(f"Password Strength: {strength}")
        st.write(f"Score: {score}/10")  # Total possible score is 10
        for line in feedback:
            st.write(f"- {line}")
    
   
    # Button to generate a strong password
    if st.button("Generate Strong Password"):
        new_password = strong_password()
        st.write(f"Suggested Strong Password: **{new_password}**")

    # Password requirements section
    st.write("\n### Password Requirements:")
    st.write("- At least 8 characters long")
    st.write("- Contains uppercase and lowercase letters")
    st.write("- Includes at least one digit (0-9)")
    st.write("- Has one special character (!@#$%^&*)")

# Run the Streamlit app
if __name__ == "__main__":
    main()
