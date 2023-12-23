from django_seed import Seed
from dione.models import Company, Employee

seeder = Seed.seeder()

seeder.add_entity(Company, 5, {
    'name': lambda x: seeder.faker.company()
})

seeder.add_entity(Employee, 10, {
    'name': lambda x: seeder.faker.last_name(),
    'surname': lambda x: seeder.faker.first_name(),
    'job_position': lambda x: seeder.faker.job(),
})

inserted_pks = seeder.execute()
