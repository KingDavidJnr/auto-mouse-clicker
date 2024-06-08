from setuptools import setup, find_packages

setup(
    name='auto-clicker',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyautogui',
    ],
    entry_points={
        'console_scripts': [
            'auto-clicker=auto_clicker:main',
        ],
    },
    author='David Oduse',
    author_email='odusedavid@gmail.com',
    description='Python auto-clicker script that automates mouse clicks at defined intervals and visually indicates each click with a bubble overlay.',
    long_description=open('DOCS.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KingDavidJnr/auto-mouse-clicker',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
