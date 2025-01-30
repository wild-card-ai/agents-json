# Wildcard Core

Core functionality package for Wildcard Python implementation. This package provides the fundamental components for executing flows, handling authentication, and managing tool operations.

## Features

- Flow execution engine
- Authentication handling (OAuth1, OAuth2, API Key, Bearer, Basic)
- Parameter linking and mapping
- Tool operation management

## Installation

```bash
pip install wildcard-core
```

## Development

This package is managed with Poetry. To set up your development environment:

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Run tests:
   ```bash
   poetry run pytest
   ```

## License

MIT License (See LICENSE file for details) 
