from setuptools import setup, find_packages

setup(
    name="vw-api",
    version="0.1.0",
    description="API para consulta de dados processados da Volkswagen",
    author="Grupo 2 - M11 Volkswagen",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi==0.109.2",
        "uvicorn==0.27.1",
        "clickhouse-driver==0.2.6",
        "python-dotenv==1.0.1",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
) 