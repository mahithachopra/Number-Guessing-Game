import random
import streamlit as st

# Set the title of the Streamlit app with emoji
st.title("🎉 Guess the Number Game 🎉")

# Add a subtitle and instructions with markdown
st.markdown("""
Welcome to the **Guess the Number** game! 🤔
Try to guess the randomly chosen number within a limited number of attempts. 
Choose your difficulty level, enter your guess, and see if you can win! 🏆
""")

# Set background color using custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to set the difficulty level
def set_difficulty(level):
    if level == 'Easy':
        return random.randint(1, 50), 10
    elif level == 'Medium':
        return random.randint(1, 100), 7
    elif level == 'Hard':
        return random.randint(1, 200), 5

# Initialize session state variables
if 'random_number' not in st.session_state:
    st.session_state.random_number = 0
if 'attempts_left' not in st.session_state:
    st.session_state.attempts_left = 0
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'game_active' not in st.session_state:
    st.session_state.game_active = False

# Difficulty selection
difficulty = st.selectbox("Select Difficulty Level:", ["Easy", "Medium", "Hard"])

# Start new game button
if st.button("🎮 Start New Game"):
    st.session_state.random_number, st.session_state.attempts_left = set_difficulty(difficulty)
    st.session_state.message = ""
    st.session_state.game_active = True
    st.write(f"🌟 Game started! You have {st.session_state.attempts_left} attempts.")

# Player input for guessing the number
if st.session_state.game_active:
    guess = st.number_input("🔢 Enter your guess:", min_value=1, max_value=200, step=1, format="%d")

    # Submit guess button
    if st.button("✅ Submit Guess"):
        if st.session_state.random_number == 0:
            st.session_state.message = "⚠️ Click 'Start New Game' to begin."
        else:
            if guess < st.session_state.random_number:
                st.session_state.message = "📉 Too low! Try again."
            elif guess > st.session_state.random_number:
                st.session_state.message = "📈 Too high! Try again."
            else:
                st.session_state.message = f"🎉 Correct! You've guessed the number {st.session_state.random_number}!"
                st.session_state.game_active = False  # End the game
            st.session_state.attempts_left -= 1

            if st.session_state.attempts_left == 0 and guess != st.session_state.random_number:
                st.session_state.message = f"💔 Game over! The number was {st.session_state.random_number}."
                st.session_state.game_active = False  # End the game

# Display the message and remaining attempts
st.markdown(f"### {st.session_state.message}")
if st.session_state.attempts_left > 0 and st.session_state.game_active:
    st.write(f"🕹️ Attempts remaining: {st.session_state.attempts_left}")
elif not st.session_state.game_active and st.session_state.attempts_left == 0:
    st.markdown("### ⚠️ No attempts left. Click 'Start New Game' to try again!")
