import typer


app = typer.Typer()

@app.command()
def seedusers(name: str):
    typer.echo(f"Hello {name}")
