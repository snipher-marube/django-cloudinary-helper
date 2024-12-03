from setuptools import setup, find_packages

setup(
    name="django-cloudinary-helper",
    version="0.1.0",
    author="Snipher Marube",
    author_email="sniphermarube@gmail.com",
    description="Helper package for integrating Cloudinary with Django projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
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
