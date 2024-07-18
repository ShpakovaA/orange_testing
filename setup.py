from setuptools import setup

setup(
    name="orange_demo_testing",
    version="24.6.0",
    packages=["web_tests"],
    install_requires=["pytest", "selenium", "webdriver_manager"]

)
