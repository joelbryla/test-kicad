import shutil
from pathlib import Path


def create_new_project(project_name):
    target_dir = Path(f"Projects/{project_name}")
    replacements = {
        "{{PROJECT_NAME}}": project_name,
    }

    shutil.unpack_archive("PROJECT_TEMPLATE.zip", "Projects/")
    shutil.move("Projects/PROJECT_TEMPLATE", target_dir)

    for file_path in target_dir.rglob("*"):
        new_name = file_path.name
        for key, val in replacements.items():
            new_name = new_name.replace(key, val)
        file_path = file_path.rename(file_path.with_name(new_name))

        if file_path.is_file():
            # Rename files if placeholders are in the filename
            new_name = file_path.name
            for key, val in replacements.items():
                new_name = new_name.replace(key, val)
            file_path = file_path.rename(file_path.with_name(new_name))

            # Replace placeholders inside text files
            try:
                content = file_path.read_text(encoding="utf-8")
                for key, val in replacements.items():
                    content = content.replace(key, val)
                file_path.write_text(content, encoding="utf-8")
            except UnicodeDecodeError:
                pass  # Skip binary files like images


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("project_name")
    args = parser.parse_args()
    create_new_project(args.project_name)

    # update shared table after creating
    import generate_shared_table

    _ = generate_shared_table
