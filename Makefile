setup:
	pip install -r requirements.txt

test:
	python -m unittest discover tests -v

run: setup
	python application_controller.py

clean:
	rm -rf __pycache__
