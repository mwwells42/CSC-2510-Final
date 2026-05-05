setuptest:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test: setuptest
	python -m unittest discover tests -v

build:
	@docker build -t sotiredrn .

run:
	@docker run -itdp 8080:8080  --rm --name aaaaa sotiredrn

full: build run

clean:
	@docker stop aaaaa
	@docker image rm sotiredrn
