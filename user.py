import random
import streamlit as st

# Set up the game
st.title("Guess the Number Game!")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Initialize or reset the game
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0

# Input from the user
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")
guess_button = st.button("Submit Guess")

# Game logic
if guess_button:
    st.session_state.attempts += 1
    if guess < st.session_state.target_number:
        st.write("Too low! Try again.")
    elif guess > st.session_state.target_number:
        st.write("Too high! Try again.")
    else:
        st.write(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts.")
        reset_button = st.button("Play Again")
        if reset_button:
            st.session_state.target_number = random.randint(1, 100)
            st.session_state.attempts = 0