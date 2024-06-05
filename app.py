import streamlit as st
from langchain.llms  import Ollama


# Assuming Ollama is already set up and running locally on port 11434
# and the "moondream" model is available

def generate_text(prompt):
  ollama = Ollama(base_url="http://localhost:11434", model="aiAlpha")
  return ollama.invoke(prompt)

st.title("Ollama AI Expert")
st.subheader("Using the AI Alpha Model")

prompt_text = st.text_input("Enter your question:")

if st.button("Generate"):
  if prompt_text:
    response = generate_text(prompt_text)
    st.write("**Response:**")
    st.success(response)
  else:
    st.error("Please enter a prompt!")