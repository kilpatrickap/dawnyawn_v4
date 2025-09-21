# dawnyawn/tools/gobuster_tool.py
from tools.base_tool import BaseTool

class GobusterTool(BaseTool):
    @property
    def name(self) -> str:
        return "gobuster_web_scan"

    @property
    def description(self) -> str:
        return (
            "Discovers hidden directories and files on a web server using Gobuster. "
            "The input must be the full base URL of the target, including http/https. "
            "Example: 'http://www.consarltd.com'"
        )

    def _construct_command(self, tool_input: str) -> str:
        # We pre-configure a common wordlist. The AI just needs to provide the URL.
        wordlist = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
        return f"gobuster dir -u {tool_input} -w {wordlist} -t 50 --no-error"