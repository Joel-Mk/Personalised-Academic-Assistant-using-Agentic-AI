import streamlit as st
import uuid

from agent import run_agent
from db import init_db, save_interaction, get_past_interactions

# ---------------------------
# Initialize database
# ---------------------------
init_db()

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("📘 Personalised Academic Assistant")

# Create / retrieve session ID
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

session_id = st.session_state["session_id"]

# User input
user_input = st.text_input("What do you want to study or improve?")

# ---------------------------
# Run agent
# ---------------------------
if st.button("Run Agent"):
    if user_input:
        action, output = run_agent(user_input)

        st.subheader(f"Agent chose action: {action}")
        st.write(output)

        # Save interaction to SQLite
        save_interaction(
            session_id=session_id,
            user_input=user_input,
            action=action,
            output=output
        )

        st.success("Action completed and saved.")
    else:
        st.warning("Please enter a study goal.")

# ---------------------------
# History section
# ---------------------------
st.divider()
st.subheader("s Recent activity")

history = get_past_interactions(session_id)

if history:
    for user_input, action, timestamp in history:
        st.markdown(
            f"""
            **{action}**  
            *{user_input}*  
            <small>{timestamp}</small>
            """,
            unsafe_allow_html=True
        )
else:
    st.write("No past activity yet.")
