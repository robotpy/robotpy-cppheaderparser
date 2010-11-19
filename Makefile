all: package

doc:
	@pydoc -w CppHeaderParser/CppHeaderParser.py && mv CppHeaderParser.html CppHeaderParser/doc
	@python doc_generator.py

test:
	@(cd CppHeaderParser/test; python test_CppHeaderParser.py)

package: doc
	@python setup.py sdist --formats=gztar,zip

install: doc
	@python setup.py install


upload: doc
	@python setup.py sdist upload

help:
	@echo "doc     - Build Documentation"
	@echo "test    - Run regression tests"
	@echo "package - Build a distributable package"
	@echo "install - Install the CppHeaderParser package"
	@echo "upload  - Upload the latest package to pypi"
