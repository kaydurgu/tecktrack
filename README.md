# Equipment Management 
## Overview
The Equipment Management System is designed to streamline the management of equipment, alerts, data, and worker profiles. This system is particularly useful for organizations that need to keep track of various equipment statuses, handle alerts efficiently, and manage worker information. The system supports various roles with specific permissions to ensure secure and efficient operations.

**This project includes only the backend implementation.**

## Features

### Equipment Management
- **List all equipment**: Admins can retrieve a comprehensive list of all equipment.
- **Filter equipment**: Retrieve lists of equipment based on their status (in storage, under repair, working).
- **Manage equipment**: Create, update, partially update, or delete equipment records.
- **Responsible worker**: Assign and retrieve details of the worker responsible for specific equipment.

### Alerts Management
- **Retrieve alerts**: View alerts based on their severity (critical, high, medium, low).
- **Manage alerts**: Update or partially update alert details.
- **Alert details**: Retrieve detailed information about specific alerts.

### Data Management
- **Retrieve equipment data**: View detailed data for specific equipment, including temperature, speed, pressure, and location.
- **Manage data**: Update or partially update equipment data.

### Worker Management
- **List workers**: Retrieve a list of all workers.
- **Create worker profile**: Add new worker profiles.
- **Manage worker profile**: Retrieve details, update, or partially update worker profiles.


## Endpoints

### Equipment

#### Alerts
- **GET** `/equipment/alerts/critical/`: Retrieve a list of critical alerts.[Authorization required]
- **GET** `/equipment/alerts/high/`: Retrieve a list of severity-medium alerts.       [Authorization required]
- **GET** `/equipment/alerts/low/`: Retrieve a list of severity-medium alerts.      [Authorization required]
- **GET** `/equipment/alerts/medium/`: Retrieve a list of severity-medium alerts.  [Authorization required]
- **GET** `/equipment/alerts/{id}/`: Retrieve details of a specific alert.        [Authorization required]
- **PUT** `/equipment/alerts/{id}/`: Update details of a specific alert.        [Authorization required, Warehouseman Permission needed]
- **PATCH** `/equipment/alerts/{id}/`: Partially update details of a specific alert.   [Authorization required, Warehouseman Permission needed]

#### Data
- **GET** `/equipment/data/{id}/`: Retrieve details of specific equipment data.  [Authorization required, Admin Permission need or Warehouseman Permission need ] 
- **PUT** `/equipment/data/{id}/`: Update details of specific equipment data.   
- **PATCH** `/equipment/data/{id}/`: Partially update details of specific equipment data.

#### Equipment List
- **GET** `/equipment/list/`: Retrieve a list of all equipment.  [Authorization required, Admin Permission needed | Warehouseman Permission needed ] 
- **GET** `/equipment/list/instorage/`: Retrieve a list of equipment in storage.  [Authorization required, Admin Permission needed | Warehouseman Permission needed ] 
- **GET** `/equipment/list/underrepair/`: Retrieve a list of equipment under repair. [Authorization required, Admin Permission needed | Warehouseman Permission needed ] 
- **GET** `/equipment/list/working/`: Retrieve a list of working equipment.         [Authorization required, Admin Permission needed | Warehouseman Permission needed ] 
- **GET** `/equipment/responsible/{id}/`: Retrieve details of the equipment responsible worker. [Authorization required ] 
- **GET** `/equipment/{id}/`: Retrieve details of specific equipment.[Authorization required ] 
- **PUT** `/equipment/{id}/`: Update details of specific equipment.  [Authorization required, Admin Permission needed  ] 
- **PATCH** `/equipment/{id}/`: Partially update details of specific equipment.   [Authorization required, Admin Permission needed | Warehouseman Permission needed ] 
- **DELETE** `/equipment/{id}/`: Delete specific equipment.     [Authorization required, Admin Permission needed] 

### Worker

#### Worker List
- **GET** `/worker/`: Retrieve a list of all workers.    [Authorization required, Admin Permission need]  
- **POST** `/worker/create/`: Create a new worker profile.  [Authorization required, Admin Permission need] 
- **GET** `/worker/{id}/`: Retrieve details of specific worker. [Authorization required] 


## Data Models

### Profile
Represents a worker profile in the system.

#### Fields
- **username**: Worker's unique username.
- **email**: Worker's email address.
- **phone_number**: Worker's phone number.
- **first_name**: Worker's first name.
- **last_name**: Worker's last name.
- **birth_date**: Worker's birth date.
- **address**: Worker's address.
- **position**: Worker's job position.
- **hire_date**: Date the worker was hired.
- **bio**: Worker's biography.
- **is_active**: Whether the worker is working.
- **role**: Worker's role (repairman, warehouseman, admin).
- **groups**: Groups the worker belongs to.
- **user_permissions**: Permissions assigned to the worker.

### Equipment
Represents equipment in the system.

#### Fields
- **type**: Type of equipment (terminal, coffee machine, force meter, game console).
- **model**: Equipment model.
- **registration_date**: Date when the equipment was registered in warehouse.
- **status**: Current status of the equipment (working, under repair, in storage).
- **added_by**: Worker who added the equipment.
- **responsible**: Worker responsible for the equipment(Reference to the Profile).

### Data
Represents data of equipment.

#### Fields
- **equipment**: Reference to the equipment.
- **timestamp**: Time when data is updated.
- **temperature**: Temperature of equipment.
- **speed**: Speed of equipment.
- **pressure**: Pressure  of equipment.
- **is_active**: Whether the equipment working.
- **address**: Location of equipment.

### Alerts
Represents alerts related to equipment.

#### Fields
- **equipment**: Reference to the equipment.
- **timestamp**: Time when the alert was created.
- **description**: Description of the alert.
- **severity**: Severity level of the alert (low, medium, high, critical).
- **detected_by**: Worker who detected the alert.(Reference to the Profile of worker)
- **resolved_by**: Worker who resolved the alert (optional)(Reference to the Profile of worker) .

  
### Profile Groups and Permissions

#### Admin
- **Permissions**:
  - Managment(CREAT, READ, DELETE, UPDATE) of equipment.
  - Managment(CREAT, READ, DELETE, UPDATE) of alerts.
  - Managment(CREAT, READ, DELETE, UPDATE) of data.
  - Managment(CREAT, READ, DELETE, UPDATE) worker profiles.
  - etc...

#### Repairman
- **Permissions**:
  - Can change alerts.
  - Can view alerts.
  - Can change data.
  - Can view data.
  - Can view profile.

#### Warehouseman
- **Permissions**:
  - Can view alerts.
  - Can view data.
  - Can change equipment.
  - Can view equipment.
  - Can view profile.
 
  
## Screenshots and Video Demonstration

Equipment related endpoints 

![Equipment related endpoints](https://github.com/kaydurgu/tecktrack/blob/main/screens/Screenshot_17.png)

Worker related endpoints 

![Worker related endpoints ](https://github.com/kaydurgu/tecktrack/blob/main/screens/Screenshot_18.png)

Alerts Data model details 

![Alerts Data model details ](https://github.com/kaydurgu/tecktrack/blob/main/screens/Screenshot_19.png)

Data Model details 

![Data Model details  ](https://github.com/kaydurgu/tecktrack/blob/main/screens/Screenshot_20.png)

Equipment Data Model details 

![Equipment Ddata Model details ](https://github.com/kaydurgu/tecktrack/blob/main/screens/Screenshot_21.png)

Profile Data Model details 

![Equipment Ddata Model details ](https://github.com/kaydurgu/tecktrack/blob/main/screens/Screenshot_22.png)

- **GET** `/equipment/responsible/{id}/`: Retrieve details of the equipment responsible worker. [Authorization required ] 

![Equipment Ddata Model details ](https://github.com/kaydurgu/tecktrack/blob/main/screens/Screenshot_23.png)

- **GET** `/equipment/list/instorage/`: Retrieve a list of equipment in storage.  [Authorization required, Admin Permission needed | Warehouseman Permission needed ]

![Equipment Ddata Model details ](https://github.com/kaydurgu/tecktrack/blob/main/screens/Screenshot_24.png)

- **GET** `/worker/`: Retrieve a list of all workers.    [Authorization required, Admin Permission need]
![Equipment Ddata Model details ](https://github.com/kaydurgu/tecktrack/blob/main/screens/Screenshot_25.png)
-  
## Getting Started

To run the application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables for API keys and database configurations.
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Contributors

- Bakytbek uulu Zhanbolot

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
