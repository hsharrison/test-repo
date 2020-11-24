import os
from pathlib import Path
from setuptools import setup, find_packages

metadata_path = Path(__file__).parent  / 'src' / 'packagename' / '__about__.py'
metadata = {}
with metadata_path.open() as file:
    raw_code = file.read()
exec(raw_code, metadata)
print(metadata)
metadata = {key.strip('_'): value for key, value in metadata.items()}
metadata['name'] = metadata.pop('package_name')

setup(
    long_description=open('README.md').read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[path.stem for path in Path('src').glob('*.py')],
    zip_safe=True,
    include_package_data=True,
    install_requires=[
    ],
    extras_require=dict(
        # these dependencies are not in environment.yml
        test=[
            'flake8 == 3.8.1',
            'pep8-naming == 0.8.2',
            'pydocstyle == 3.0.0',
            'pytest == 5.1.2',
            'pytest-cov == 2.7.1',
            'pytest-docstyle == 2.0.0',
            'pytest-flake8 == 1.0.6',
            'pytest-mypy == 0.4.0',
        ]
    ),

    **metadata,
)
