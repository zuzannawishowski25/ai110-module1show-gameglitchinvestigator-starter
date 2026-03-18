# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran it, it seemed to be fine with showing me "go lower" when i entered the number 3. There were no bugs I could see like missing text or my answer disappearing or anything like that. The number of attempts also was accurate and lowered accordingly to my first guess.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The first two obvious bugs were that when i entered 2, then 1, it kept telling me to "go lower" even though the minimum
is supposed to be 1. Further, when I went on the enter 0 and -1, it kept telling me "go lower" even though those numbers should give an error or some message saying "stay within the 1-100 range" since the guesses were out of range. Those were the most obvious errors and I never got around to being able to correctly guess the number.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot. I was going to use Claude but decided to follow what the assignment stated. I wonder if the results would be different if I used Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI gave 3 suggestions when i first asked it to fix the bugs it saw. The first one was a relatively easy fix, just changing the range to be (low,high) instead of (1,100). I later verified this as being correct by using the test cases that copilot gave me. The problem was that the secret number was being regenerated on every button click because the session state initialization happens on every page reload, but it's only checking if the secret exists at the start. When you click "New Game," it correctly resets, but when you click "Submit Guess," Streamlit reruns the entire script and the random.randint() is called again if the difficulty changes.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I did not get any "wrong" results, although i guess I could have pushed it to do a deeper analyzation of more test cases to find more bugs. It gave me 3 bugs that were "critical" problems and i deicded to only fix 2 of those just for the sake of the assignment. They were easy bugs to fix, so maybe thats why i didnt get many wrong answers from copilot.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
After testing a few cases, I would decide a bug is really fixed. Any possible test cases i could think of like testing below 1 or over 100 and in between were the only values to test so it wasnt too bad. I feel like next time i would ask copilot to make even more test cases for me to really see how fixed the bug is.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I tested 0 again since last time when i tested 0 i got points and the message was "go lower". After trying it again after fixing the code, i finally got the correct points taken off (-5) which is what should have been happening all along. So the fix that copilot gave me turned out to actually work as intended.
- Did AI help you design or understand any tests? How?
I did not ask copilot to help me understadn the tests because I understood them myself. If i were to not not understand something i can imagine copilot would give me actual in-depth explanations and examples. Probably trying out the test cases to try to understand whats going on myself would be best.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
To explain in short, streamlit rereads the script every time the user makes any interaction with the app. Like clicking a button, or searching, whatever it may be, streamlit reruns the entire script top to bottom. So its basically like hitting "run" over and over. For the error i had, the secret number kept resetting instead of being kept the same.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Asking AI to come up with test cases is really helpful to me because it is hard to think outside the box and imagine different scenarios off the top of my head. Having test cases already made and thought of saves time as well. I also think asking AI to explain why it fixed something a certain way is also helpful because not only do i understand "ok this was the error and here is the solution" i get to understand "ok but why was it fixed in this specific way and not another way".
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Maybe next time I would first allow copilot to analyze the code and tell me what it thinks are bugs and then later ask about specific problems that i saw. Its good to get a different perspective first and then give it more detail about what i really want to see. it also helps me think "hmm maybe this issue copilot found relates to the one that i found, let me see if the two are connected" which just helps me think deeper about a bigger issue there may be with the code.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code to me is still okay and good to use for when im working on a small project such as this one. It is very hard to have a lot of files and ask AI "hey tell me what you see is wrong with the logic" because theres just too much going on to be able to ask broadly and then im limited to asking more specific questions only. This is annoying but it also helps me to feel motivated in trying to find out whats wrong by myself.