#!/usr/bin/env python3
"""
Connective CRM MCP Server

Exposes the Connective CRM SDK as MCP tools that can be called by
Claude Code or other MCP clients.

Tools provided:
- get_selector: Get selector info for a field
- validate_dropdown: Check if value is valid
- fuzzy_match: Smart value matching
- get_workflow: Retrieve validated workflow (10 workflows available)
- search_elements: Search for elements
- get_all_options: List all dropdown options

Available Workflows (10 total):
- login_to_crm (NEW: Unified login with 4 modes - existing client, dashboard action, opportunity, dashboard only)
- add_note, upload_file, complete_questionnaire (original 3)
- add_liability, add_asset_other, add_living_expense, add_other_income (recordings batch 1)
- add_real_estate (Assets - Real Estate with address autocomplete/manual entry)
- borrowing_capacity (Complete borrowing capacity calculation with 2 applicants, income, expenses, assets)
"""

import sys
import json
import logging
from pathlib import Path
from typing import Any, Sequence

# Add parent directory to path to import SDK
sys.path.insert(0, str(Path(__file__).parent.parent))

from sdk import CRMReference


# MCP Protocol utilities
def read_message() -> dict:
    """Read a JSON-RPC message from stdin"""
    line = sys.stdin.readline()
    if not line:
        return None
    return json.loads(line)


def write_message(msg: dict):
    """Write a JSON-RPC message to stdout"""
    json.dump(msg, sys.stdout)
    sys.stdout.write('\n')
    sys.stdout.flush()


def error_response(request_id: Any, code: int, message: str) -> dict:
    """Create an error response"""
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {
            "code": code,
            "message": message
        }
    }


def success_response(request_id: Any, result: Any) -> dict:
    """Create a success response"""
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": result
    }


class ConnectiveCRMServer:
    """MCP Server for Connective CRM SDK"""

    def __init__(self):
        """Initialize server and load CRM reference"""
        self.crm = CRMReference()

        # Tool definitions
        self.tools = [
            {
                "name": "get_selector",
                "description": "Get CSS selector and metadata for a Connective CRM field. Returns element type, primary selector, fallback selectors, and dropdown options if applicable.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "field_name": {
                            "type": "string",
                            "description": "Name of the field (e.g., 'lender', 'propertyType', 'agent')"
                        }
                    },
                    "required": ["field_name"]
                }
            },
            {
                "name": "validate_dropdown",
                "description": "Check if a value is valid for a Connective CRM dropdown field. Returns true/false.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "description": "Name of the dropdown field"
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to validate"
                        }
                    },
                    "required": ["field", "value"]
                }
            },
            {
                "name": "fuzzy_match",
                "description": "Smart matching for dropdown values. Handles abbreviations (CBA → Commonwealth Bank), typos, and partial matches. Returns best match with confidence score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "description": "Name of the dropdown field"
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to match (can be abbreviation or partial)"
                        }
                    },
                    "required": ["field", "value"]
                }
            },
            {
                "name": "get_workflow",
                "description": "Get validated step-by-step workflow for CRM tasks. Returns detailed steps with selectors, actions, and timing. Available workflows: login_to_crm (NEW: unified login with 4 modes), add_note, upload_file, complete_questionnaire, add_liability, add_asset_other, add_living_expense, add_other_income, add_real_estate, borrowing_capacity. All workflows include critical timing and selector stability info.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "workflow_name": {
                            "type": "string",
                            "description": "Name of workflow. Options: login_to_crm, add_note, upload_file, complete_questionnaire, add_liability, add_asset_other, add_living_expense, add_other_income, add_real_estate, borrowing_capacity"
                        }
                    },
                    "required": ["workflow_name"]
                }
            },
            {
                "name": "search_elements",
                "description": "Search for elements across all sections by name, label, selector, or section. Returns matching elements with full details.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search term"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "get_all_options",
                "description": "Get complete list of valid options for a dropdown field. Useful for generating dropdowns or validating data.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "description": "Name of the dropdown field"
                        }
                    },
                    "required": ["field"]
                }
            },
            {
                "name": "validate_and_correct",
                "description": "Validate a value and provide auto-correction if needed. Returns whether valid, corrected value, confidence, and alternatives.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "description": "Name of the dropdown field"
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to validate and correct"
                        }
                    },
                    "required": ["field", "value"]
                }
            }
        ]

    def handle_initialize(self, params: dict) -> dict:
        """Handle initialize request"""
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "connective-crm-server",
                "version": "1.0.0"
            }
        }

    def handle_tools_list(self, params: dict) -> dict:
        """Handle tools/list request"""
        return {
            "tools": self.tools
        }

    def handle_tools_call(self, params: dict) -> dict:
        """Handle tools/call request"""
        tool_name = params.get("name")
        arguments = params.get("arguments", {})

        try:
            if tool_name == "get_selector":
                element = self.crm.get_selector(arguments["field_name"])
                if element:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps(element.to_dict(), indent=2)
                            }
                        ]
                    }
                else:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": f"Element '{arguments['field_name']}' not found"
                            }
                        ],
                        "isError": True
                    }

            elif tool_name == "validate_dropdown":
                is_valid = self.crm.validate_dropdown(
                    arguments["field"],
                    arguments["value"]
                )
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "valid": is_valid,
                                "field": arguments["field"],
                                "value": arguments["value"]
                            }, indent=2)
                        }
                    ]
                }

            elif tool_name == "fuzzy_match":
                match = self.crm.fuzzy_match(
                    arguments["field"],
                    arguments["value"]
                )
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(match.to_dict(), indent=2)
                        }
                    ]
                }

            elif tool_name == "get_workflow":
                workflow = self.crm.get_workflow(arguments["workflow_name"])
                if workflow:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps(workflow.to_dict(), indent=2)
                            }
                        ]
                    }
                else:
                    available = self.crm.list_workflows()
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": f"Workflow '{arguments['workflow_name']}' not found. Available: {', '.join(available)}"
                            }
                        ],
                        "isError": True
                    }

            elif tool_name == "search_elements":
                results = self.crm.search_elements(arguments["query"])
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "query": arguments["query"],
                                "count": len(results),
                                "results": [elem.to_dict() for elem in results]
                            }, indent=2)
                        }
                    ]
                }

            elif tool_name == "get_all_options":
                options = self.crm.get_all_options(arguments["field"])
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "field": arguments["field"],
                                "count": len(options),
                                "options": options
                            }, indent=2)
                        }
                    ]
                }

            elif tool_name == "validate_and_correct":
                result = self.crm.validate_and_correct(
                    arguments["field"],
                    arguments["value"]
                )
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, indent=2)
                        }
                    ]
                }

            else:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": f"Unknown tool: {tool_name}"
                        }
                    ],
                    "isError": True
                }

        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Error executing {tool_name}: {str(e)}"
                    }
                ],
                "isError": True
            }

    def handle_request(self, request: dict) -> dict:
        """Route request to appropriate handler"""
        method = request.get("method")

        if method == "initialize":
            return self.handle_initialize(request.get("params", {}))
        elif method == "tools/list":
            return self.handle_tools_list(request.get("params", {}))
        elif method == "tools/call":
            return self.handle_tools_call(request.get("params", {}))
        else:
            raise ValueError(f"Unknown method: {method}")

    def run(self):
        """Main server loop"""
        while True:
            try:
                request = read_message()
                if request is None:
                    break

                request_id = request.get("id")

                try:
                    result = self.handle_request(request)
                    response = success_response(request_id, result)
                except Exception as e:
                    response = error_response(request_id, -32603, str(e))

                write_message(response)

            except KeyboardInterrupt:
                break
            except Exception as e:
                # Log error but keep running
                logging.error(f"Server error: {e}")


def main():
    """Entry point"""
    # Set up logging to stderr (stdout is for JSON-RPC)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        stream=sys.stderr
    )

    server = ConnectiveCRMServer()
    server.run()


if __name__ == "__main__":
    main()
