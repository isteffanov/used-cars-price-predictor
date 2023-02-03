
.PHONY: download_dataset
download_dataset:
	kaggle datasets download -d lepchenkov/usedcarscatalog
	unzip usedcarscatalog.zip
	rm usedcarscatalog.zip
	mkdir -p data/
	mv cars.csv data/