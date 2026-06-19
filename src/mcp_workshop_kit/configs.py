from __future__ import annotations

from dataclasses import dataclass


REMOTE_MCP_URL = "https://api.you.com/mcp"
NPM_PACKAGE = "@youdotcom-oss/mcp"


@dataclass(frozen=True)
class ClientConfig:
    client: str
    payload: dict


def build_claude_config(api_key_env: str = "YDC_API_KEY") -> ClientConfig:
    return ClientConfig(
        client="claude",
        payload={
            "mcpServers": {
                "youcom": {
                    "command": "npx",
                    "args": ["-y", NPM_PACKAGE],
                    "env": {
                        "YDC_API_KEY": f"${{{api_key_env}}}",
                    },
                }
            }
        },
    )


def build_cursor_config(api_key_env: str = "YDC_API_KEY") -> ClientConfig:
    return ClientConfig(
        client="cursor",
        payload={
            "mcpServers": {
                "youcom": {
                    "url": REMOTE_MCP_URL,
                    "headers": {
                        "Authorization": f"Bearer ${{{api_key_env}}}",
                    },
                }
            }
        },
    )


def build_config(client: str, api_key_env: str = "YDC_API_KEY") -> ClientConfig:
    normalized = client.lower().strip()
    if normalized == "claude":
        return build_claude_config(api_key_env)
    if normalized == "cursor":
        return build_cursor_config(api_key_env)
    raise ValueError(f"Unsupported client: {client}. Choose claude or cursor.")
