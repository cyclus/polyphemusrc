server_name = server_url = 'cyclus-ci.fuelcycle.org'
port = 80

# GitHub setting
github_owner = 'cyclus'
github_repo = 'cyclus'
github_user = 'cyclus-ci'
github_credentials = '/root/cyclusrc/gh.cred'

# BaTLab setting
batlab_user = 'cyclusci'
batlab_scripts_url = 'https://github.com/cyclus/ciclus/archive/master.zip'
batlab_fetch_file = 'fetch/cyclus.git'
batlab_run_spec = 'cyclus.fast.run-spec'
batlab_submit_cmd = './submit.sh'
batlab_jobs_cache = '/var/www/cyclus-ci.fuelcycle.org/jobs.cache'

# Apache settings
log_dir = '/root/cyclusrc'
