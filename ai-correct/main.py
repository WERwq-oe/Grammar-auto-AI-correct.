import pyperclip
import time
import google.generativeai as genai
import os
from pynput.keyboard import Controller as KeyboardController, Key

# --- Configuration ---
# ⚠️ WARNING: Your API key is placed directly in the code.
API_KEY = "Your_API_key"

# --- Initialization ---
keyboard = KeyboardController()

# --- Gemini API Function ---
def get_humanized_correction(text_to_correct):
    """
    Sends text to Gemini with instructions to correct it while making it sound
    natural and human-written, focusing on grammar and paragraph structure.
    """
    if not text_to_correct or len(text_to_correct) < 2:
        return None
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        prompt = (
            "You are an expert English editor. Your task is to revise the following text. "
            "Focus on correcting all grammatical errors, improving sentence structure, and ensuring the paragraph flows logically and naturally. "
            "The final text should sound like it was written by a person, not an AI. "
            "Do not change the original meaning. Only provide the final, corrected text.\n\n"
            f"ORIGINAL TEXT:\n\"\"\"\n{text_to_correct}\n\"\"\"\n\n"
            "CORRECTED TEXT:"
        )
        
        response = model.generate_content(prompt)
        corrected_text = response.text.strip()

        if corrected_text.lower() != text_to_correct.lower():
            return corrected_text
        else:
            return None
            
    except Exception as e:
        print(f"❌ Error communicating with Gemini API: {e}")
        return None

# --- Main Clipboard Monitoring Loop ---
def main():
    print("✅ Fully Automatic Corrector is running...")
    print("   Select and copy text (Ctrl+C) to correct and paste it automatically.")
    print("   Press Ctrl+C in this terminal to stop the script.")
    recent_clipboard_content = ""
    
    while True:
        try:
            current_clipboard_content = pyperclip.paste()
            
            # Check if the clipboard has new, different content
            if current_clipboard_content and current_clipboard_content != recent_clipboard_content:
                print(f"\n📋 Detected: \"{current_clipboard_content[:60]}...\"")
                # Mark this content as "seen" to avoid re-correcting it
                recent_clipboard_content = current_clipboard_content
                
                corrected_text = get_humanized_correction(current_clipboard_content)
                
                if corrected_text:
                    print(f"✨ Pasting: \"{corrected_text[:60]}...\"")
                    # Put the corrected text on the clipboard
                    pyperclip.copy(corrected_text)
                    # Update recent content to the corrected version to prevent loops
                    recent_clipboard_content = corrected_text
                    
                    # Automatically paste the correction
                    time.sleep(0.1) # A brief pause
                    with keyboard.pressed(Key.ctrl):
                        keyboard.press('v')
                        keyboard.release('v')
                else:
                    print("✅ No correction was needed.")
            
            # Wait a moment before checking the clipboard again
            time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n🛑 Script stopped by user. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)

# --- Main Execution ---
if __name__ == "__main__":
    if "PASTE_YOUR_NEW_API_KEY_HERE" in API_KEY:
        print("🚨 ERROR: Please paste your new API key into the script on line 10.")
    else:
        main()