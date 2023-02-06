
.PHONY: download_dataset
download_dataset:
	kaggle datasets download -d lepchenkov/usedcarscatalog
	unzip usedcarscatalog.zip
	rm usedcarscatalog.zip
	mkdir -p data/
	mv cars.csv data/


.PHONY: create_make_yaml_template
create_make_yaml_template:
	LIST = tail -n +2 data/cars.csv | cut -d ',' -f 1 | sort | uniq | sort | tr '\n' ' '
	python3 scripts/create_template_make_yaml.py --list $(LIST) --dest config/template_make.yaml

