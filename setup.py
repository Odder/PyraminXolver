import setuptools

setuptools.setup(
    name='PyraminXolver',
    version='1.0',
    license='MIT',
    entry_points={
        'console_scripts': [
            'pyraminxolver=pyraminxolver.command_line:main',
            'pyraminxolver-setup=pyraminxolver.command_line:setup'
        ],
    },
    author='Oscar Roth Andersen',
    author_email='oscarrothandersen@gmail.com',
    url='https://github.com/odder/pyraminxolver',
    download_url='https://github.com/odder/pyraminxolver/archive/v_01.tar.gz',
    description='This runs pyraminxolver Command Line',
    packages=['pyraminxolver'],
    python_requires='>=3.7'
)