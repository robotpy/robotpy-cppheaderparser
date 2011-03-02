all: package

doc:
	@pydoc -w CppHeaderParser/CppHeaderParser.py && mv CppHeaderParser.html CppHeaderParser/doc
	@python doc_generator.py

test: gen
	@echo -e "\n\nTesting Python 2.x"
	@(cd CppHeaderParser/test; python test_CppHeaderParser.py)
	@echo -e "\n\nTesting Python 3.x"
	@(cd CppHeaderParser/test; python3 test_CppHeaderParser3.py)

package: doc gen
	@python setup.py sdist --formats=gztar,zip

install: doc
	@python setup.py install


upload: doc
	@python setup.py sdist upload

gen:
	@(cd CppHeaderParser; \
	cp CppHeaderParser.py CppHeaderParser3.py; \
	2to3 CppHeaderParser3.py -w -n >/dev/null; \
	cd test; \
	cp test_CppHeaderParser.py test_CppHeaderParser3.py; \
	2to3 test_CppHeaderParser3.py -w -n >/dev/null)

help:
	@echo "doc     - Build Documentation"
	@echo "test    - Run regression tests"
	@echo "package - Build a distributable package"
	@echo "install - Install the CppHeaderParser package"
	@echo "upload  - Upload the latest package to pypi"
