# TechTrack Equipment Management API


## Endpoints

### Equipment

#### Alerts
- **GET** `/equipment/alerts/critical/`: Retrieve a list of critical alerts.
- **GET** `/equipment/alerts/high/`: Retrieve a list of high alerts.
- **GET** `/equipment/alerts/low/`: Retrieve a list of low alerts.
- **GET** `/equipment/alerts/medium/`: Retrieve a list of medium alerts.
- **GET** `/equipment/alerts/{id}/`: Retrieve details of a specific alert.
- **PUT** `/equipment/alerts/{id}/`: Update details of a specific alert.
- **PATCH** `/equipment/alerts/{id}/`: Partially update details of a specific alert.

#### Data
- **GET** `/equipment/data/{id}/`: Retrieve details of specific equipment data.
- **PUT** `/equipment/data/{id}/`: Update details of specific equipment data.
- **PATCH** `/equipment/data/{id}/`: Partially update details of specific equipment data.

#### Equipment List
- **GET** `/equipment/list/`: Retrieve a list of all equipment.  (Admin Permission need)
- **GET** `/equipment/list/instorage/`: Retrieve a list of equipment in storage.
- **GET** `/equipment/list/underrepair/`: Retrieve a list of equipment under repair.
- **GET** `/equipment/list/working/`: Retrieve a list of working equipment.
- **GET** `/equipment/responsible/{id}/`: Retrieve details of the equipment responsible worker.
- **GET** `/equipment/{id}/`: Retrieve details of specific equipment.
- **PUT** `/equipment/{id}/`: Update details of specific equipment.
- **PATCH** `/equipment/{id}/`: Partially update details of specific equipment.  
- **DELETE** `/equipment/{id}/`: Delete specific equipment.   

### Worker

#### Worker List
- **GET** `/worker/`: Retrieve a list of all workers.  
- **POST** `/worker/create/`: Create a new worker profile. 
- **GET** `/worker/{id}/`: Retrieve details of specific worker. 


# Models

## Profile
Represents a worker profile in the system.

### Fields
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

## Equipment
Represents equipment in the system.

### Fields
- **type**: Type of equipment (terminal, coffee machine, force meter, game console).
- **model**: Equipment model.
- **registration_date**: Date when the equipment was registered in warehouse.
- **status**: Current status of the equipment (working, under repair, in storage).
- **added_by**: Worker who added the equipment.
- **responsible**: Worker responsible for the equipment(Reference to the Profile).

## Data
Represents data of equipment.

### Fields
- **equipment**: Reference to the equipment.
- **timestamp**: Time when data is updated.
- **temperature**: Temperature of equipment.
- **speed**: Speed of equipment.
- **pressure**: Pressure  of equipment.
- **is_active**: Whether the equipment working.
- **address**: Location of equipment.

## Alerts
Represents alerts related to equipment.

### Fields
- **equipment**: Reference to the equipment.
- **timestamp**: Time when the alert was created.
- **description**: Description of the alert.
- **severity**: Severity level of the alert (low, medium, high, critical).
- **detected_by**: Worker who detected the alert.(Reference to the Profile of worker)
- **resolved_by**: Worker who resolved the alert (optional)(Reference to the Profile of worker) .

  
## Profile Groups and Permissions

### Admin
- **Permissions**:
  - Managment(CREAT, READ, DELETE, UPDATE) of equipment.
  - Managment(CREAT, READ, DELETE, UPDATE) of alerts.
  - Managment(CREAT, READ, DELETE, UPDATE) of data.
  - Managment(CREAT, READ, DELETE, UPDATE) worker profiles.
  - etc...

### Repairman
- **Permissions**:
  - Can change alerts.
  - Can view alerts.
  - Can change data.
  - Can view data.
  - Can view profile.

### Warehouseman
- **Permissions**:
  - Can view alerts.
  - Can view data.
  - Can change equipment.
  - Can view equipment.
  - Can view profile.
