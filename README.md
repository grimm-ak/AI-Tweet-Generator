# 🐦 AI-Powered Tweet Generator

An interactive web application built with Streamlit and the Google Gemini API that generates multiple tweet variations based on a user's topic and desired tone.

**Live App Link:** [https://ai-tweet-generator-2hesapphnm3ptzgfprbdr5l.streamlit.app/](https://ai-tweet-generator-2hesapphnm3ptzgfprbdr5l.streamlit.app/)

---

## Features
- **Dynamic Content Generation:** Users can input any topic to generate relevant social media content.
- **Tone Control:** A dropdown menu allows users to select a specific tone (e.g., Professional, Witty) for the generated tweets.
- **Multiple Options:** The app generates three distinct tweet variations, providing users with choices.
- **Interactive UI:** Built with a clean and simple user interface using Streamlit.

---

## Tech Stack
* **Frontend:** Streamlit
* **Backend & Logic:** Python
* **LLM API:** Google Gemini 1.5 Flash
* **Deployment:** Streamlit Community Cloud

---

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/grimm-ak/AI-Tweet-Generator.git](https://github.com/grimm-ak/AI-Tweet-Generator.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd AI-Tweet-Generator
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your API Key:**
    * Create a folder named `.streamlit`.
    * Inside it, create a file named `secrets.toml`.
    * Add your API key to this file in the following format:
        ```toml
        GOOGLE_API_KEY = "Your-API-Key-Goes-Here"
        ```
5.  **Run the Streamlit app:**
    ```bash
    streamlit run tweet_app.py
    ```
