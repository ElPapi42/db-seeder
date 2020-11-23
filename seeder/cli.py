import random

import typer
from passlib.context import CryptContext

from seeder import settings
from seeder.mongo import db


app = typer.Typer()
pass_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

def generate_user(company):
    """Generate a dummy user registered on the supplied company."""
    names = [
        'alberto',
        'jose',
        'whitman',
        'pablo',
        'ruso'
    ]

    name = random.choice(names)

    return {
        'email': f'{name}@gmail.com',
        'password': pass_hasher.hash(name),
        'company_id': company,
        'profile': {
            'name': name,
            'last_name': name[::-1],
            'age': random.randint(19, 23),
            'gender': 'M' if random.randint(0, 1) else 'F',
            'document_number': str(random.randint(26493929, 31456896))
        },
    }

@app.command()
def seeddb():
    # Mongo collection for companies
    companies = db.companies

    # Insert 3 companies with dummy data
    new_companies = companies.insert([generate_company() for i in range(3)])

    users = db.users

    for company in new_companies:

        typer.echo(generate_user(company))
