# 🎵 AI-Powered Hindi Song Recommender & YouTube Player

This Python project uses **Google Gemini AI** to recommend Hindi songs based on your mood or input prompt and plays the result directly on **YouTube** using **Selenium WebDriver**. Perfect for discovering songs that match your vibe—automatically and instantly.

---

## 🚀 Features

- 💡 Recommends Hindi songs based on user mood or input
- 🧠 Uses Google Gemini AI (via `gemini-1.5-flash`) to generate song names
- 🔍 Automates YouTube search using Selenium
- ▶️ Plays the top video match on YouTube
- ⏩ Skips ads when possible (automatically)

---

## 🧠 How It Works

1. **User Input**
   - Accepts a mood or keyword from the user (e.g., "romantic", "study", "monsoon vibes")

2. **Song Generation with Gemini AI**
   - Sends the prompt to Gemini asking for **one** Hindi song that matches the mood
   - Gemini responds with the song name and artist

3. **YouTube Automation**
   - Opens YouTube, searches for the Gemini-recommended song
   - Plays the top result
   - Tries to skip the ad automatically if it appears

---

## 🔧 Requirements

- Python 3.8+
- Google Gemini AI API Key
- Chrome browser & [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed and on PATH
- `.env` file with your API key
- Required Python packages

---

## 🧪 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/hindi-song-recommender.git
   cd hindi-song-recommender
   ```

3. **Set up your `.env` file:**
   Create a `.env` file in the root folder and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```

4. **Make sure ChromeDriver is installed and accessible:**
   - [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)
   - Add it to your system's PATH

5. **Run the project:**
   ```bash
   python main.py
   ```

---

## 📁 Project Structure

```
├── gemini.py         # Handles Gemini AI song recommendations
├── youtube.py        # Automates YouTube search and video playback
├── main.py           # Entry point that integrates Gemini + YouTube
├── .env              # Stores your Google Gemini API key (not included in repo)
```

---

## 📝 Sample Prompt

When asked:

```text
Enter the mood of song or any thing you want to search:
```

You can type:

- "romantic"
- "rainy day"
- "heartbreak"
- "study session"
- "party time"

Gemini will recommend one Hindi song accordingly, and it will be played on YouTube.

---

## 📌 Notes

- Make sure your internet connection is stable (Selenium opens a live browser).
- Gemini AI responses are subject to variation and accuracy.
- Only supports **Hindi songs** in current implementation.
- You can easily extend it to include other languages, more filters, or even Spotify integration.

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Acknowledgements

- [Google Gemini API](https://ai.google.dev/)
- [YouTube](https://www.youtube.com/)
- [Selenium](https://www.selenium.dev/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)

---

