all: package

doc:
	@pydoc -w CppHeaderParser/CppHeaderParser.py && mv CppHeaderParser.html CppHeaderParser/doc
	@python doc_generator.py

test: gen
	@echo ""
	@echo ""
	@echo "Testing Python 2.x"
	@(cd CppHeaderParser/test; python test_CppHeaderParser.py)
	@echo ""
	@echo ""
	@echo "Testing Python 3.x"
	@if [ ! -e CppHeaderParser/python3-libs ]; \
	then \
	    echo "Can't test python3 version without CppHeaderParser/python3-libs containing"; \
	    echo " * ply"; \
	    echo " * unittest"; \
	    exit 1; \
	fi;
	@(cd CppHeaderParser/test; python3 test_CppHeaderParser3.py)

package: doc gen
	@python setup.py sdist --formats=gztar,zip

install: doc
	@python setup.py install


upload: doc
	@python setup.py sdist upload

gen:
	@echo "Auto generating python 3 version..."
	@(cd CppHeaderParser; \
	cp CppHeaderParser.py CppHeaderParser3.py; \
	2to3 CppHeaderParser3.py -w -n >/dev/null 2>&1; \
	cd test; \
	cp test_CppHeaderParser.py test_CppHeaderParser3.py; \
	2to3 test_CppHeaderParser3.py -w -n >/dev/null 2>&1)

help:
	@echo "doc     - Build Documentation"
	@echo "test    - Run regression tests"
	@echo "package - Build a distributable package"
	@echo "install - Install the CppHeaderParser package"
	@echo "upload  - Upload the latest package to pypi"
