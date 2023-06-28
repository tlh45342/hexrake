all:

build:
	pip wheel --no-deps -w dist .

clean:
	rm -rf build dist hexrake.egg-info
	
uninstall:
	pip uninstall hexrake -y
	
wheel:
	pip wheel --no-deps -w dist .
	
install:
	make uninstall
	make clean
	make wheel
	pip install dist/hexrake-1.0-py3-none-any.whl
