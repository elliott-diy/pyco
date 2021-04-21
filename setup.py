import setuptools

with open('readme.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name = "pyco",
    version = "0.7",
    author = "Duplexes",
    maintainer = "LemonPi314",
    author_email = "no@email.com",
    description = "Colored console printing and input, ANSI escape codes, and logging functions.",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Duplexes/pyco',
    keywords=['console', 'terminal', 'ansi', 'color'],
    license = "MIT",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    packages = setuptools.find_packages(),
    python_requires = '>=3.6.8',
)