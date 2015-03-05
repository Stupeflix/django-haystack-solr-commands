import os
import subprocess

from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.management import call_command


class Command(BaseCommand):
    """
    Development command
    """
    def handle(self, *args, **kwargs):
        install_dir = os.path.join(settings.SOLR_DIRECTORY, 'solr-%s' % settings.SOLR_VERSION)
        subprocess.call(" ".join(['bin/solr', 'restart']), cwd=install_dir, shell=True)
        try:
            # solr create always return 1 even when it's successfull...
            subprocess.call(" ".join(['bin/solr', 'create', '-c', settings.SOLR_CORE]), shell=True, cwd=install_dir)
        except subprocess.CalledProcessError as exc:
            print exc

        call_command('update_solr_schema')

        if 'rebuid_index' in kwargs:
            call_command('rebuild_index')
