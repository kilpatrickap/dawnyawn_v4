# dawnyawn/tools/tool_manager.py
import logging
from typing import Dict, Optional

# --- Import all your tool classes ---
from tools.base_tool import BaseTool
from tools.nmap_tool import NmapTool
from tools.gobuster_tool import GobusterTool


# Add imports for WhatWebTool, SqlmapTool, etc. as you create them

class ToolManager:
    """Manages the registration and execution of all available tools."""

    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}
        # --- Register all your tools here ---
        self._register_tool(NmapTool())
        self._register_tool(GobusterTool())
        # self._register_tool(WhatWebTool())
        # self._register_tool(SqlmapTool())

        # A special tool for when the AI decides the mission is over.
        # It doesn't execute a command, so it doesn't inherit from BaseTool.
        self.finish_mission_tool_name = "finish_mission"
        logging.info("ToolManager initialized with %d tools.", len(self.tools))

    def _register_tool(self, tool_instance: BaseTool):
        """Registers a single tool instance."""
        if tool_instance.name in self.tools:
            raise ValueError(f"Tool with name '{tool_instance.name}' is already registered.")
        self.tools[tool_instance.name] = tool_instance
        logging.info("  - Registered tool: '%s'", tool_instance.name)

    def get_tool(self, tool_name: str) -> Optional[BaseTool]:
        """Retrieves a tool instance by its name."""
        return self.tools.get(tool_name)

    def get_tool_manifest(self) -> str:
        """
        Generates a formatted string of all available tools and their
        descriptions for the AI's system prompt. THIS IS THE KEY.
        """
        manifest = []
        for tool in self.tools.values():
            manifest.append(f'- `{tool.name}`: {tool.description}')

        # Add the special finish_mission tool to the manifest
        manifest.append(
            '- `finish_mission`: Use this tool when all tasks are complete. The '
            'tool_input should be a final, detailed summary of all findings.'
        )
        return "\n".join(manifest)