# ai-skills

Structured prompts and recipes for AI-assisted workflows. Use these with Claude, Cursor, ChatGPT, or other coding agents. Organized by **use case** (e.g. open source contribution); vendor-specific overrides can go under `vendor/` later.

## Structure

```
ai-skills/
  README.md
  oss-contribution/           # Open source contribution workflows
    apache/
      hadoop/                 # Apache Hadoop PR (JIRA, Yetus CI, Maven)
      spark/                  # Apache Spark PR (JIRA, sbt, GitHub Actions)
      airflow/                # Apache Airflow PR (GitHub issues, prek, breeze)
```

## Skills

| Skill | Path | Use when |
|-------|------|----------|
| **Hadoop PR** | [oss-contribution/apache/hadoop/SKILL.md](oss-contribution/apache/hadoop/SKILL.md) | New or existing Hadoop/HDFS/YARN PR; JIRA; Yetus CI; "work on this Hadoop PR" with URL. |
| **Spark PR** | [oss-contribution/apache/spark/SKILL.md](oss-contribution/apache/spark/SKILL.md) | New or existing Spark PR; JIRA (SPARK-xxxxx); sbt tests; "here is my Spark PR URL — take actions". |
| **Airflow PR** | [oss-contribution/apache/airflow/SKILL.md](oss-contribution/apache/airflow/SKILL.md) | New or existing Airflow PR; GitHub issues; prek, breeze, Helm tests. |

## How to use

- **Cursor:** Copy a `SKILL.md` (or its path) into `.cursor/skills/<name>/SKILL.md` so the agent can load it, or reference this repo in your project.
- **Claude / ChatGPT:** Paste the relevant section or link the file when starting a task (e.g. "Follow the Hadoop contribution recipe" and attach the Hadoop SKILL.md).
- **Generic:** Each `SKILL.md` has a **Trigger phrases** section; use those when asking the AI to perform the workflow.

## Repo

- **GitHub:** [deepujain/ai-skills](https://github.com/deepujain/ai-skills)
