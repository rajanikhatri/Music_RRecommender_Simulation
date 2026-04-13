# Reflection

## What I Learned

One of the biggest things I learned from this project is that a recommender does not need very complicated math to feel useful. Using simple features like genre, mood, energy, and tempo was enough to create recommendations that often felt meaningful and believable. Building it step by step also helped me understand how a system can turn user preferences into scores and then into ranked results.

## Use of AI Tools

I used AI tools like Copilot and Codex to help me think through the structure of the project, generate ideas for the scoring logic, and clean up parts of the code and writing. They helped me move faster, especially when I needed a starting point or wanted to compare different ways to organize the project. At the same time, I still had to review everything carefully, check it against the CSV data and assignment requirements, and make sure I was not trusting the output blindly.

## Evaluation of Results

The Chill Lofi profile seems the most accurate because the recommended songs all match a calm, low-energy style, which feels very consistent with what a user would expect. The system does a good job capturing that type of mood and energy.

One surprising result is Gym Hero appearing in the Deep Intense Rock profile. While it makes sense mathematically because it matches energy and tempo, it is still a pop song, so a human might not expect it to rank that high for a rock-based preference.

The scoring weights seem reasonable overall. Giving genre the highest weight helps the recommendations feel more natural, while using closeness for energy and tempo allows the system to match different types of preferences instead of always favoring higher values.

This shows that even a simple recommender can feel realistic. Using just a few features like genre, mood, energy, and tempo can produce meaningful results, although it still cannot fully capture human taste in every case.

## Experiment and Observations

I also tried a small scoring experiment by reducing the genre weight and increasing the importance of energy. More specifically, genre match was lowered and energy closeness was made stronger, while mood and tempo stayed the same. This changed the rankings in a noticeable way because songs with the wrong genre could move higher if their energy and tempo were very close to the target.

For example, non-matching genre songs started ranking higher in some profiles, which made the system feel a little less intuitive in those cases. At the same time, the top songs for each profile still stayed mostly consistent when they matched several features at once, so the system did not completely break. That experiment showed me how sensitive the results are to the scoring weights.

## Final Thoughts

I think the biggest strength of this system is that it is simple, understandable, and still works reasonably well. It is easy to explain why a song ranked highly, which makes it good for learning. At the same time, the dataset is small, the results are sensitive to the scoring weights, and the system is still much simpler than the kind of recommender used in real apps.
