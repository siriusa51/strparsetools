
all: clean build-whl

.PHONY: build-whl
build-whl:
	pip install -U build twine
	python -m build


.PHONY: to-testpypi
to-testpypi:
	twine upload --repository testpypi dist/*


.PHONY: to-pypi
to-pypi:
	twine upload --repository pypi dist/*


.PHONY: clean
clean:
	rm -rf dist/ *.egg-info/
