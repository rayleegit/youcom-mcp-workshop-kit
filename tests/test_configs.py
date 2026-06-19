import unittest

from mcp_workshop_kit.configs import REMOTE_MCP_URL, build_claude_config, build_config, build_cursor_config


class ConfigTests(unittest.TestCase):
    def test_builds_claude_config(self):
        config = build_claude_config()
        server = config.payload["mcpServers"]["youcom"]

        self.assertEqual(server["command"], "npx")
        self.assertIn("@youdotcom-oss/mcp", server["args"])

    def test_builds_cursor_config(self):
        config = build_cursor_config("CUSTOM_KEY")
        server = config.payload["mcpServers"]["youcom"]

        self.assertEqual(server["url"], REMOTE_MCP_URL)
        self.assertEqual(server["headers"]["Authorization"], "Bearer ${CUSTOM_KEY}")

    def test_rejects_unknown_client(self):
        with self.assertRaises(ValueError):
            build_config("unknown")


if __name__ == "__main__":
    unittest.main()
