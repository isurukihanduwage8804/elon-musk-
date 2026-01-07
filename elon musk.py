import streamlit as st
import random

# පූජනීය මතක් කිරීම: ඉසුරු විසින් නිර්මාණය කරන ලදී.

st.set_page_config(page_title="Elon's Mars Mission", layout="centered")

st.title("🚀 Elon's Mars Mission")
st.subheader("Help Elon reach the Red Planet!")

# --- Variable Initialization (මෙතන තමයි ඔයාට වැරදුණු තැන හදලා තියෙන්නේ) ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# --- Game Logic Functions ---
def reset_game():
    st.session_state.score = 0
    st.session_state.game_over = False

# --- UI and Hero Message ---
# ඔයාට කලින් Error එක ආපු තැන (Line 15 ආසන්නයේ)
if st.session_state.score < 300:
    st.info("🛰️ **Mission Control:** Elon, I wish you a safe journey, Hero!")

# සරල ගේම් එකක් වගේ පෙනෙන්නට Button එකක් හදමු
if not st.session_state.game_over:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Boost Rocket"):
            st.session_state.score += 50
    with col2:
        if st.button("☄️ Dodge Asteroid"):
            st.session_state.score += 20
            if random.random() < 0.1: # 10% chance to fail
                st.session_state.game_over = True

    # Progress Bar එකක් පෙන්වමු
    progress = min(st.session_state.score / 1000, 1.0)
    st.progress(progress)
    st.write(f"Distance covered: **{st.session_state.score} km** / 1000 km")

# --- Winning Condition ---
if st.session_state.score >= 1000:
    st.balloons()
    st.success("🎉 **VICTORY!** You have successfully reached Mars.")
    st.markdown("### 🏆 I wish you a safe journey, Hero!")
    if st.button("Play Again"):
        reset_game()
        st.rerun()

# --- Game Over Condition ---
if st.session_state.game_over:
    st.error("💥 Mission Failed! An asteroid hit the Starship.")
    if st.button("Try Again"):
        reset_game()
        st.rerun()

# --- Footer ---
st.write("---")
st.caption("Developed by Isuru | Supporting the mission to Mars")
