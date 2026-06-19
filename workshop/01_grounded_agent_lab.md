# Lab 1: Build A Grounded Search Agent

## Goal

Get an MCP-compatible assistant using You.com search, then make it show its work with source URLs.

## Setup

Generate a client config:

```bash
mcp-workshop-config --client cursor
```

Set your API key:

```bash
export YDC_API_KEY="your-api-key"
```

## Prompt

```text
Use You.com search to answer: What has changed recently in AI search evaluation?
Give me three claims. Put a source URL next to each claim.
```

## Discussion

- Which sources were useful?
- Did the assistant cite enough evidence?
- Which claim deserves a closer page read before anyone repeats it?
