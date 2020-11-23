import random

import typer

from seeder import settings
from seeder.mongo import db
from seeder.users import generate_user


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
    new_companies = companies.insert_many([generate_company() for i in range(3)])

    # collection for users
    users = db.users

    for company in new_companies.inserted_ids:

        # Generate 20 users for each company
        new_users = users.insert([generate_user(company) for i in range(20)])

        typer.echo(f'Register 20 Users on Company id = {company}')
