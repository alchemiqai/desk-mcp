# Alchemiq News Intelligence

AI-curated, publication-ready global news intelligence — available inside **ChatGPT**, **Claude**, and **Gemini**.

This repository ships installable manifests for the **Alchemiq Desk MCP server** hosted at `https://mcp.alchemiqai.com/mcp`. The server speaks the [Model Context Protocol](https://modelcontextprotocol.io/), so it works with any MCP-compatible AI assistant. Authentication is handled by Alchemiq's secure OAuth flow on first use.

## What you get

Five tools exposed to your assistant:

| Tool | What it does |
| :--- | :--- |
| `search_news` | Search ranked story clusters across hundreds of global publishers — filter by keyword, category, country, language, sentiment, and time range. |
| `get_story_package` | Drill into a single story cluster — sources, publishers, timeline, articles grouped by language. |
| `generate_brief` | Produce an editor-ready brief summarizing one or more stories. |
| `localize_brief` | Translate a brief into another language, including a specialized 3-step German news-portal pipeline. |
| `conversational_news_query` | Natural-language assistant with multi-turn state — supports follow-ups like *"show more"*, *"tell me about #3"*, *"create a report"*, *"translate to Hebrew"*. |

Coverage spans 50+ categories (Business, Technology, Politics, Health, Entertainment, Sports, Science) across hundreds of publishers worldwide.

## Install

### ChatGPT

Add the **Alchemiq News Intelligence** app from the ChatGPT Apps directory, or connect the MCP server directly:

```
https://mcp.alchemiqai.com/mcp
```

Settings → Connectors → Add MCP server → paste the URL above and complete OAuth.

### Claude (Claude Code & Claude apps)

In Claude Code, this repository is a complete plugin. Install via the community marketplace:

```bash
/plugin marketplace add anthropics/claude-plugins-community
/plugin install alchemiq-news-intelligence@claude-community
```

Or directly from this repo:

```bash
/plugin marketplace add alchemiqai/desk-mcp
/plugin install alchemiq-news-intelligence
```

In Claude apps (web/desktop), add the connector at `https://mcp.alchemiqai.com/mcp` from Settings → Connectors.

### Gemini (Gemini CLI)

```bash
gemini extensions install https://github.com/alchemiqai/desk-mcp
```

The extension manifest in this repo registers the MCP server automatically. Run `/extensions list` inside Gemini to verify.

### Any other MCP client

Point your client at:

```
https://mcp.alchemiqai.com/mcp
```

Transport: HTTP (streamable). Authentication: OAuth 2.0 via Frontegg — your client will be redirected on first tool call.

## Example prompts

- *"Find the top tech stories from Germany this week"*
- *"Show more"* → *"Tell me more about number 2"*
- *"Generate a publication-ready brief on the EU AI Act developments from the past 7 days"*
- *"Localize this brief into German news-portal style"*
- *"What's trending in business across the US, UK, and Israel right now?"*

## Authentication & data

- Sign-in is handled by Alchemiq via secure OAuth 2.0 — credentials are never exchanged with the AI assistant.
- An Alchemiq account is required. Create one at [alchemiqai.com](https://alchemiqai.com).
- The extension transmits only your tool calls and your session token. No background data collection.

## Legal

- **License**: Proprietary. See [LICENSE](./LICENSE).
- **Privacy policy**: <https://alchemiq.ai/privacy>
- **Terms of service**: <https://alchemiq.ai/terms>

## Support

- Website: <https://alchemiqai.com>
- Issues: open one in this repository
- Email: liad@alchemiq.ai
