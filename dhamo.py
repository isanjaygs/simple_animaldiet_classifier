import streamlit as st

def classify_animal(plant, meat, dead, host, decaying):
    if host == 'y':
        return "Parasite"
    elif decaying == 'y':
        return "Decomposer"
    elif dead == 'y':
        return "Scavenger"
    elif plant == 'y' and meat == 'n':
        return "Herbivore"
    elif plant == 'n' and meat == 'y':
        return "Carnivore"
    elif plant == 'y' and meat == 'y':
        return "Omnivore"
    else:
        return "Unknown or Special Diet"

st.title("🐾 Animal Diet Classifier")

st.subheader("Answer the following questions:")

plant = st.radio("Eats plants?", ("Yes", "No"))
meat = st.radio("Eats meat?", ("Yes", "No"))
dead = st.radio("Eats dead animals?", ("Yes", "No"))
host = st.radio("Feeds on a host without killing it?", ("Yes", "No"))
decaying = st.radio("Feeds on decaying matter?", ("Yes", "No"))

if st.button("Classify"):
    # Convert button values to 'y' or 'n'
    plant_val = 'y' if plant == "Yes" else 'n'
    meat_val = 'y' if meat == "Yes" else 'n'
    dead_val = 'y' if dead == "Yes" else 'n'
    host_val = 'y' if host == "Yes" else 'n'
    decaying_val = 'y' if decaying == "Yes" else 'n'

    result = classify_animal(plant_val, meat_val, dead_val, host_val, decaying_val)
    st.success(f"Classification: {result}")
