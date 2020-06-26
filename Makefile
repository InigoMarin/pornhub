all: dependencies pip install

dependencies:
	sudo apt install fzf mpv python3-pip -y

pip:
	pip3 install pornhub-api

install:
	sudo cp pornhub.py /usr/local/bin/
	sudo cp pornhub /usr/local/bin/

clean:
	sudo rm -f /usr/local/bin/pornhub.py
	sudo rm -f /usr/local/bin/pornhub
