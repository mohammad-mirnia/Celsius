import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='Celsius',
     version='0.1',
     scripts=['dokr'] ,
     author="Mohammad Mirnia",
     author_email="mohammad_mirnia@yahoo.com",
     description="Convert Fahrenheit to Celsius",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/mohammad-mirnia/Celsius",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )