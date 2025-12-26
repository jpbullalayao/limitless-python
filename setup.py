import setuptools

setuptools.setup(
	name="limitless-python",
	version="1.0.1",
	author="Professor Ragna",
	author_email="professor.ragna@gmail.com",
	long_description="Python wrapper for the LimitlessTCG API",
	url="https://github.com/jpbullalayao/limitless-python",
	packages=setuptools.find_packages(),
	license="MIT",
	install_requires=['requests'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
