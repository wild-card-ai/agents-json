import typer
import agentsjson.core.loader as loader

app = typer.Typer()

# Default agents.json URL
DEFAULT_AGENTS_JSON_URL = "https://raw.githubusercontent.com/wild-card-ai/agents-json/refs/heads/master/agents_json/stripe/agents.json"

@app.command()
def query(
    app_name: str, 
    user_query: str, 
    model: str = typer.Option("gpt-4", "--model", help="Specify the model to use (e.g., gpt-3.5-turbo, gpt-4)."),
    agents_json: str = typer.Option(DEFAULT_AGENTS_JSON_URL, "--agents-json", help="Specify the agents.json file.")
):
    """
    Execute a query against the specified app using the provided model and agents.json file.
    """
    try:
        # Load agents.json from the specified URL or default
        data = loader.load_agents_json(agents_json)
        flows = data.agentsJson.flows

        if not flows:
            typer.echo("There are no API workflows available.")
            raise typer.Exit()

        # List available workflows
        typer.echo("Available API workflows:")
        for flow in flows:
            typer.echo(f"- {flow.title}: {flow.description}")

        # Display execution settings
        typer.echo(f"\nExecution is currently disabled.\n")
        typer.echo(f"Model: {model}")
        typer.echo(f"Agents.json URL: {agents_json}")

    except Exception as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit()
