from setuptools import setup, find_packages

setup(
    name="image-processing-joao",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow"
    ],
    author="João",
    description="Pacote simples de processamento de imagens"
)