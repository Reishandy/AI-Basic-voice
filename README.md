# Voice Assistant

This is a simple voice assistant script written in Python that utilizes various libraries to perform tasks based on voice commands. The voice assistant responds to voice commands for tasks such as searching the internet, opening YouTube videos, querying Wikipedia, checking internet speed, playing a simple rock-paper-scissors game, and providing information about the current date, time, and day.

## Dependencies

- [pywhatkit](https://github.com/Ankit404butfound/PyWhatKit): A Python library to automate tasks on the web.
- [wikipedia](https://github.com/goldsmith/Wikipedia): A Python library to access and parse data from Wikipedia.
- Other standard Python libraries (`datetime`, `sys`) and modules (`rps`, `search`, `voice`) included in the repository.

## How to Use

1. Install the required dependencies using the following command:
    ```bash
    pip install pywhatkit wikipedia
    ```

2. Run the script using the following command:
    ```bash
    python voice_assistant.py
    ```

3. The voice assistant will greet you and wait for your command. Speak clearly and use one of the supported commands.

## Supported Commands

- **Search**: Perform a Google search.
  ```
  Example: search What is the capital of France?
  ```

- **Open**: Open a YouTube video.
  ```
  Example: open music video
  ```

- **Wiki**: Get a summary from Wikipedia.
  ```
  Example: wiki Artificial Intelligence
  ```

- **Play**: Play a simple rock-paper-scissors game.
  ```
  Example: play rock paper scissors
  ```

- **What**: Ask for the current date, time, or day.
  ```
  Examples:
  - what is the time?
  - what is the date?
  - what day is it?
  ```

- **Check Internet Speed**: Check the internet speed.
  ```
  Example: check internet speed
  ```

- **Goodbye/Exit/Stop**: Exit the program.
  ```
  Examples:
  - goodbye
  - exit
  - stop
  ```

- **Unrecognized Commands**: If the voice assistant doesn't understand the command, it will provide a list of supported commands.

## Notes

- The voice assistant utilizes text-to-speech and speech-to-text capabilities to interact with the user.
- The script continuously runs in a loop, waiting for user commands until explicitly exited.

Feel free to customize and extend the functionality of the voice assistant as needed!
