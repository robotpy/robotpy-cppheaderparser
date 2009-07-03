all: package

doc:
	pydoc -w CppHeaderParser/CppHeaderParser.py && mv CppHeaderParser.html CppHeaderParser/doc

package: doc
	@python setup.py sdist --formats=gztar,zip

install: doc
	@python setup.py install


upload: doc
	@python setup.py sdist upload

help:
	@echo "doc     - Build Documentation"
	@echo "package - Build a distributable package"
	@echo "install - Install the CppHeaderParser package"
	@echo "upload  - Upload the latest package to pypi"
