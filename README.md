# Alchemiq News Intelligence — Claude Code Plugin

AI-curated, publication-ready global news intelligence, available inside Claude Code via the Model Context Protocol.

This plugin connects Claude to the hosted **Alchemiq Desk MCP server** at `mcp.alchemiqai.com`. No local server is started; authentication happens through Alchemiq's secure OAuth flow the first time you use a tool.

## What you get

Five tools exposed to Claude:

| Tool | What it does |
| :--- | :--- |
| `search_news` | Search ranked story clusters across hundreds of global publishers — filter by keyword, category, country, language, sentiment, and time range. |
| `get_story_package` | Drill into a single story cluster — sources, publishers, timeline, articles grouped by language. |
| `generate_brief` | Produce an editor-ready brief summarizing one or more stories. |
| `localize_brief` | Translate a brief into another language, including a specialized 3-step German news-portal pipeline. |
| `conversational_news_query` | Natural-language assistant with multi-turn state — supports follow-ups like *"show more"*, *"tell me about #3"*, *"create a report"*, *"translate to Hebrew"*. |

Coverage spans 50+ categories (Business, Technology, Politics, Health, Entertainment, Sports, Science) across hundreds of publishers worldwide.

## Install

### From the Claude Code community marketplace

```bash
/plugin marketplace add anthropics/claude-plugins-community
/plugin install alchemiq-news-intelligence@claude-community
```

### Direct from this repository

```bash
/plugin marketplace add alchemiqai/desk-mcp
/plugin install alchemiq-news-intelligence
```

After installation, run `/mcp` to complete the Alchemiq sign-in. If you do not yet have an account, create one at [alchemiqai.com](https://alchemiqai.com).

## Example prompts

- *"Find the top tech stories from Germany this week"*
- *"Show more"* → *"Tell me more about number 2"*
- *"Generate a publication-ready brief on the EU AI Act developments from the past 7 days"*
- *"Localize this brief into German news-portal style"*
- *"What's trending in business across the US, UK, and Israel right now?"*

## Authentication & data

- Sign-in is handled by Alchemiq via secure OAuth 2.0 — credentials are never exchanged with Claude.
- An Alchemiq account is required. The plugin sends only your queries and the tokens needed to scope the session to your account.

## Legal

- **License**: Proprietary. See [LICENSE](./LICENSE).
- **Privacy policy**: <https://alchemiq.ai/privacy>
- **Terms of service**: <https://alchemiq.ai/terms>

## Support

- Website: <https://alchemiqai.com>
- Issues: open one in this repository
- Email: liad@alchemiq.ai
