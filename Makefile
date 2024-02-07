VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run_forever: $(VENV)/bin/activate
  nohup $(PYTHON) main.py >/dev/null 2>&1 &

run: $(VENV)/bin/activate
  $(PYTHON) main.py


$(VENV)/bin/activate: requirements.txt
 python3 -m venv $(VENV)
 $(PIP) install -r requirements.txt


clean:
 rm -rf __pycache__
 rm -rf $(VENV)