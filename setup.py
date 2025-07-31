import setuptools

with open("README.md", 'r', encoding = "utf-8") as f:
    long_description = f.read()
    
setuptools.setup(
    name='Text-Summarization',
    version='0.0.1',
    description='A sample Python package for Text Summarization using NLP',
    author='Sumit Garg',
    author_email='sumit0000garg@gmail.com',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src'),
    
)