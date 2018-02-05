### < variables available for overwriting > ###

# e.g. `python3.6`
python = python3

# e.g. `/tmp/venv`
venv = venv

# options: `false` -> `default` -> `true` -> `very`
verbose = default

# e.g. `make install python=python3.6 verbose=true venv=/tmp/venv`

### </ variables available for overwriting > ###


### < venv utils > ###

# install the aiourlshortener package into the venv
.PHONY: install
install: venv-create
	@echo "Install: started"
	@$(pip) install .
	@echo "Install: finished"

# ensure a venv with dev requirements
.PHONY: venv-dev
venv-dev: venv-create
	@echo "Installing Dev requirements"
	@$(pip) install --requirement requirements-dev.txt
	@echo "Done"

### </ venv utils > ###


### < tests > ###

# check the venv and run the test-suite
.PHONY: test
test:
	@$(MAKE) -s venv-dev > /dev/null
	@$(MAKE) -s clean > /dev/null
	@$(MAKE) -s .test

### </ tests > ###


### < misc > ###

# remove the local cache and compiled python files from local directories
.PHONY: clean
clean:
	@echo "Remove the local cache and compiled Python files"
	@rm -rf .cache `find aiourlshortener tests -name __pycache__`

### </ misc > ###


################################################################################
################# internal, house keeping and debugging targets ################

### < house keeping > ###

##### < update requirements > #####

#### dev: `requirements-dev.txt` ####
.PHONY: gen-requirements
gen-requirements: .gen-requirements
	@echo "Gathering development requirements"
	@CUSTOM_COMPILE_COMMAND="make gen-requirements" \
	    $(pip-compile) --upgrade --output-file requirements-dev.txt \
	    aiourlshortener/requirements.in tests/requirements.in > /dev/null
	@echo "Done"

##### </ update requirements > #####

### </ house keeping > ###


### < internal > ###

# ensure an existing venv
.PHONY: venv-create
venv-create:
	@if [ ! -d "$(venv)/bin/" ]; then \
		echo "Creating venv" && ${python} -m venv $(venv); fi

# check for `pip-compile` and ensure an existing cache directory
.PHONY: .gen-requirements
.gen-requirements: venv-create
	@if [ ! -d $(venv)/*ib/*/site-packages/piptools ]; then \
		echo "Installing pip-tools" && $(pip) install pip-tools \
		echo "Done"; fi
	@if [ ! -d .cache ]; then mkdir .cache; fi

# run the test-suite
.PHONY: .test
.test:
	@echo "Tests: started"
	@$(pytest) tests
	@echo "Tests: all completed"

### </ internal > ###


### < parse args > ###

ifeq ($(verbose),true)
    # show detailed status messages
    f_quiet =
    f_verbose = -v
else ifeq ($(verbose),very)
    # displays full diffs for pytest
    f_quiet =
    f_verbose = -vvv
else ifeq ($(verbose),false)
    # only show basic status messages
    f_quiet = --quiet
    f_verbose =
else
    # default
    f_quiet =
    f_verbose =
endif

### </ parse args > ###


### < aliases > ###

pip = $(venv)/bin/pip $(f_quiet) $(f_verbose)
pip-compile = $(venv)/bin/pip-compile
pytest = $(venv)/bin/pytest -rs $(f_quiet) $(f_verbose)

### </ aliases > ###
