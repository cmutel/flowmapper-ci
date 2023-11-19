import typer
from scripts.match import main

app = typer.Typer()

@app.callback()
def callback():
    """
    Generate mappings between elementary flows lists
    """

app.command(name="map")(main)

if __name__ == "__main__":
    app()