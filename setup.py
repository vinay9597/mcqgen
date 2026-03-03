from setuptools import find_packages, setup

setup(
    name="mcqgen",
    version="0.1.0",
    author="Vinay Yachamaneni",
    author_email="vinay80965@gmail.com",
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "pyPDF2",
    ],
    packages=find_packages(),
)