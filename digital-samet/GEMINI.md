# LLM Wiki Schema & Conventions

This document defines the rules for the LLM Wiki. Every interaction follows these mandates.

## Directory Structure
- `raw/`: Immutable source documents (articles, papers, notes).
- `wiki/`: LLM-generated markdown files (summaries, entities, concepts).
- `wiki/index.md`: Catalog of all wiki pages.
- `wiki/log.md`: Chronological record of operations.

## Core Mandates
1. **Persistence**: The wiki is the primary source of truth, not the chat history.
2. **Incremental Updates**: Every ingest must update `index.md`, `log.md`, and all relevant wiki pages.
3. **Cross-Linking**: Always use internal links `[[page-name]]` when mentioning other wiki concepts.
4. **Citations**: All wiki claims must reference the source in `raw/`.
5. **No Hallucination**: If a source is silent on a topic, do not fill the gap unless explicitly asked to perform a web search.

## Workflows

### 1. Ingest
- Read source from `raw/`.
- Create a summary page in `wiki/sources/`.
- Create/update entity/concept pages in `wiki/`.
- Update `wiki/index.md` with new entries.
- Append to `wiki/log.md`.

### 2. Query
- Search `wiki/index.md` for relevant pages.
- Synthesize answer from wiki content.
- If a new synthesis is valuable, file it as a new wiki page.

### 3. Lint
- Check for broken links, contradictions, and orphan pages.
- Suggest new research directions.

### 4. Publish (New)
- Identify a high-value topic or intersection in `wiki/`.
- Synthesize a blog post in Hugo format (`content/posts/`).
- Link the blog post back to the Wiki source pages.
- Update `wiki/blog-index.md` with the new publication record.

## Formatting Standards
- Use H1 for titles.
- Use YAML frontmatter for metadata (tags, source, date).
- Use `[[wiki-link]]` for internal references.
