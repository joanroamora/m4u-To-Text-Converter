# 🏳️‍🇺🇸   Code Documentation in English

### Description
This Python script converts `.m4a` audio files to `.wav` format and then transcribes the audio content into text using Google Speech Recognition. The transcription process handles long audio files by breaking them into smaller chunks for better accuracy. The transcriptions are saved in text files, and the intermediary `.wav` files are deleted after processing.

## Functions

### `convert_m4a_to_wav(input_path, output_path)`
- **Purpose**: Converts an `.m4a` audio file to `.wav` format.
- **Parameters**:
  - `input_path`: The file path of the input `.m4a` file.
  - `output_path`: The file path where the output `.wav` file will be saved.
- **Returns**: None

### `transcribe_audio(audio_path)`
- **Purpose**: Transcribes the entire content of a `.wav` audio file into text.
- **Parameters**:
  - `audio_path`: The file path of the `.wav` audio file.
- **Returns**: A string containing the transcribed text.

### `transcribe_audio_in_chunks(audio_path)`
- **Purpose**: Transcribes a `.wav` audio file in 30-second chunks to handle longer files.
- **Parameters**:
  - `audio_path`: The file path of the `.wav` audio file.
- **Returns**: A string containing the transcribed text from all chunks combined.

### `main()`
- **Purpose**: Main function that handles the processing of all `.m4a` files in the specified directory.
- **Workflow**:
  1. Convert `.m4a` files to `.wav`.
  2. Transcribe the audio in chunks.
  3. Save the transcription to a text file.
  4. Delete the temporary `.wav` file after processing.

---

# 🏳🇨🇴 Documentación del Código en Español

### Descripción
Este script de Python convierte archivos de audio `.m4a` a formato `.wav` y luego transcribe el contenido del audio en texto usando Google Speech Recognition. El proceso de transcripción maneja archivos de audio largos dividiéndolos en partes más pequeñas para mejorar la precisión. Las transcripciones se guardan en archivos de texto, y los archivos `.wav` intermedios se eliminan después de ser procesados.

## Funciones

### `convert_m4a_to_wav(input_path, output_path)`
- **Propósito**: Convierte un archivo de audio `.m4a` a formato `.wav`.
- **Parámetros**:
  - `input_path`: Ruta del archivo de entrada `.m4a`.
  - `output_path`: Ruta donde se guardará el archivo de salida `.wav`.
- **Retorno**: Ninguno

### `transcribe_audio(audio_path)`
- **Propósito**: Transcribe todo el contenido de un archivo de audio `.wav` en texto.
- **Parámetros**:
  - `audio_path`: Ruta del archivo de audio `.wav`.
- **Retorno**: Una cadena de texto que contiene la transcripción.

### `transcribe_audio_in_chunks(audio_path)`
- **Propósito**: Transcribe un archivo de audio `.wav` en partes de 30 segundos para manejar archivos largos.
- **Parámetros**:
  - `audio_path`: Ruta del archivo de audio `.wav`.
- **Retorno**: Una cadena de texto que contiene la transcripción de todas las partes combinadas.

### `main()`
- **Propósito**: Función principal que gestiona el procesamiento de todos los archivos `.m4a` en el directorio especificado.
- **Flujo de trabajo**:
  1. Convierte archivos `.m4a` a `.wav`.
  2. Transcribe el audio en partes.
  3. Guarda la transcripción en un archivo de texto.
  4. Elimina el archivo `.wav` temporal después de ser procesado.

eso es todo.
