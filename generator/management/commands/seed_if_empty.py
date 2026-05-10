"""Run seed_templates only if Template table is empty.
Idempotent: safe to run on every deploy. Used in startCommand so a
fresh DB (e.g. after switching providers) gets bootstrapped without
manual shell access on free Render tier.
"""
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run seed_templates only if Template table is empty."

    def handle(self, *args, **options):
        from generator.models import Template
        try:
            count = Template.objects.count()
        except Exception as exc:
            self.stdout.write(
                self.style.WARNING(
                    f"seed_if_empty: skipping (DB not ready: {exc})"
                )
            )
            return
        if count > 0:
            self.stdout.write(
                f"seed_if_empty: {count} templates already exist, skipping"
            )
            return
        self.stdout.write("seed_if_empty: empty table — running seed_templates")
        call_command('seed_templates')
        self.stdout.write(
            self.style.SUCCESS(
                f"seed_if_empty: done, {Template.objects.count()} templates loaded"
            )
        )
