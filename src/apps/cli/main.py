import typer

from src.apps.cli.commands.migrate import cli

app = typer.Typer()
app.add_typer(cli, name="migrate")


if __name__ == "__main__":
    app()
