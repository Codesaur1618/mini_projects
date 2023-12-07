import pyttsx3

def text_to_speech(text, output_file):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties, including the male voice and a stronger rate (adjust as needed)
    engine.setProperty('rate', 150)  # Speed of speech
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 1 for male voice, 0 for female voice

    # Save the speech as a WAV file (can be converted to MP3 if needed)
    engine.save_to_file(text, output_file)

    # Run the engine to generate speech and save it to the specified file
    engine.runAndWait()

    print(f"Text converted to speech and saved as {output_file}")

# Example usage
if __name__ == "__main__":
    text = "Hi i am xyz"
    output_file = "output_male.wav"

    text_to_speech(text, output_file)
