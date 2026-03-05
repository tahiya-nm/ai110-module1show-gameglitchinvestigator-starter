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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
