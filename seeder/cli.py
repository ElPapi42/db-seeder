import random

import typer
import pymongo

from seeder import settings
from seeder.mongo import db
from seeder.users import generate_user
from seeder.companies import generate_company


app = typer.Typer()

@app.command()
def seeddb():
    # Mongo collection for companies
    companies = db.companies

    # Insert 3 companies with dummy data
    new_companies = companies.insert_many([generate_company() for i in range(3)])

    # collection for users
    users = db.users

    # An index for ensure user emails are unique
    users.create_index([('email', pymongo.ASCENDING)], unique=True)

    for company in new_companies.inserted_ids:

        # Generate 20 users for each company
        new_users = users.insert([generate_user(company) for i in range(20)])

        typer.echo(f'Register 20 Users on Company id = {company}')
