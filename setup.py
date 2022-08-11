import os
from setuptools import setup, find_packages


def config_discovery(module_cfg_dir, module_cfg_install_dir):
    modules_cfgs = {}
    for directory, _, files in os.walk(module_cfg_dir):
        for f in files:
            if f.endswith(".csv") or f.endswith(".json"):
                full_path = os.path.join(directory, f)
                relpath = os.path.relpath(full_path, module_cfg_dir)
                install_path = os.path.join(module_cfg_install_dir, relpath)
                install_dir, _ = os.path.split(install_path)
                if install_dir not in modules_cfgs:
                    modules_cfgs[install_dir] = []

                modules_cfgs[install_dir].append(full_path)
    print(list(modules_cfgs.items()))
    return list(modules_cfgs.items())


MODEL_CFG_DIR = "data"
MODEL_CFG_INSTALL_DIR = "data"
CFGS = config_discovery(MODEL_CFG_DIR, MODEL_CFG_INSTALL_DIR)

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='private-pgm',
    version='0.0.1',
    description='Graphical-model based estimation and inference for differential privacy.',
    url='git@github.com:ryan112358/private-pgm.git',
    author='Ryan McKenna',
    author_email='rmckenna21@gmail.com',
    license='Apache License 2.0',
    packages=['mbi'],
    package_dir={'': 'src'},
    data_files=CFGS,
    install_requires=requirements,
)
