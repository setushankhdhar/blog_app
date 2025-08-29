from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create default superuser admin/helloyou if not exists'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'helloyou')
            self.stdout.write(self.style.SUCCESS('Superuser admin created.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser admin already exists.'))
