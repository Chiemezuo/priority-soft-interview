# Online Store Inventory & Supplier Management API
## By: Chiemezuo Akujobi

## Introduction
This is the documentation guide for the interview task I was given by [Priority Soft](https://www.prioritysoft.rs/) for the **Django Developer Position**

## Features
* Item Inventory Management.
* Supplier Management.
* Relationship between Inventory Items and Suppliers.
* CRUD operations for both Items and Suppliers.
* Unit tests for the CRUD operations of both Items and Suppliers.
* Requirements file for easy installation/setup.

## Setup Pre-requisites
1. A computer running Windows/Linux/Mac.
2. A recent [Python](https://www.python.org/downloads/) installation (3.8.x and above).
3. [Django](https://www.djangoproject.com/download/) (4.2.x and above, preferably 5.0.x and above).
4. Django Rest Framework ([DRF](https://www.django-rest-framework.org/#installation)).
5. **Optional**: [Virtualenv](https://pypi.org/project/virtualenv/)

## Installation Steps
1. Add this project folder anywhere into your local machine.
2. **Optional**: Create a virtual environment. This is not needed, but it is recommended. See link for setup in pre-requisites section.
3. Navigate to the root folder of the project.
4. Install dependencies. You can achieve this by running `pip install -r requirements.txt`
5. Apply migrations using the command: `python manage.py migrate`
6. Run the dev server. You can use the following command for this: `python manage.py runserver`
7. Access the API. To do this, open your browser and go to: `http://localhost:8000/` or whichever default you specified after the `runserver` command.
8. You can navigate to the URLs that will be shown on your screen, and you can append an integer to either of the shown URLs to get the specific Item or Supplier instance (and perform other CRUD operations).

## API Endpoints
>**Note**: When you navigate to any of these endpoint URLs, you will be able to handle CRUD operations from within the browser, and will not need an external API client app like Postman, Insomnia, or ThunderClient.

- **Items**:
  - `GET /items/` - List all items
  - `POST /items/` - Create a new item
  - `GET /items/{id}/` - Retrieve a specific item
  - `PATCH /items/{id}/` - Update a specific item
  - `DELETE /items/{id}/` - Delete a specific item

- **Suppliers**:
  - `GET /suppliers/` - List all suppliers
  - `POST /suppliers/` - Create a new supplier
  - `GET /suppliers/{id}/` - Retrieve a specific supplier
  - `PATCH /suppliers/{id}/` - Update a specific supplier
  - `DELETE /suppliers/{id}/` - Delete a specific supplier

## Tests
To run the automated tests I've written so far, use the following command:
```
  python manage.py test
```

## Note:
* This project is configured to use the default SQLite database, but you can update the `Settings` if you want to use a different database.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.