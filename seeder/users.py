import random

from passlib.context import CryptContext


pass_hasher = CryptContext(schemes=['bcrypt'], deprecated='auto')

# A list of dummy names
NAMES = [
    'alberto',
    'jose',
    'whitman',
    'pablo',
    'jacqueline',
    'thomas',
    'donald',
    'stanton',
    'elmer',
    'beatrice',
    'peachey',
    'gregory',
    'fairbanks',
    'david',
]

def generate_user(company):
    """Generate a dummy user registered on the supplied company."""
    name = random.choice(NAMES)

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
