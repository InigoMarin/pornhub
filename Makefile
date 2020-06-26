all: dependencies pip install

dependencies:
	sudo apt install fzf mpv python3-pip suckless-tools -y

pip:
	pip3 install pornhub-api
	pip3 install youtube-dl

install:
	sudo cp pornhub.py /usr/local/bin/
	sudo cp pornhub /usr/local/bin/

clean:
	sudo rm -f /usr/local/bin/pornhub.py
	sudo rm -f /usr/local/bin/pornhub
