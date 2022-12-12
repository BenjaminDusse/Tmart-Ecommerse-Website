import random
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from store.models import Collection, Product

NAME = 'collections'


class Command(BaseCommand):
    help = 'This command creates {NAME}'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many {NAME} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        products = Product.objects.all()
        try:
            for i in range(3):
                Collection.objects.create(
                    title=seeder.faker.name()
                )

            self.stdout.write(self.style.SUCCESS(
                f"{number} {NAME} created!"))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"{e} Error found ...."))
