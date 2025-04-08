from setuptools import Extension, setup, find_packages

module = Extension('pymsilib._msi',
    libraries = ['Msi','Rpcrt4', 'Cabinet'],
    sources = ['src/_msi.c'],
)

setup(
    packages=find_packages(),
    include_package_data=True,
    ext_modules=[module]
)
