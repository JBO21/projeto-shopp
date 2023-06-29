from random import randint

from faker import Faker


def rand_ratio():
    return randint (840, 900), randint(473, 573)


fake = Faker('pt_BR')
#print(signature(fake.random_number))

def make_product():
    return { 
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'category': {
            'name': fake.word()
        },
        'image': {
            'url': 'https://loremflickr.com/%s/%s/ebook' % rand_ratio(),
        },
        'rota': 'https://djangoproject.com'
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_product())
