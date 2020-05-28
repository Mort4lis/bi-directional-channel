from subprocess import PIPE, Popen, TimeoutExpired

from settings import config

config = config['postgres']

args = (
    '/usr/bin/psql',
    '-d', config['database'],
    '-U', config['user'],
    '--no-password',
    '-h', config['host'],
    '-p', str(config['port'])
)
with Popen(args, stdin=PIPE, stdout=PIPE, env={'PGPASSWORD': config['password']}) as process:
    query = b'SELECT VERSION();'
    try:
        stdout, stderr = process.communicate(input=query, timeout=5)
    except TimeoutExpired as e:
        print(e)
    else:
        print(stdout.decode('utf-8'))
