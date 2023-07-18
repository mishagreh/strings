from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent


a = get_project_root()
print(a)
complexity = input('Enter complexity rate (if any): ')
init_filename = input('Enter a file name: ')
end_filename = init_filename.lower().replace(' ', '_') + '.py'
with open(f'{a}/' + complexity + '_' + end_filename, 'w') \
        as file:
    print(f'{end_filename}     file has been created!')
