# ai-skills

Coding agents have changed how software is built forever. What matters is the **skills** or **context** given to them—this repository captures those skills. It starts with a small subset (recipes for contributing to OSS projects); contribute any AI skill that improves the responses an agent gives back.

**Current skills** focus on OSS contribution: open issues, implement fixes, and land PRs. Each skill gives your agent the workflows, conventions, and checklists for a specific project. Use with Cursor, Claude, ChatGPT, or any agent that can follow structured instructions.

**Currently supported projects:**

| Project | Scope |
|--------|--------|
| **Apache Hadoop** | HADOOP, HDFS, YARN, MAPREDUCE — JIRA, Yetus CI, Maven |
| **Apache Spark** | SPARK (SQL, Core, PySpark, etc.) — JIRA, sbt, GitHub Actions |
| **Apache Airflow** | Core, providers — GitHub issues, prek, breeze, Helm |
| **OpenClaw** | openclaw/openclaw — GitHub issues, pnpm, contributor workflow |

More projects can be added the same way: one skill per project, with issue flow, branch/commit rules, CI, and PR conventions.

---

Structured prompts and recipes for AI-assisted workflows. Organized by **use case** (e.g. open source contribution); vendor-specific overrides can go under `vendor/` later.

## Structure

```
ai-skills/
  README.md
  oss-contribution/           # Open source contribution workflows
    apache/
      hadoop/                 # Apache Hadoop PR (JIRA, Yetus CI, Maven)
      spark/                  # Apache Spark PR (JIRA, sbt, GitHub Actions)
      airflow/                # Apache Airflow PR (GitHub issues, prek, breeze)
    openclaw/                 # OpenClaw PR (GitHub issues, pnpm)
```

## Skills

| Skill | Path | Use when |
|-------|------|----------|
| **Hadoop PR** | [oss-contribution/apache/hadoop/SKILL.md](oss-contribution/apache/hadoop/SKILL.md) | New or existing Hadoop/HDFS/YARN PR; JIRA; Yetus CI; "work on this Hadoop PR" with URL. |
| **Spark PR** | [oss-contribution/apache/spark/SKILL.md](oss-contribution/apache/spark/SKILL.md) | New or existing Spark PR; JIRA (SPARK-xxxxx); sbt tests; "here is my Spark PR URL — take actions". |
| **Airflow PR** | [oss-contribution/apache/airflow/SKILL.md](oss-contribution/apache/airflow/SKILL.md) | New or existing Airflow PR; GitHub issues; prek, breeze, Helm tests. |
| **OpenClaw PR** | [oss-contribution/openclaw/SKILL.md](oss-contribution/openclaw/SKILL.md) | New OpenClaw PR; GitHub issues; pnpm; "follow the openclaw PR recipe". |

## How to use

- **Cursor:** Copy a `SKILL.md` (or its path) into `.cursor/skills/<name>/SKILL.md` so the agent can load it, or reference this repo in your project.
- **Claude / ChatGPT:** Paste the relevant section or link the file when starting a task (e.g. "Follow the Hadoop contribution recipe" and attach the Hadoop SKILL.md).
- **Generic:** Each `SKILL.md` has a **Trigger phrases** section; use those when asking the AI to perform the workflow.

## Repo

- **GitHub:** [deepujain/ai-skills](https://github.com/deepujain/ai-skills)
