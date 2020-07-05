import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="DefCurse",
    version="0.0.1",
    author="Sakuk",
    author_email="lukas.fritsch30@gmail.com",
    description="High level terminal user interface library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sakuk/DefCurse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)