import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import requests

# Load environment variables
load_dotenv()

# Retrieve API keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)


# Function to get recipe
def get_recipe_from_ingredients(ingredients, description="", cuisine="", servings=None):
    prompt = f"""
    I have the following ingredients: {ingredients}.
    {f"Here’s a short description or cooking goal: {description}." if description else ""}
    {f"The cuisine should be: {cuisine}." if cuisine else ""}
    {f"I want to make this for {servings} servings." if servings else ""}
    Please suggest a recipe I can make with these ingredients.
    Include a recipe name, a short description, and step-by-step instructions.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text


# Streamlit layout
# Streamlit layout and background
st.set_page_config(page_title="AI Recipe Generator", page_icon="🍳", layout="centered")

# Set background image using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/ingredients-cooking-food-background-with-herbs-vegetables-top-view-white-background_937503-1941.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        font-weight: bold !important;
        font-size:24px !important;
        color: #000000 !important;
    }
    h1, h2, h3, h4, h5, h6 {
        font-weight: bold !important;
        font-size: 24px !important;
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    /* Target form content inside the form block */
    .stForm label, .stForm textarea, .stForm input, .stForm div[data-baseweb="input"] {
        font-weight: bold !important;
        font-size: 18px !important;
        color: #000000 !important;
    }

    /* Also increase label font size if needed */
    .stForm label {
        font-size: 19px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stForm {
        font-weight: bold !important;
    }

    .stForm label, .stForm textarea, .stForm input, .stForm div[data-baseweb="input"] {
        font-weight: bold !important;
        font-size: 22Spx !important;
        color: #000000 !important;
    }
    .stForm h2 {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #333333 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)




st.markdown("<h1 style='text-align: center; color: #FF5722;'>AI Recipe Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #808080;'>Enter your ingredients and get a recipe instantly!</p>", unsafe_allow_html=True)

# Form
with st.form("recipe_form"):
    st.subheader("🥕 Enter Ingredients and Preferences")
    ingredients_input = st.text_area("Ingredients (comma-separated):", placeholder="e.g., tomatoes, eggs, onions, bread")
    description_input = st.text_input("Dish description (optional):", placeholder="e.g., healthy breakfast, quick snack")
    cuisine_input = st.text_input("Cuisine (optional):", placeholder="e.g., Indian, Italian")
    servings_input = st.number_input("Servings (optional):", min_value=1, step=1)
    submit_button = st.form_submit_button("Generate Recipe")

# On submit
if submit_button:
    if ingredients_input.strip():
        try:
            recipe = get_recipe_from_ingredients(ingredients_input, description_input)
            st.markdown("<h3 style='color: #FF5722;'>Here’s a Recipe You Can Try!</h3>", unsafe_allow_html=True)
            st.write(recipe)
        except Exception as e:
            st.error(f"An error occurred while generating the recipe: {e}")
    else:
        st.warning("Please enter some ingredients.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #808080;'>Ai-powered recipe app-MGMCET</p>", unsafe_allow_html=True)