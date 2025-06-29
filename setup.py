from setuptools import setup

setup(
    name='RibORF',
    version='2.0',
    description='Identifying genome-wide translated open reading frames using ribosome profiling',
    author='Zhe Ji',
    author_email='zhe.ji@northwestern.edu',
    url='https://github.com/zhejilab/RibORF/tree/master/RibORF.2.0',
    license='GNU GPL v3',
    # tells setuptools to install any scripts under bin/
    scripts=['bin/mergeORF', 'bin/offsetCorrect', 'bin/ORFannotate', 'bin/parameterOffset', 'bin/readDist', 'bin/removeAdapter', 'bin/ribORF'],
    # no Python dependencies:
    install_requires=[],
    classifiers=[
        'Programming Language :: Perl',
        'License :: GNU GPL v3',
        'Operating System :: OS Independent',
    ],
    zip_safe=False,
)
