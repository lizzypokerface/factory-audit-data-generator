# Factory Audit Data Generator

## Overview

The **Factory Audit Data Generator** is a Python program designed to generate CSV files containing simulated audit and contact data for a sporting apparel company. It utilizes the `pandas`, `numpy`, and `Faker` libraries to create realistic datasets that can be used for testing and analysis.

## Prerequisites

- Python 3.12 or later

## Installation

1. **Create a Virtual Environment**

   First, create a virtual environment to isolate your dependencies:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install Required Packages**

   Use the provided `requirements.txt` to install the necessary libraries:

   ```bash
   pip install -r requirements.txt
   ```

   Your `requirements.txt` should contain the following:

   ```
   pandas
   numpy
   faker
   ```

## Usage

To generate the datasets, run the `main.py` script with the desired parameters. Below is an example of how to execute the script:

```bash
python main.py
```

### Example of `main.py`

Here is an example of what your `main.py` file might look like:

```python
from factory_audit_data_generator import generate_factory_audit_and_contact_data  # Adjust the import as necessary

if __name__ == "__main__":
    # Generate datasets for the year 2023 with a default submission rate (75%) and 20 factories
    generate_factory_audit_and_contact_data(
        year=2023,
        submission_percentage=75,
        num_factories=50,
        audit_output_file='factory_audit_data.csv',
        contact_output_file='factory_contact_database.csv'
    )
```

Make sure to adjust the import statement based on the actual module name where the `generate_factory_audit_and_contact_data` function is defined.

## Functions

### `generate_factory_audit_and_contact_data`

- **Parameters:**
  - `year` (int): The year for which data is generated.
  - `submission_percentage` (int): The percentage of factories that submitted data.
  - `num_factories` (int): The number of factories to generate data for.
  - `audit_output_file` (str): The filename for the audit data CSV.
  - `contact_output_file` (str): The filename for the contact data CSV.

### Example Call

You can customize the parameters in `main.py` to suit your needs.

## License

This project is licensed under the MIT License. See the LICENSE file for details.