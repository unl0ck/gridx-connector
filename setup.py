from setuptools import setup, find_packages

setup(
    name='gridx-connector',
    version='1.0.1',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    description="Connector for GridX to fetch live data from your Photovoltaic System",
    packages=find_packages(),
    install_requires=[
        'requests',
        'authlib'
    ],
    package_data={
        'gridx_connector': ['eon-home.config.json','viessmann.config.json'],
    },
    entry_points={
        'console_scripts': [
            'gridx=gridx_connector.cli:main',
        ],
    },
)
