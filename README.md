# Django-Inventory

<br />
<div align="center">
	<h3 align="center">Django Inventory Management</h3>
	<p align="center">
    	Example Django RESTful app to be used as an inventory management solution.
  	</p>
</div>


## Usage

1. Clone the repo
	```sh
	git clone https://github.com/DarioArzaba/Django-Inventory
	cd Django-Inventory
	```
2. Install the requirements and run the backend and frontend
	```sh
	pip install -r requirements.txt
	cd djangoinventory
	python manage.py runserver
	cd ..
	cd frontend
	npm install
	npm run serve 
	```
3. Install the requirements and run the backend and frontend

## Roadmap

- [x] See product catalogue
- [ ] Create buying cart
	- [ ] Make and order and add it to a list
- [ ] Manage current inventory
    - [ ] Update inventory
    - [ ] Receive products
    - [ ] Show current products and if they are available
- [ ] Show Rotation KPI and Rate of ordr rejections 
- [ ] JWT token auth
- [ ] Search and filter specific products using the API
- [ ] Frontend to interact with the platform

## License

Distributed under the [MIT License](https://mit-license.org/).

## Contact

Dario Arzaba - dario.arzaba@gmail.com