import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Tweet Generator",
    page_icon="🐦",
    layout="wide"
)

# --- GOOGLE GEMINI API SETUP ---
# Reads the API key from the secrets.toml file
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("API key not found. Please create a .streamlit/secrets.toml file and add your GOOGLE_API_KEY.")
    st.stop()

# --- MODEL AND HELPER FUNCTION ---
model = genai.GenerativeModel('gemini-1.5-flash')

def get_completion(prompt):
    """Generates content from the Gemini-Pro model."""
    response = model.generate_content(prompt)
    return response.text

# --- USER INTERFACE ---
st.title("🐦 AI-Powered Tweet Generator")
st.write("Generate engaging tweets for your social media. Just provide a topic and a tone!")

with st.form("tweet_form"):
    topic = st.text_input("**Topic:**", placeholder="e.g., The future of machine learning")
    tone = st.selectbox("**Select a Tone:**", ["Professional", "Witty", "Inspirational", "Casual"])
    
    submitted = st.form_submit_button("Generate Tweets")

if submitted:
    if not topic:
        st.warning("Please enter a topic to generate tweets.")
    else:
        with st.spinner("Generating 3 tweet variations..."):
            prompt = f"""
            Act as an expert social media manager. Your goal is to create 3 engaging tweets.

            Topic: "{topic}"
            Tone: "{tone}"

            For each tweet, you must:
            - Keep it under 280 characters.
            - Include 2-3 relevant hashtags.
            - Follow the specified tone.

            Generate the 3 tweets separated by "---".
            """
            
            response_text = get_completion(prompt)
            tweets = response_text.split("---")

            st.subheader("Generated Tweets:")
            for i, tweet in enumerate(tweets):
                if tweet.strip():
                    st.text_area(f"Option {i+1}", tweet.strip(), height=150)