# Wildcard Integrations

Integration modules for Wildcard Python implementation. This package provides various service integrations that can be used with the Wildcard core package.

## Available Integrations

- Twitter
- Giphy
- More integrations coming soon...

## Installation

### Basic Installation
```bash
pip install wildcard-integrations
```

### With Specific Integrations
```bash
# Install with Twitter integration
pip install wildcard-integrations[twitter]

# Install with Giphy integration
pip install wildcard-integrations[giphy]

# Install with multiple integrations
pip install wildcard-integrations[twitter,giphy]

# Install all integrations
pip install wildcard-integrations[all]
```

## Development

This package is managed with Poetry. To set up your development environment:

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies (including all integrations for development):
   ```bash
   poetry install --all-extras
   ```

3. Run tests:
   ```bash
   poetry run pytest
   ```

## Adding New Integrations

To add a new integration:

1. Create a new directory under `wildcard/integrations/`
2. Add the integration's dependencies to pyproject.toml:
   - Add as an optional group under `[tool.poetry.group.<integration>]`
   - Add to `[tool.poetry.extras]` for pip installation
3. Implement the required tools and mapping functions
4. Add appropriate tests
5. Update this README with the new integration

## License

Apache 2.0 License (See LICENSE file for details) 
