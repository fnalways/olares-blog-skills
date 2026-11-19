# Writing and editing

## Find the reason to keep reading

Identify a specific question, change, or finding worth reading about. The opening may begin with a release theme, an existing difficulty, a new capability, or a measured result. Let the content decide. Do not spend the opening on generic industry trends, vague aspirations, or an announcement of what the article will cover. Not every article needs to lead with a benefit before explaining the mechanism.

Technical posts default to readers willing to experiment who know what GPUs and memory are, but may not understand model architectures or inference engines. Follow an existing audience definition when provided. Explain an unfamiliar term's role naturally when introducing it, then use its abbreviation.

Match evidence and length to the article type. Product announcements explain capabilities and value. Tutorials center on a task the reader can complete. Conceptual articles answer the reader's questions. Event reports describe what happened. Reviews explain observed results and tradeoffs. Do not turn every Olares post into a hardware benchmark or a complete product introduction.

Do not insert a fixed “What is Olares?” section at the beginning. Enter the article's subject directly. For readers new to Olares, add a necessary sentence or link in context rather than restoring the old product boilerplate. Follow [Release posts](release-blog.md) for version announcements.

For example, the Flash-Next article's hook was the gap between a large model and consumer hardware resources. Installing it with one instruction describes the agent's workflow and cannot be attributed to the model or inference engine. Other articles need their own focus rather than copying this parameter-count hook.

## Structure and rhythm

- Let each paragraph advance one idea while providing enough explanation. Do not split the whole article into slogans or impose a word limit.
- Order information according to what readers need to understand the subject. Select among problems, explanations, scenarios, results, and practical entry points. Do not impose a result → mechanism → how-to sequence.
- Connect sections through questions still to be answered. After explaining mechanisms and resource use, readers may want to understand the experience. Two H3 subsections for speed and agent tasks under one experience section can be more coherent than an abrupt standalone speed-test section.
- H2s should express the section's specific subject or point. Avoid bare report labels such as “Performance,” “Features,” or “Test results,” without making every heading a suspense device.
- Vary sentence length. An important result may stand alone. Rhythm comes from advancing the information, not repeatedly adding exclamation marks, rhetorical questions, or “But here's the thing.”
- End by returning to what the article established and offering a natural next step. Mention follow-up work briefly when useful. Future commitments must stay within user-provided or public information.

## This user's blog preferences

These preferences come from explicit feedback in this workflow. Follow different instructions for the current task when given.

- Do not use semicolons in English or Chinese prose. Code syntax and quotations requiring exact reproduction are exceptions.
- Do not use middle dots as separators in titles, labels, or sentences.
- Prefer direct affirmative statements. Remove empty defensive phrasing and repetitive “not X, but Y” constructions. Retain limitations that change the conclusion or the reader's actions.
- Do not announce appeal with “exciting,” “powerful,” or “game-changing.” Show the actual scale, waiting time, completed work, or capability the reader gains.
- Omit internal metrics that readers do not need, such as agent step counts, state enums, or unexplained token quotas. Remove claims such as “Responses completed within the limit” when they have no practical meaning.
- Accessibility should not mean a lack of substance. Explain mechanisms, important tradeoffs, or why a result matters.

## Write a review, not a test report

Keep full methodology in the evidence file. Retain enough conditions in the article to make the results understandable. A useful order is the real task, what completed, how long it took, and what that means. Tables suit parallel comparisons, while prose should explain meaningful differences.

Distinguish total from active parameters, original precision from the quantized package, weight size from runtime memory, reserved from actual resources, and generation speed from total agent task time. Do not equate model output speed with task completion speed.

For one or a few runs, put natural qualifiers next to the result, such as “In this run” or “On our setup.” Do not extend these into universal rankings or repeat broad disclaimers in every paragraph. When conditions differ, preserve useful observations and explain the relevant limitation near the comparison. Do not combine numbers from different devices or tasks merely to make the result look better.

Be specific about caching: model loading/warm-up, prompt/KV cache, agent session history, and working-directory drafts or build artifacts are different. Restarting a model does not prove the working directory was empty. Treat possible reuse as something to investigate, not an invented causal explanation. Reruns depend on task authorization. Describe only what the evidence establishes.

Connect resource figures to practical choices. Lower memory requirements may leave room for other apps. Claims about simultaneous generation on one GPU, switching without waiting, or no performance impact require corresponding evidence. If the experience involved sequential tasks, describe the agent task followed by creative work without claiming parallel execution.

## Tutorials and genuinely necessary procedures

This section applies only to tutorials, requested getting-started instructions, or passages readers actually need to follow. Release feature descriptions do not each need an app entry point, button path, or procedure. A link to the relevant guide is usually sufficient. Keep a useful one-sentence entry point or short command without automatically expanding it into a tutorial.

When sequential actions are necessary, introduce them naturally and use an ordered list. Let the introduction cover the entry point or preparation and the steps cover actions, without repetition.

- Begin with verbs such as “Open,” “Select,” “Click,” or “Wait for,” retaining exact UI labels.
- Do not give simple steps extra subheadings. Place explanations and screenshots inside the relevant step and preserve continuous numbering.
- A simple install button and total preparation time are different. For large models, verify weight, engine, and auxiliary-file downloads and initialization, and explain when the app is ready. Mention components such as MTP only when the app actually uses them.
- Do not guess roles, administrator requirements, or button labels. Check the current product or official instructions.
- Prefer current Olares Router documentation for model connections. The user has identified an older connection guide for retirement, so verify it and its replacement before reuse.

## Editing order

Check whether the article's claim and hook agree, then address structure, transitions, headings, and explanation, and finally sentences and punctuation. Each iteration should target the feedback while preserving approved parts.

Verify facts that affect the conclusion and keep detailed checks in internal notes. Evidence in the article should support the story, not turn every internal check into a disclaimer. Use nonpublic device test material only when the user has provided or authorized it for the article. Remove credentials, personal identifiers, and unrelated internal information.
