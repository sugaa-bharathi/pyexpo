import streamlit as st
import random

# Set page title
st.title("Guess the Number Game!")

# Select a random number between 1 and 10
number = random.randint(1, 10)

# Ask the user to input their guess
user_guess = st.number_input('Guess a number between 1 and 10:', min_value=1, max_value=10, step=1)

# Button to submit the guess
if st.button('Submit'):
    if user_guess == number:
        st.success("Congratulations! You guessed the right number.")
    else:
        st.error(f"Oops! The correct number was {number}. Try again!")
