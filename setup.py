import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding = "utf-8") as fh:
    requirements = [line.strip() for line in fh.read().splitlines()]

setuptools.setup(
    name = "block_wrangler",
    version = "0.0.1",
    author = "Lowell Camp",
    author_email = "camplowell@gmail.com",
    description = "A developer tool for managing numerical block IDs during shader development.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "package URL",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages(),
    python_requires = ">=3.6",
    install_requires = requirements,
    extras_require = {
        "fuzzy_tags": ["rapidfuzz"]
    }
)
