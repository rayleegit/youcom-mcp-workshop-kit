from __future__ import annotations

import argparse
import json

from .configs import build_config


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate You.com MCP workshop configs.")
    parser.add_argument("--client", choices=["claude", "cursor"], required=True)
    parser.add_argument("--api-key-env", default="YDC_API_KEY", help="Environment variable that stores the API key.")
    args = parser.parse_args(argv)

    config = build_config(args.client, args.api_key_env)
    print(json.dumps(config.payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
