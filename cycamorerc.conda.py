server_name = server_url = 'cycamore-ci.fuelcycle.org'
port = 80

# GitHub setting
github_owner = 'cyclus'
github_repo = 'cycamore'
github_user = 'cyclus-ci'
github_credentials = '/root/polyphemusrc/gh.cred'

# BaTLab setting
batlab_user = 'cyclusci'
batlab_scripts_url = 'https://github.com/cyclus/ciclus/archive/conda.zip'
batlab_fetch_file = 'fetch/cycamore.git'
batlab_run_spec = 'cycamore.fast.run-spec'
batlab_submit_cmd = './submit.sh'
batlab_jobs_cache = '/var/www/cycamore-ci.fuelcycle.org/jobs.cache'
batlab_build_type = 'conda'

# Apache settings
log_dir = '/root/polyphemusrc'
