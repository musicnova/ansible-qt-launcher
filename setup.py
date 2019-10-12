import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name='ansible-qt-launcher',
        version='0.1',
        scripts=['launcher'],
        author="ybasov1984",
        author_email="basov.yo19844@gmail.com",
        description="QT Launcher for ansible",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/musicnova/ansible-qt-launcher",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache License",
            "Operating System :: OS Independent",
        ],
)

