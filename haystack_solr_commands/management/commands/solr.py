import os
import subprocess

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    """
    Development command to download and start Solr if needed
    Or Start and create a Core if needed and assures the right schema is in place
    """
    def handle(self, *args, **kwargs):
        install_dir = os.path.join(settings.SOLR_DIRECTORY, 'solr-%s' % settings.SOLR_VERSION)
        rebuild = False
        if not os.path.exists(install_dir):
            install(install_dir)
            rebuild = True

        # will rebuild index if is a new install
        call_command('run_solr', rebuild_index=rebuild)


def install(install_dir):
    url = 'http://mir2.ovh.net/ftp.apache.org/dist/lucene/solr/%s/solr-%s.tgz' % (settings.SOLR_VERSION, settings.SOLR_VERSION)
    if os.path.exists(install_dir + ".tgz"):
        subprocess.call('rm %s' % 'solr-%s.tgz' % settings.SOLR_VERSION, cwd=settings.SOLR_DIRECTORY, shell=True)

    subprocess.call(" ".join(['wget', url]), cwd=settings.SOLR_DIRECTORY, shell=True)
    subprocess.call(" ".join(['tar', 'xzf', 'solr-%s.tgz' % settings.SOLR_VERSION]), cwd=settings.SOLR_DIRECTORY, shell=True)
    subprocess.call(" ".join(['rm', os.path.join(settings.SOLR_DIRECTORY, 'solr-%s.tgz' % settings.SOLR_VERSION)]), cwd=settings.SOLR_DIRECTORY, shell=True)
    subprocess.call(" ".join(['bin/solr', 'start']), cwd=install_dir, shell=True)
