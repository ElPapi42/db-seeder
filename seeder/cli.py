import typer
import random

from seeder import settings
from seeder.mongo import db


app = typer.Typer()

def generate_company():
    """Generates random data for a dummy company."""
    companies = [
        'Ala Delta',
        'Next Evo',
        'Dummy File',
        'Dummy Lol'
    ]

    addresses = [
        'Calle 15',
        'Calle 16',
        'Calle 17',
        'Calle 18'
    ]

    return {
        'name': random.choice(companies),
        'nit': random.randint(100000, 999999),
        'address': random.choice(addresses),
    }

@app.command()
def seeddb():
    # Mongo collection for companies
    companies = db.companies

    # Insert 3 companies with dummy data
    new_companies = companies.insert([generate_company() for i in range(3)])

    users = db.users

    for company in new_companies:
        typer.echo(company)

