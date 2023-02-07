
.PHONY: download_dataset
download_dataset:
	kaggle datasets download -d lepchenkov/usedcarscatalog
	unzip usedcarscatalog.zip
	rm usedcarscatalog.zip
	mkdir -p data/
	mv cars.csv data/

LIST := $(shell tail -n +2 data/cars.csv | cut -d ',' -f 1 | sort | uniq | sort | tr '\n' ' ')

.PHONY: create_make_yaml_template
create_make_yaml_template:
	python3 scripts/create_make_yaml_template.py --make-list $(LIST) --dest template_make.yaml

