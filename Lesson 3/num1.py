def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return True if command in ignore else False

print(ignore_command('alias'))
print(ignore_command('ip'))

print(ignore_command('ipasd'))
