# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The game showed a simple title, a button for developer debug info, then a box to enter your guess and a button below it to submit it. There was another button below it to start a new game. When you submit a guess, it accepts it on the first go, but for each submission after that, you have to click submit twice for it to register. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - The first bug was that the hint was incorrect, it kept telling me to go lower when it should have been saying higher (I saw the real number by expanding the debug info).
  - The second bug was that the game accepted my guess on the first try, but for each subsequent guess, I had to click submit twice for it to register. This was very confusing and made the game frustrating to play. On the first submit click, it would enter my previous guess number into the developer debug info history. On the second click, it registered the actual new guess. 
  - If I guess correctly, the final score that it shows me in the "You won!" message is different from the score that is shown in the developer debug info. The score in the debug info is correct, but the score in the "You won!" message is incorrect.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Claude Code and GitHub Copilot on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - I asked Claude Code to help me refactor the parse_guess and check_guess functions from app.py into logic_utils.py. It successfully refactored the function and I verified that it worked by running the game and testing it to see if the guesses were being parsed correctly and that the hints were being given correctly based on the guess. The game worked as expected after the refactor, so I knew that the AI's suggestion was correct.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - When I asked Claude Code to help me generate a pytest case to specifically test and target the bugs I fixed, it generated a test that was not passing due to an error in the test code itself. The test was supposed to check if the check_guess function was returning the correct hint based on the guess, but it had a syntax error that caused it to fail. I verified that the test was incorrect by looking at the error message and realizing that there was a mistake in the test code, not in the actual game code. I then had to fix the test code manually to get it to run correctly.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I decided that a bug was really fixed by running the game and testing it manually to see if the behavior that was previously buggy was now working as expected. For example, after fixing the hint logic, I ran the game and made guesses that were too high and too low to see if the hints were now correct. After fixing the issue with having to click submit twice, I ran the game and made multiple guesses to see if they were being registered on the first click. I also checked the developer debug info to see if the history of guesses was being updated correctly.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - One test I ran was a manual test where I played the game and made a series of guesses to see if the hints were correct and if the game was registering my guesses on the first click. This test showed me that after fixing the hint logic, the hints were now correct based on whether my guess was too high or too low. It also showed me that after fixing the submit button issue, my guesses were being registered on the first click instead of requiring two clicks. This gave me confidence that the bugs I fixed were actually resolved.
- Did AI help you design or understand any tests? How?
  - Yes, AI helped me design a pytest case to test the check_guess function. I asked Claude Code to generate a test case that would check if the function was returning the correct hint based on the guess. The AI generated a test that included different scenarios for guesses that were too high, too low, and correct. This helped me understand how to structure my tests and what cases to consider when testing the function. However, I had to fix an error in the generated test code to get it to run correctly.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - The secret number kept changing in the original app because it was being generated inside the main body of the Streamlit app, which runs from top to bottom every time there is an interaction (like clicking a button). This means that every time I clicked submit, the app would rerun and generate a new secret number, which is why it seemed like the secret number had commitment issues. The secret number was not being stored in a way that persisted across interactions, so it would reset every time the app reran.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit reruns the entire script from top to bottom every time there is an interaction, such as clicking a button or entering text. This means that any variables defined in the script will be reset to their initial values on each rerun. To keep track of information across these reruns, you have to save variables that you want to persist across interactions in "session states". By using session states, you can ensure that certain values, like the secret number in this game, remain the same even as the app reruns.
- What change did you make that finally gave the game a stable secret number?
  - The change I made was to move the generation of the secret number into the block of code that runs when a new game is started. This way, the secret number is only generated once when the player clicks the "New Game" button, and it is stored in the session state. This ensures that the secret number remains stable and does not change every time there is an interaction with the app.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
- One habit that I want to reuse in future projects is the practice of writing detailed pre and post reflections on my coding and debugging process. This helps me to be more mindful of the decisions I have to make while coding and to learn from the experience. It also allows me to track my progress and identify areas where I can improve in future projects.
- What is one thing you would do differently next time you work with AI on a coding task?
  - One thing I would do differently next time is to be more critical and careful when reviewing AI-generated code, especially when it comes to testing. I would make sure to thoroughly review any test cases generated by AI to ensure that they are correctly structured and free of errors before relying on them to validate my code. This would help me avoid situations where I have to fix errors in the test code itself, which can be time-consuming and confusing.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project made me realize that while AI-generated code can be a helpful starting point, it is not always perfect and may require careful review and debugging. It also highlighted the importance of understanding the underlying logic of the code and being able to identify and fix bugs, rather than just relying on AI to generate code that works perfectly on the first go.
