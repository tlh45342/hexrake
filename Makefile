all:

clean:
	rm -rf build dist hexrake.egg-info
	
uninstall:
	pip uninstall hexrake -y
	
wheel:
	python setup.py bdist_wheel
	
install:
	make uninstall
	make clean
	make wheel
	pip install dist\hexrake-1.0-py3-none-any.whl