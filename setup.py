from setuptools import setup, find_packages

setup(
    name="file2",
    version='0.0.1',
    author='Alex Marder',
    # author_email='notlisted',
    description="File opener for gzip, bzip2, or uncompressed files.",
    url="https://github.com/alexmarder/traceutils",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rotate-scamper=rotate.rotate_scamper:main',
            'rotate-targets=rotate.rotate_targets:main'
        ],
    },
    zip_safe=False,
    include_package_data=True,
    python_requires='>3.7'
)