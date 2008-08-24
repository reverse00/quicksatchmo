import os
import subprocess
from qs_settings import *
import shutil

yes_choices = ['y', 'yes', 'Yes', 'YES', '1', 'hell, yes!']
no_choices = ['n', 'no', 'No', 'NO', '0', 'no, thanks']

def create_django_project(project_name=PROJECT_NAME):
    return subprocess.call(['django-admin.py', 'startproject', project_name])
    
def append_settings():
    print 'appending to settings...'
    settings = open('settings.py', 'a')
    qs_settings = open(qs_root + os.path.sep + 'append_to_settings.py', 'r')
    settings.write('\n')
    settings.write(qs_settings.read())
    settings.close()
    qs_settings.close()

def copy_local_settings():
    print 'copying local_settings and qs_settings...'
    shutil.copy(qs_root + os.path.sep + 'local_settings.py', qs_project)
    shutil.copy(qs_root + os.path.sep + 'qs_settings.py', qs_project)

def satchmo_copy_urls():
    return subprocess.call(['python', 'manage.py', 'satchmo_copy_urls'])
    
def merge_urls():
    print 'merging urls...'
    shutil.copy('urls.py', 'urls.py.orig')
    shutil.copy('satchmo-urls.py', 'urls.py')
    
def satchmo_copy_static():
    print 'copying static files...'
    return subprocess.call(['python', 'manage.py', 'satchmo_copy_static'])
    
def satchmo_copy_templates():
    print 'copying templates files...'
    return subprocess.call(['python', 'manage.py', 'satchmo_copy_templates'])
    
def sync_db():
    print 'synchronizing with your DB...'
    return subprocess.call(['python', 'manage.py', 'syncdb'])
    
def load_l10n():
    'loading localization data'
    return subprocess.call(['python', 'manage.py', 'satchmo_load_l10n'])
    
def load_demo_data():
    print 'loading demo store data...'
    return subprocess.call(['python', 'manage.py', 'satchmo_load_store'])

def load_us_tax():
    'loading us tax table...'
    return subprocess.call(['python', 'manage.py', 'satchmo_load_us_tax'])

if not os.path.exists(INSTALL_DIR):
    print 'creating installation directory... \n'
    os.path.makedirs(INSTALL_DIR)
    
os.chdir(INSTALL_DIR)
retcode = create_django_project(PROJECT_NAME)
qs_project = os.path.join(INSTALL_DIR, PROJECT_NAME)

os.chdir(qs_project)

append_settings()
copy_local_settings()
satchmo_copy_urls() 
merge_urls()
satchmo_copy_static()
satchmo_copy_templates()
sync_db()
load_l10n()

load_demo_choice = raw_input('Would you like to load the demo store ? [y/n]: ')

if load_demo_choice in yes_choices:
    load_demo_data()
    
load_us_taxes_choice = raw_input('Would you like to load US tax table ? [y/n]: ')

if load_us_taxes_choice in yes_choices:
    load_us_tax()
    
print 'If everything worked out right, you should just run the server! Go to your installation directory and type: \n\n python manage.py runserver'