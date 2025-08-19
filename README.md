

<img width="1000" height="700" alt="Screenshot 2025-08-19 162130" src="https://github.com/user-attachments/assets/3c84d071-403b-4626-885d-522f94c4d6e1" />

<img width="1000" height="700" alt="Screenshot 2025-08-19 162208" src="https://github.com/user-attachments/assets/a1fd0e31-7200-42c5-96f0-af6f11f670e2" />



A lightweight Python script that runs in the background to automatically correct your grammar. It monitors your clipboard, uses Google's advanced AI to improve your text, and seamlessly pastes the correction back for you.

***

## ✨ Features

* **Automatic Correction**: Runs silently on your local machine to watch for any new text you copy.
* **Powered by Gemini AI**: Leverages the power of Google's AI for high-quality, human-sounding corrections.
* **Seamless Workflow**: Simply **copy** your text (`Ctrl+C`), and the script automatically **pastes** (`Ctrl+V`) the corrected version back in its place.
* **Human-Like Tone**: The AI is instructed to not just fix errors, but to improve sentence flow and make the text sound natural.
* **Lightweight**: Uses minimal system resources and requires no complex setup.

***

## ⚙️ How It Works

The script operates on a simple, intuitive loop that makes correcting text feel effortless.

1.  **Select Text**: You highlight any text in any application (a web browser, Notepad, etc.).
2.  **Copy**: You press `Ctrl + C`.
3.  **Detect & Correct**: The script detects the new text, sends it to the Gemini AI for correction, and gets the improved version back.
4.  **Auto-Paste**: The script simulates a `Ctrl + V` keypress, instantly replacing your original text.

***

## 💻 Local Installation & Setup

To use all features of this tool, you must run it on your own computer.

### 1. Prerequisites

* **Python 3.8+**: Ensure Python is installed on your system.
* **Google Gemini API Key**: Get a free API key from **[Google AI Studio](https://aistudio.google.com/app/apikey)**.

### 2. Get the Code

* **For Beginners**: Go to the GitHub repository page, click the green `<> Code` button, and select **Download ZIP**. Unzip the folder.
* **Using Git**: Open your terminal and clone the repository with this command:
    ```bash
    git clone https://github.com/WERwq-oe/Grammar-auto-AI-correct.git
    ```

### 3. Install Dependencies

This project uses a `requirements.txt` file to manage its libraries.

* **Create the File**: Inside your project folder, create a new file named `requirements.txt` and paste the following into it:
    ```
    google-generativeai
    pyperclip
    pynput
    ```
* **Install**: Open your terminal in the project folder and run:
    ```bash
    pip install -r requirements.txt
    ```

### 4. Add Your API Key

* Open the **`main.py`** file.
* Find the line:
    ```python
    API_KEY = "PASTE_YOUR_NEW_API_KEY_HERE"
    ```
* **Replace** the placeholder with your actual Gemini API key, keeping the quotation marks.

> **⚠️ Security Warning**: Do not share this file publicly with your API key inside it. Keep your key safe!

***

## ▶️ Usage

1.  **Run the Script**: Open your terminal, navigate to the project folder, and run:
    ```bash
    python main.py
    ```
2.  **Minimize the Terminal**: The script is now running in the background.
3.  **Correct Your Text**:
    * Select text in any application.
    * Press `Ctrl + C`.
    * The corrected text will instantly be pasted back over your selection.
4.  **Stop the Script**: Go back to the terminal window and press `Ctrl + C`.

***

## 🔧 Troubleshooting

* **`ImportError: No module named ...`**: This means a required library is missing. Make sure you have created the `requirements.txt` file correctly and run `pip install -r requirements.txt`.
* **API Errors**: If you see an error from the Gemini API, double-check that you have pasted your API key correctly and that it is valid.
* **Script doesn't do anything**: Ensure the script is still running in a terminal window.


## 📄 License

This project is licensed under the MIT License.
