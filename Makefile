all: package

doc:
	@pydoc -w CppHeaderParser/CppHeaderParser.py && mv CppHeaderParser.html CppHeaderParser/doc
	@python doc_generator.py

test:
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
