import random
from faker import Faker

fake = Faker()

fake1 = Faker('ko_KR')
Faker.seed_instance(87654321)

print(fake1.name())

fake2 = Faker('ko_KR')
print(fake2.name())