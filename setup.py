from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='unity_raw_to_exr',
    version='0.0.1',
    description='A utility for converting Unity Terrain Heightmap data from 16-bit raw to 16-bit exr',
    py_modules=["unity_raw_to_exr"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=[
        "numpy"
    ],
    install_requires=[
        "numpy",
        "imageio"
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
            "check-manifest"
        ]
    },
    url="https://github.com/TonyMarkham",
    author="Tony Markham",
    author_email="myonlineentity@gmail.com"
)
