import typer

from pymongo import MongoClient

from seeder import settings

MongoClient()


app = typer.Typer()

@app.command()
def seedusers():
    typer.echo(f"{settings.DB_URL}")
