import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyourls3",
    version="1.0.3",
    author="Thomas Pain",
    author_email="pyourls3@tdpain.net",
    description="A Python 3 API wrapper for YOURLS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codemicro/pyourls3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=["requests==2.22.0"]
)