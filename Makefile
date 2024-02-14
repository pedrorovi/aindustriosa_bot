open_env:
	@echo "source env/bin/activate"

close_env:
	@echo "deactivate"

install_requirements:
	@echo "Installing requirements..."
	@. env/bin/activate; pip install -r requirements.txt

list_packages:
	@echo "Listing packages..."
	@. env/bin/activate; pip list

docker_build:
	@echo "Building docker image..."
	@docker build -t aindustriosa_info_bot .

docker_run:
	@echo "Running docker image..."
	@docker run -d -p 4000:80 aindustriosa_info_bot