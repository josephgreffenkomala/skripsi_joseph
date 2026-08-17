---
name: skill-creator
description: Create, evaluate, optimize, and package skills. Use when users want to create a skill, revise an existing skill, run skill evals, compare with-skill vs baseline behavior, optimize a skill description, or package a .skill file.
---

# Skill Creator

Create and improve skills through an evaluation loop. This skill owns the mechanics: drafting from intent, running with-skill/baseline evals, collecting human feedback, optimizing descriptions, and packaging.

For skill-quality theory, use `../writing-great-skills/SKILL.md` as the canonical reference. Do not duplicate its vocabulary here; apply it when judging invocation, context load, information hierarchy, progressive disclosure, completion criteria, duplication, sediment, sprawl, and no-ops.

## Decide the branch

Pick the branch that matches the user's request:

1. **Create a new skill** — capture intent, draft the skill, then evaluate it.
2. **Improve an existing skill** — snapshot the current skill, revise it, then compare old vs new.
3. **Evaluate a skill** — run with-skill and baseline test prompts, grade outputs, and show the user a review UI.
4. **Optimize invocation** — run trigger evals against the skill description.
5. **Package a skill** — build the `.skill` artifact.

Completion criterion: you can name the branch, the skill path, and the next concrete artifact to produce.

## Branch 1 — Create or revise a skill

### 1. Capture intent

Extract what you can from the current conversation before interviewing. Ask only for missing decisions:

- What should this skill help the agent do?
- When should it trigger?
- What output should the user see?
- Is success objectively checkable, or mainly qualitative?
- Which files, tools, scripts, or external systems does it depend on?

For an existing skill, preserve the directory name and `name` frontmatter unless the user explicitly asks to rename it.

Completion criterion: the intended behavior, trigger conditions, output shape, and evaluation approach are explicit enough to draft or edit `SKILL.md`.

### 2. Apply the writing-great-skills review

Read `../writing-great-skills/SKILL.md` and, when needed, `../writing-great-skills/GLOSSARY.md`.

Use that vocabulary to decide:

- whether the skill should be model-invoked or user-invoked
- whether its description earns its context load
- which material belongs in `SKILL.md` versus disclosed reference files
- which steps need sharper completion criteria
- what duplication, sediment, sprawl, and no-ops to remove

Completion criterion: the draft has a clear invocation decision, a protected information hierarchy, and no obvious duplicated theory.

### 3. Write or edit the skill

Use this structure unless the task calls for something simpler:

```text
skill-name/
├── SKILL.md
├── references/   # disclosed reference, loaded only when needed
├── scripts/      # deterministic/repetitive operations
└── assets/       # templates or static files used by outputs
```

Keep `SKILL.md` focused on the steps every run needs. Move branch-specific reference, examples, schemas, and long command cookbooks behind explicit context pointers.

Completion criterion: the skill is runnable by an agent from `SKILL.md`, and any deferred material has a clear pointer explaining when to read it.

## Branch 2 — Build eval prompts

Create 2–3 realistic prompts first; expand later if the skill proves valuable. Ask the user to review them before running expensive evals.

Save prompts to `evals/evals.json` near the skill or in the evaluation workspace:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 0,
      "prompt": "User's realistic task prompt",
      "expected_output": "What good behavior looks like",
      "files": []
    }
  ]
}
```

Read `references/schemas.md` for the full schema when adding assertions or producing benchmark artifacts.

Completion criterion: each eval prompt is realistic, tied to a behavior the skill should change, and approved by the user or clearly marked as agent-proposed.

## Branch 3 — Run and review evals

Put results in `<skill-name>-workspace/` as a sibling to the skill directory. Organize by iteration:

```text
<skill-name>-workspace/
└── iteration-1/
    └── eval-<name>/
        ├── with_skill/outputs/
        └── without_skill-or-old_skill/outputs/
```

### 1. Spawn with-skill and baseline runs together

For each eval, launch both runs in the same turn when subagents are available:

- **New skill baseline:** same prompt without the skill.
- **Existing skill baseline:** snapshot the old skill before editing, then run against the snapshot.

Each run should save the user-visible outputs to its run directory.

Write `eval_metadata.json` in each eval directory:

```json
{
  "eval_id": 0,
  "eval_name": "descriptive-name",
  "prompt": "The prompt used for this eval",
  "assertions": []
}
```

Completion criterion: every eval has both a with-skill output and the right baseline output saved on disk.

### 2. Draft assertions while runs execute

Use assertions only where behavior is objectively checkable. For subjective outputs, rely on qualitative review instead of forcing weak metrics.

Good assertions are descriptive and independently verifiable. If an assertion can be checked by a script, write the script instead of eyeballing it.

Completion criterion: each eval has either useful assertions or an explicit note that it needs human qualitative review.

### 3. Capture timing data immediately

When subagent notifications include token and duration data, save it immediately to `timing.json` in the relevant run directory:

```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

Completion criterion: available timing data has been persisted before it disappears from the conversation.

### 4. Grade and aggregate

For each run, grade assertions into `grading.json`. The viewer expects each expectation to use exactly these fields:

```json
{
  "text": "Assertion text",
  "passed": true,
  "evidence": "Evidence for the verdict"
}
```

Read these helper instructions only when needed:

- `agents/grader.md` — grading assertions
- `agents/analyzer.md` — analyzing benchmark results
- `agents/comparator.md` — blind A/B comparisons

Aggregate the iteration:

```bash
python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
```

Completion criterion: the iteration has `grading.json` where applicable plus `benchmark.json` and `benchmark.md`.

### 5. Generate the review UI

Use the bundled viewer; do not write a custom review page.

```bash
nohup python <skill-creator-path>/eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name "my-skill" \
  --benchmark <workspace>/iteration-N/benchmark.json \
  > /dev/null 2>&1 &
VIEWER_PID=$!
```

For headless environments, write a static HTML file:

```bash
python <skill-creator-path>/eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name "my-skill" \
  --benchmark <workspace>/iteration-N/benchmark.json \
  --static <workspace>/iteration-N/review.html
```

For iteration 2+, pass `--previous-workspace <workspace>/iteration-<N-1>`.

Completion criterion: the user has a review UI or static HTML artifact that shows qualitative outputs and benchmark data.

### 6. Iterate from feedback

When the user is done, read `feedback.json`. Empty feedback means the output was acceptable. Focus revisions on specific complaints and on benchmark failures that actually discriminate between versions.

Kill the viewer server if one was started:

```bash
kill $VIEWER_PID 2>/dev/null
```

Then revise the skill, run a new iteration, and compare against the previous iteration or original snapshot.

Completion criterion: either the user is satisfied, feedback is empty, or another concrete revision is identified.

## Branch 4 — Optimize the description

Run this after the skill behavior is good. Description optimization is about invocation accuracy, not fixing a bad skill body.

### 1. Generate trigger eval queries

Create about 20 realistic queries:

- 8–10 should trigger
- 8–10 should not trigger
- include near misses and competing-skill cases
- avoid trivial unrelated negatives

Save them as JSON:

```json
[
  {"query": "realistic user prompt", "should_trigger": true},
  {"query": "near miss prompt", "should_trigger": false}
]
```

Completion criterion: the eval set tests the real boundary of when the skill should fire.

### 2. Let the user review the trigger set

Use `assets/eval_review.html`:

1. Replace `__EVAL_DATA_PLACEHOLDER__` with the JSON array.
2. Replace `__SKILL_NAME_PLACEHOLDER__` with the skill name.
3. Replace `__SKILL_DESCRIPTION_PLACEHOLDER__` with the current description.
4. Write the result to `/tmp/eval_review_<skill-name>.html` and open it if possible.
5. If the browser downloads `eval_set.json`, use the newest copy from `~/Downloads`.

Completion criterion: the trigger eval set is user-approved or clearly marked as agent-proposed.

### 3. Run the optimization loop

```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id-powering-this-session> \
  --max-iterations 5 \
  --verbose
```

Use the model ID powering the current session so results match the user's environment. Periodically report iteration scores.

Completion criterion: the loop returns a best description chosen by held-out test score, not just train score.

### 4. Apply the result

Update the skill frontmatter with the best description. Show the user before/after and the score change.

Completion criterion: the skill's description is updated and the invocation trade-off is explicit.

## Branch 5 — Package the skill

If `present_files` exists, package and present the artifact. Otherwise, still create the package and tell the user the path.

```bash
python -m scripts.package_skill <path/to/skill-folder>
```

When updating an installed or read-only skill, copy it to a writable temp directory first, preserve the original name, edit there, and package from the copy.

Completion criterion: the user has the path to the generated `.skill` file.

## Environment adaptations

### Claude.ai-style environments

If there are no subagents, run test prompts yourself one at a time after reading the skill. Skip baseline benchmarking unless the environment supports it. Present outputs directly in the conversation or as files on disk.

### Headless/Cowork-style environments

Use `--static` for the review UI. The user's browser may download `feedback.json`; ask for or locate that file before iterating. Description optimization can still run if the required CLI and model access are available.

## Final checklist

Before calling the work done:

- [ ] `writing-great-skills` was applied to the skill design.
- [ ] The invocation decision is explicit.
- [ ] Eval prompts exist or the user declined evals.
- [ ] With-skill and baseline outputs were compared where practical.
- [ ] Human feedback was requested for qualitative outputs.
- [ ] Description optimization was offered after behavior stabilized.
- [ ] The package path was provided if packaging was requested.
