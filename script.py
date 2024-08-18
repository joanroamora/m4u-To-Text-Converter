import os
import subprocess
import speech_recognition as sr
from pydub import AudioSegment

def convert_m4a_to_wav(input_path, output_path):
    audio = AudioSegment.from_file(input_path, format='m4a')
    audio.export(output_path, format='wav')

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        # Transcribe audio to text (assuming the language is Spanish)
        text = recognizer.recognize_google(audio_data, language='es-ES', show_all=False)
        return text
    
def transcribe_audio_in_chunks(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_length = source.DURATION  # Get the duration of the audio file
        chunk_duration = 30  # Process 30 seconds at a time
        transcription = ""
        for start in range(0, int(audio_length), chunk_duration):
            end = min(start + chunk_duration, int(audio_length))
            audio_chunk = recognizer.record(source, duration=(end - start))
            try:
                chunk_text = recognizer.recognize_google(audio_chunk, language='es-ES', show_all=False)
                transcription += chunk_text + " "
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                continue
    return transcription

def main():
    audio_dir = './audio'
    transcription_dir = './transcriptions'
    
    if not os.path.exists(transcription_dir):
        os.makedirs(transcription_dir)
    
    for audio_file in os.listdir(audio_dir):
        if audio_file.endswith('.m4a'):
            audio_path = os.path.join(audio_dir, audio_file)
            wav_path = os.path.join(audio_dir, audio_file.replace('.m4a', '.wav'))
            
            # Convert m4a to wav
            convert_m4a_to_wav(audio_path, wav_path)
            
            # Transcribe the audio file in chunks
            transcription = transcribe_audio_in_chunks(wav_path)
            
            # Save transcription to text file
            transcription_file = os.path.join(transcription_dir, audio_file.replace('.m4a', '.txt'))
            with open(transcription_file, 'w') as f:
                f.write(transcription)
            
            # Remove the wav file after processing
            os.remove(wav_path)
        else:
            print(f"Skipping non-m4a file: {audio_file}")

if __name__ == "__main__":
    main()
