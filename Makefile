all: dependencies pip install

dependencies:
	sudo apt install fzf mpv xargs python3-pip -y

pip:
	pip3 install pornhub-api

install:
	sudo cp pornhub.py /usr/local/bin/
	sudo cp pornhub /usr/loca/bin/

clean:
	sudo rm -f /usr/local/bin/pornhub.py
	sudo rm -f /usr/local/bin/pornhub
