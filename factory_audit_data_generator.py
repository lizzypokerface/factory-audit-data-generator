import logging
from faker import Faker
import pandas as pd
import numpy as np
import random
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def generate_factory_audit_and_contact_data(
    year,
    submission_percentage=75,
    num_factories=20,
    audit_output_file="factory_audit_data.csv",
    contact_output_file="factory_contact_database.csv",
):
    """
    Generates factory audit data and contact database for a given year, and exports them to CSV files.
    """

    logging.info("Initializing Faker and seeding random number generators.")
    # Initialize Faker
    fake = Faker()
    Faker.seed(0)
    np.random.seed(0)
    random.seed(0)

    logging.info("Defining regions and factory groups.")
    # Define regions and their corresponding countries (5 regions x 5 countries each)
    regions = {
        "North America": ["USA", "Canada", "Mexico", "Cuba", "Jamaica"],
        "Europe": ["Germany", "France", "Italy", "Spain", "United Kingdom"],
        "Asia": ["China", "India", "Japan", "South Korea", "Singapore"],
        "South America": ["Brazil", "Argentina", "Chile", "Peru", "Colombia"],
        "Africa": ["Nigeria", "Egypt", "South Africa", "Kenya", "Ghana"],
    }

    # Define factory groupings relevant to a sporting apparel company
    factory_groups = [
        "Footwear",
        "Athletic Apparel",
        "Sports Equipment",
        "Accessories",
        "Bags & Gear",
    ]

    logging.info("Generating unique factory codes and names.")
    # Generate unique factory codes
    factory_codes = [f"FC{str(i).zfill(4)}" for i in range(1, num_factories + 1)]
    # Generate factory names using Faker
    factory_names = [
        f"{fake.company()} {random.choice(['Inc.', 'Ltd.', 'LLC', 'Group'])}"
        for _ in range(num_factories)
    ]

    logging.info("Assigning factories to groups and regions.")
    # Assign each factory to a group and a region
    factory_group_assignments = random.choices(factory_groups, k=num_factories)
    factory_region_assignments = random.choices(list(regions.keys()), k=num_factories)

    logging.info("Determining factory countries based on regions.")
    # Assign each factory to a country based on its region
    factory_country_assignments = []
    for region in factory_region_assignments:
        country = random.choice(regions[region])
        factory_country_assignments.append(country)

    logging.info("Generating unique emails for each factory.")
    # Generate unique emails per factory
    factory_email1 = [fake.company_email() for _ in range(num_factories)]
    factory_email2 = [fake.company_email() for _ in range(num_factories)]

    logging.info("Creating DataFrames for contact and audit data.")
    # Create a DataFrame for factories (Contact Database)
    contact_df = pd.DataFrame(
        {
            "Factory Code": factory_codes,
            "Factory Group": factory_group_assignments,
            "Factory Name": factory_names,
            "Factory Email 1": factory_email1,
            "Factory Email 2": factory_email2,
        }
    )

    # Create a DataFrame for factories with additional info for audit data
    audit_factories_df = pd.DataFrame(
        {
            "Factory Code": factory_codes,
            "Factory Group": factory_group_assignments,
            "Factory Name": factory_names,
            "Region": factory_region_assignments,
            "Country": factory_country_assignments,
        }
    )

    logging.info("Generating periods for the specified year.")
    # Generate list of periods (months) for the specified year
    periods = [datetime(year, month, 1) for month in range(1, 13)]

    logging.info("Collecting audit records.")
    # Prepare list to collect all audit records
    audit_records = []

    for idx, factory in audit_factories_df.iterrows():
        for period in periods:
            # Determine if the audit was submitted based on submission_percentage
            submitted = random.uniform(0, 100) < submission_percentage
            if submitted:
                status = "Submitted"
                # Generate compliance score (50-100)
                compliance_score = random.randint(50, 100)
                # Generate a random verification date within the month (1-28 to avoid month-end issues)
                day = random.randint(1, 28)
                verification_date = datetime(year, period.month, day).strftime(
                    "%Y-%m-%d"
                )
            else:
                status = "Not Submitted"
                compliance_score = np.nan
                verification_date = ""

            # Format period as 'Jan 2023', 'Feb 2023', etc.
            period_formatted = period.strftime("%b %Y")

            # Determine Pass/Fail based on compliance score
            if pd.notna(compliance_score):
                pass_fail = "Pass" if compliance_score >= 70 else "Fail"
            else:
                pass_fail = ""

            # Append the audit record
            audit_records.append(
                {
                    "Factory Code": factory["Factory Code"],
                    "Factory Group": factory["Factory Group"],
                    "Factory Name": factory["Factory Name"],
                    "Region": factory["Region"],
                    "Country": factory["Country"],
                    "Period": period_formatted,
                    "Status": status,
                    "Compliance Score": compliance_score,
                    "Pass/Fail": pass_fail,
                    "Verification Date": verification_date,
                }
            )

    logging.info("Creating DataFrame from audit records.")
    # Create DataFrame from audit records
    audit_df = pd.DataFrame(audit_records)

    logging.info("Sorting the audit DataFrame.")
    # Optional: Sort the DataFrame by Factory Code and Period
    audit_df["Period_Sort"] = pd.to_datetime(audit_df["Period"], format="%b %Y")
    audit_df.sort_values(["Factory Code", "Period_Sort"], inplace=True)
    audit_df.drop(columns=["Period_Sort"], inplace=True)
    audit_df.reset_index(drop=True, inplace=True)

    logging.info(f"Exporting audit data to '{audit_output_file}'.")
    # Export Audit Data to CSV
    audit_df.to_csv(audit_output_file, index=False)

    logging.info(f"Exporting contact database to '{contact_output_file}'.")
    # Export Contact Database to CSV
    contact_df.to_csv(contact_output_file, index=False)

    logging.info("Data generation completed successfully.")
    logging.info(
        f"Factory audit dataset generated successfully and saved to '{audit_output_file}'!"
    )
    logging.info(
        f"Contact database generated successfully and saved to '{contact_output_file}'!"
    )
