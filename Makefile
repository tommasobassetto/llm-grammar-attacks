all:
	echo "Script only intended for use on Linux."
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt