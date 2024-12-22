from factory_audit_data_generator import generate_factory_audit_and_contact_data

if __name__ == "__main__":
    # Generate datasets for the year 2023 with a default submission rate (75%) and 20 factories
    generate_factory_audit_and_contact_data(
        year=2023,
        submission_percentage=75,
        num_factories=50,
        audit_output_file="factory_audit_data.csv",
        contact_output_file="factory_contact_database.csv",
    )
