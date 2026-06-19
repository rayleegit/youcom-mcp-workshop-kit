# You.com MCP Workshop Kit

A hands-on kit for teaching developers how to connect AI assistants to You.com's MCP server.

I made this as the kind of repo I would want before running a live workshop: a tiny config generator, copyable examples, and labs that move from setup to a real grounded-agent workflow.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Generate a Claude Desktop config that uses the local You.com MCP package:

```bash
mcp-workshop-config --client claude
```

Generate a Cursor remote MCP config:

```bash
mcp-workshop-config --client cursor --api-key-env YDC_API_KEY
```

## What It Covers

- Why MCP is useful for AI tool workflows
- How to wire up You.com tools in common clients
- How to teach grounding without turning the workshop into a lecture
- How to explain API keys and config files without losing the room

## Repository Map

```text
src/mcp_workshop_kit/configs.py       Config builders
src/mcp_workshop_kit/cli.py           CLI entrypoint
examples/                            Ready-to-copy config examples
workshop/                            Facilitation-ready labs
tests/                               Unit tests
```

## Suggested Demo Flow

1. Generate the client config.
2. Ask the assistant to search for a recent technical topic.
3. Ask for source URLs next to the claims.
4. Pull page contents for one source that matters.
5. Use the research flow for a deeper brief.

## License

MIT
