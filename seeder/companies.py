import random
from uuid import uuid4


COMPANIES = [
    'Ala Delta',
    'Next Evo',
    'Dummy File',
    'Dummy Lol',
    'The Past',
    'Bulk Edit',
    'Dele Home',
    'Daleware',
    'Macham',
    'HloP',
]

ADDRESSES = [
    '4 Swinburne Street, Derby',
    'The Old Red Lion, North Cheriton',
    '32 Westwood Road, East Peckham',
    'Flat A, 20 Redfearn Mews, Harrogate',
    'Little Furzy, Tanyard, Nether Stowey',
    '18 Oak Lane, Ambrosden',
    '100 Church Road, Hadleigh',
    'Flat 1, Westgate Court, 297 Long Lane, Hillingdon',
    '4 Orchard Close, Hemel Hempstead',
    '6 Gainsborough Close, Grange Farm'
]

def generate_company():
    """Generates random data for a dummy company."""
    return {
        'name': f'{random.choice(COMPANIES)} {str(uuid4())[:8]}',
        'nit': random.randint(1000000, 9999999),
        'address': random.choice(ADDRESSES),
    }
