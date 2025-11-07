from setuptools import setup, find_packages

with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt","r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup( 
    name= "fraud-detection-gnn",
    version="1.0.0",
    author="Arun Ekambaram",
    author_email="arunekambaram173@gmail.com",
    description="Real-Time Fraud Detection System Using Graph Neural Networks",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arun-ekambaram/fraud-detection-gnn",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.4",
            "black>=23.12.1",
            "flake8>=7.0.0",
            "mypy>=1.8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "fraud-detection-train=models.train:main",
            "fraud-detection-serve=api.app:main",
            "fraud-detection-stream=streaming.kafka_consumer:main",
        ],
    },


)


