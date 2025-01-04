import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='Sweetspot',  
     version='0.1.0',
     author="Audun Skau Hansen",
     author_email="audunsh4@gmail.com",
     description=" A ray-triangle instersection challenge for the Imerso Challenge",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires = ["numba", "numpy"],
 )
