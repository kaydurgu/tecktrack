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
