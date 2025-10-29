from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="whisper-lang",
    version="1.0.0",
    license="MIT",
    # ... other fields ...
    url="https://whisper.ibrahimmustafaopu.com",  # Main website
    project_urls={
        'Documentation': 'https://whisper.ibrahimmustafaopu.com/documentation.html',
        'Tutorial': 'https://whisper.ibrahimmustafaopu.com/tutorial.html',
        'Examples': 'https://whisper.ibrahimmustafaopu.com/examples.html',
        'Bug Reports': 'https://github.com/ibrahim787898m/whisper-lang/issues',
        'Source': 'https://github.com/ibrahim787898m/whisper-lang',
        'Changelog': 'https://github.com/ibrahim787898m/whisper-lang/blob/master/CHANGELOG.md',
    },
    include_package_data=True,
    zip_safe=False,
    author="Ibrahim Mustafa Opu",
    author_email="ibrahimmustafa787898@gmail.com",
    description="A truly unique programming language with conversational, natural English syntax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'whisper=whisper.interpreter:main',
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Interpreters",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    keywords='programming-language interpreter whisper natural-language conversational education beginner-friendly',
    python_requires='>=3.7',
    install_requires=[],
)