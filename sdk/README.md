# Connective CRM SDK

Python SDK for querying the Complete Connective CRM Reference. Provides instant, accurate access to all 74 elements, 286+ dropdown options, and validated workflows.

## Features

- ✅ **Instant lookups** - No AI calls needed for known fields
- ✅ **100% accurate** - Based on validated recording, not inference
- ✅ **Smart fuzzy matching** - Handles abbreviations (CBA → Commonwealth Bank) and typos
- ✅ **Dropdown validation** - Check if values are valid before automation runs
- ✅ **Selector fallbacks** - Auto-retry with alternative selectors if primary fails
- ✅ **Validated workflows** - Step-by-step instructions for common tasks
- ✅ **Cross-platform** - Works on Mac and Windows

## Installation

```bash
pip install rapidfuzz>=3.5.0
```

## Quick Start

```python
from sdk import CRMReference

# Initialize SDK
crm = CRMReference()

# Get selector info
lender = crm.get_selector("lender")
print(f"Selector: {lender.selector}")
print(f"Options: {len(lender.options)} lenders")

# Validate dropdown value
is_valid = crm.validate_dropdown("lender", "Commonwealth Bank")
print(f"Valid: {is_valid}")  # True

# Fuzzy match (handles abbreviations)
match = crm.fuzzy_match("lender", "CBA")
print(f"CBA → {match.matched_value}")  # "Commonwealth Bank"
print(f"Confidence: {match.confidence}%")  # 95.0%

# Get validated workflow
workflow = crm.get_workflow("add_note")
for step in workflow.steps:
    print(f"{step.number}. {step.description}")
    print(f"   Selector: {step.selector}")
```

## CLI Tool

```bash
# Get summary
python scripts/crm_query.py summary

# Get selector
python scripts/crm_query.py selector lender

# Validate value
python scripts/crm_query.py validate lender "Commonwealth Bank"

# Fuzzy match
python scripts/crm_query.py fuzzy lender "CBA"

# Get workflow
python scripts/crm_query.py workflow add_note

# Search elements
python scripts/crm_query.py search "property"

# List all options
python scripts/crm_query.py options lender
```

## MCP Server Integration

The SDK is exposed as an MCP server for use with Claude Code or other MCP clients.

### Setup

Add to `~/.claude.json`:

```json
{
  "mcpServers": {
    "connective-crm": {
      "type": "stdio",
      "command": "python3",
      "args": [
        "/Users/andrewlarkey/connective-intelligence/mcp_servers/connective_crm_server.py"
      ],
      "env": {}
    }
  }
}
```

### Available Tools

When using Claude Code, these tools are automatically available:

- `get_selector(field_name)` - Get selector info
- `validate_dropdown(field, value)` - Check if valid
- `fuzzy_match(field, value)` - Smart matching
- `get_workflow(workflow_name)` - Get workflow steps
- `search_elements(query)` - Search for elements
- `get_all_options(field)` - List all options
- `validate_and_correct(field, value)` - Validate with auto-correction

## API Reference

### CRMReference

Main SDK class.

#### Methods

**`get_selector(field_name: str) → Element`**
Get element with selector and metadata.

```python
element = crm.get_selector("lender")
# Returns Element with:
# - selector: "#lender"
# - element_type: ElementType.SELECT
# - options: [...54 lenders...]
# - section: "Unknown/Dashboard"
```

**`validate_dropdown(field: str, value: str) → bool`**
Check if a value is valid for a dropdown field.

```python
crm.validate_dropdown("lender", "Commonwealth Bank")  # True
crm.validate_dropdown("lender", "CBA")                # False
```

**`fuzzy_match(field: str, value: str) → FuzzyMatchResult`**
Smart matching with abbreviation handling.

```python
match = crm.fuzzy_match("lender", "CBA")
# Returns:
# - matched_value: "Commonwealth Bank"
# - confidence: 95.0
# - is_exact: False
# - alternatives: []
```

**`validate_and_correct(field: str, value: str) → Dict`**
Validate and provide correction if invalid.

```python
result = crm.validate_and_correct("lender", "CBA")
# Returns:
# {
#   "valid": False,
#   "original": "CBA",
#   "corrected": "Commonwealth Bank",
#   "confidence": 95.0,
#   "message": "Corrected 'CBA' to 'Commonwealth Bank'"
# }
```

**`get_workflow(name: str) → Workflow`**
Get validated workflow with steps.

```python
workflow = crm.get_workflow("add_note")
for step in workflow.steps:
    print(f"{step.description}: {step.selector}")
```

**`search_elements(query: str) → List[Element]`**
Search across all elements.

```python
results = crm.search_elements("property")
# Returns elements with "property" in name/label/section
```

**`get_all_options(field: str) → List[str]`**
Get complete list of dropdown options.

```python
lenders = crm.get_all_options("lender")
# Returns: ['AMP', 'ANZ', 'Commonwealth Bank', ... 54 total]
```

## Integration with Agents

### ExpertAgent

ExpertAgent automatically uses the SDK for instant lookups:

```python
# agent/expert_agent.py
expert = ExpertAgent(api_key, config)

# SDK is checked first, AI fallback if not found
selector_info = await expert.find_field_selector("lender")
# source: "crm_sdk" (no AI call needed!)

# Validate dropdown
result = expert.validate_dropdown_value("lender", "CBA")
# Returns correction: "Commonwealth Bank"

# Fuzzy match
match = expert.fuzzy_match_value("lender", "CBA")
# Returns: Commonwealth Bank with 95% confidence
```

### ExecutionAgent

ExecutionAgent can validate before filling:

```python
# Before filling dropdown
validation = expert.validate_dropdown_value("lender", user_input)
if not validation['valid']:
    # Auto-correct
    user_input = validation['corrected']

# Get selector with fallbacks
selector_info = await expert.find_field_selector("lender")
# Try primary selector first, then fallbacks
```

## Data Source

The SDK parses `/memory/raw/COMPLETE_CONNECTIVE_CRM_REFERENCE.md`, which contains:

- 74 elements with selectors
- 8 sections (Financials, Attachments, etc.)
- 3 validated workflows (add_note, upload_file, complete_questionnaire)
- 18 dropdown fields with 286+ options
- Selector priority guide (data-testid → ID → text → class)
- Framework detection (Froala, AG-Grid, React-Select)

## Testing

```bash
# Run SDK tests
python test_sdk.py

# Test CLI
python scripts/crm_query.py summary
python scripts/crm_query.py fuzzy lender "CBA"
```

## License

Internal use for Connective Intelligence Platform.
