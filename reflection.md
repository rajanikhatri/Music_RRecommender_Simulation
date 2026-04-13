# Reflection

## Biggest Learning Moment

The biggest thing I learned was that a recommender does not need super complicated math to feel useful. A few clear rules for genre, mood, energy, and tempo were enough to make results that mostly made sense, and that helped me understand how recommendation logic works step by step.

## How AI Tools Helped

AI tools like Copilot and Codex helped me move faster when I was planning the structure, checking the scoring idea, and cleaning up the writing. They were most helpful when I had a rough idea and needed help turning it into something clearer and easier to read.

## Where AI Suggestions Needed Double-Checking

I still had to double-check AI suggestions against the actual CSV headers, the starter tests, and the assignment directions. Some suggestions sounded good at first, but I had to make sure they actually matched the real data and did not drift away from the simple design I wanted.

## What Was Surprising

What surprised me most was how much the weights changed the ranking. A bonus like `+2.0` for genre match can move a song to the top very quickly, even if another song is closer in energy or tempo. That made me realize how much the designer's choices shape the final recommendations.

## What I Would Improve Next

If I kept working on this, I would add a bigger dataset, let the user choose more than one genre or mood, and try to balance similarity with variety a little better. I would also like to compare this simple content-based system with a recommender that uses listening history.

## Evaluation of Results

The Chill Lofi profile seems the most accurate because the recommended songs all match a calm, low-energy style, which feels very consistent with what a user would expect. The system does a good job capturing that type of mood and energy.

One surprising result is Gym Hero appearing in the Deep Intense Rock profile. While it makes sense mathematically because it matches energy and tempo, it is still a pop song, so a human might not expect it to rank that high for a rock-based preference.

The scoring weights seem reasonable overall. Giving genre the highest weight helps the recommendations feel more natural, while using closeness for energy and tempo allows the system to match different types of preferences instead of always favoring higher values.

This shows that even a simple recommender can feel realistic. Using just a few features like genre, mood, energy, and tempo can produce meaningful results, although it still cannot fully capture human taste in every case.
