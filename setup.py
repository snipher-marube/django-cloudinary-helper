from setuptools import setup, find_packages
import pathlib

# Get the long description from the README file
here = pathlib.Path(__file__).parent.resolve()
long_description = ""
try:
    long_description = (here / "README.md").read_text(encoding="utf-8")
except FileNotFoundError:
    print("README.md file not found. Please add it for long_description.")

setup(
    name="django-cloudinary-helper",
    version="0.2.4",
    author="Snipher Marube",
    author_email="sniphermarube@gmail.com",
    description="Helper package for integrating Cloudinary with Django projects.",
    
    long_description=long_description,
    long_description_content_type="text/markdown",  # Use 'text/markdown' for Markdown or 'text/x-rst' for reStructuredText
    url="https://github.com/snipher-marube/django-cloudinary-helper",
    packages=find_packages(),
    install_requires=[
        "django>=3.0",
        "django-storages",
        "cloudinary"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
