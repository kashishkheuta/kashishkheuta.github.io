import streamlit as st
import base64
import time

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Smart Food Recommender", layout="wide")

# ---------------- IMAGE LOAD ----------------
def get_base64(img):
    with open(img, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ---------------- BACKGROUND ----------------
def set_bg(page):

    if page == "welcome":
        img = get_base64("bg1.png")
        opacity = 0.5
    else:
        img = get_base64("bg2.png")
        opacity = 0.7

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
    }}
    .stApp::before {{
        content:"";
        position:fixed;
        width:100%;
        height:100%;
        background: rgba(255,255,255,{opacity});
        z-index:-1;
    }}
    </style>
    """, unsafe_allow_html=True)

# ---------------- STYLE ----------------
st.markdown("""
<style>
.title {
    text-align:center;
    font-size:40px;
    color:#1b5e20;
}
.glass {
    background: rgba(255,255,255,0.9);
    padding:25px;
    border-radius:15px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

page = st.session_state.page
set_bg(page)

# ---------------- 1. WELCOME ----------------
if page == "welcome":

    st.markdown('<div class="title">🍽️ Smart Food Recommender</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.write("✨ Find food that matches your mood")
    st.write("💡 Reduce confusion & save time")
    st.write("🍲 Smart suggestions")

    if st.button("🚀 Start"):
        st.session_state.page = "input"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- 2. INPUT ----------------
elif page == "input":

    st.markdown('<div class="title">📝 Input Form</div>', unsafe_allow_html=True)

    mood = st.selectbox("How are you feeling?", ["Happy 😊","Stressed 😓","Tired 😴"])
    stress = st.slider("Stress Level",0,100,40)
    energy = st.slider("Energy Level",0,100,50)
    budget = st.number_input("Budget ₹",50,1000)
    cuisine = st.selectbox("Cuisine",["Indian","Chinese","Any"])

    if st.button("Next ➡"):
        st.session_state.update({
            "mood": mood,
            "energy": energy,
            "budget": budget
        })
        st.session_state.page = "mood"
        st.rerun()

# ---------------- 3. MOOD ----------------
elif page == "mood":

    st.markdown('<div class="title">📊 Mood Insights</div>', unsafe_allow_html=True)

    mood = st.session_state.mood
    energy = st.session_state.energy

    st.write("Detected Mood:", mood)
    st.progress(energy)

    if energy < 40:
        st.warning("You seem low on energy and slightly stressed today.")

    if st.button("Next ➡"):
        st.session_state.page = "budget"
        st.rerun()

# ---------------- 4. BUDGET ----------------
elif page == "budget":

    st.markdown('<div class="title">💰 Budget Insights</div>', unsafe_allow_html=True)

    budget = st.session_state.budget
    cost = 120
    save = budget - cost

    st.write(f"Your Budget: ₹{budget}")
    st.write(f"Recommended Meal: ₹{cost}")
    st.write(f"You Save: ₹{save}")

    if st.button("Next ➡"):
        st.session_state.page = "food"
        st.rerun()

# ---------------- 5. FOOD DETAILS ----------------
elif page == "food":

    st.markdown('<div class="title">🍲 Food Details</div>', unsafe_allow_html=True)

    st.write("Name: Dal Khichdi")
    st.write("Price: ₹120")
    st.write("Cuisine: Indian")
    st.write("Tags: Light, Comfort")
    st.write("Description: Easy to digest and ideal for low energy.")

    if st.button("Next ➡"):
        st.session_state.page = "profile"
        st.rerun()

# ---------------- 6. PROFILE ----------------
elif page == "profile":

    st.markdown('<div class="title">👤 Profile</div>', unsafe_allow_html=True)

    name = st.text_input("Name")
    pref = st.selectbox("Preferred Cuisine",["Indian","Chinese"])
    diet = st.selectbox("Diet Type",["Veg","Non-Veg"])

    if st.button("Next ➡"):
        st.session_state.name = name
        st.session_state.page = "result"
        st.rerun()

# ---------------- 7. RESULT ----------------
elif page == "result":

    st.markdown('<div class="title">🏆 Final Recommendation</div>', unsafe_allow_html=True)

    mood = st.session_state.mood

    if "Tired" in mood:
        st.success("You seem tired. Try Khichdi or Soup 🍲")
    elif "Stressed" in mood:
        st.success("You seem stressed. Try Tea and Light Food ☕")
    else:
        st.success("You seem happy. Enjoy Pizza or Pasta 🍕")

    if st.button("Next ➡"):
        st.session_state.page = "about"
        st.rerun()

# ---------------- 8. ABOUT ----------------
elif page == "about":

    st.markdown('<div class="title">ℹ️ About Project</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.write("This app recommends food based on your mood and energy level.")
    st.write("It helps reduce decision fatigue and improve eating habits.")

    st.write("### Wellness Tips")
    st.write("😓 If stressed → Drink tea, eat light food")
    st.write("😴 If tired → Choose easy meals")
    st.write("😊 If happy → Try new cuisines")

    if st.button("🏠 Home"):
        st.session_state.page = "welcome"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)