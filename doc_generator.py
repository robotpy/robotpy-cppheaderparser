#!/usr/bin/python
# Generate documenation
# * README.txt
# * README.html
import sys

def gen_readme_html():
    """generate README.html"""
    import cgi
    f = open("templates/README.html").read()
    sampleClass = open("CppHeaderParser/examples/SampleClass.h").read()
    readSampleClass = open("CppHeaderParser/examples/readSampleClass.py").read()
    
    f = f.replace("{SAMPLE_CLASS_H}", cgi.escape(sampleClass))
    f = f.replace("{READ_SAMPLE_CLASS_PY}", cgi.escape(readSampleClass))
    f = f.replace("{READ_SAMPLE_CLASS_PY_OUTPUT}", cgi.escape(get_sample_class_output()))
    open("README.html", "wa").write(f)


def gen_readme_txt():
    """generate README.txt"""
    import cgi
    f = open("templates/README.txt").read()
    sampleClass = open("CppHeaderParser/examples/SampleClass.h").read()
    readSampleClass = open("CppHeaderParser/examples/readSampleClass.py").read()
    
    f = f.replace("{SAMPLE_CLASS_H}", "    " + sampleClass.replace("\n", "\n    "))
    f = f.replace("{READ_SAMPLE_CLASS_PY}", "    " + readSampleClass.replace("\n", "\n    "))
    f = f.replace("{READ_SAMPLE_CLASS_PY_OUTPUT}", "    " + get_sample_class_output().replace("\n", "\n    "))
    open("README.txt", "wa").write(f)
    print "wrote README.txt"
    
    import docutils.core
    h = docutils.core.publish_string(source=open("README.txt").read(), writer_name='html')
    h = h.replace("</style>", "/*customization*/\npre.literal-block{\ncolor: #6A6A6A;\n}\n\n</style>")
    h = h.replace('<pre class="literal-block">', '<pre class="literal-block" width="1200px" style="max-width: 1200px">')
    open("README.html", "wa").write(h)
    print "wrote README.html"


def get_sample_class_output():
    import subprocess
    return subprocess.Popen(["python", "readSampleClass.py"],
        stdout=subprocess.PIPE,
        cwd="CppHeaderParser/examples"
        ).communicate()[0]




if __name__ == "__main__":
    gen_readme_txt()
