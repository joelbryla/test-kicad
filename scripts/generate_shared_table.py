from pathlib import Path


def create_shared_footprint_table(projects):
    entries = "\n".join(
        [
            f'	(lib (name "{project_name}") (type "KiCad") (uri "${{KIPRJMOD}}/../{project_name}/{project_name}.pretty") (options "") (descr ""))'
            for project_name in projects
        ]
    )

    return f"""(fp_lib_table
	(version 7)
	(lib (name "Shared Library") (type "KiCad") (uri "${{KIPRJMOD}}/../../Shared Library/Footprints") (options "") (descr ""))
{entries}
)
"""


def create_shared_symbol_table(projects):
    entries = "\n".join(
        [
            f'	(lib (name "{project_name}") (type "KiCad") (uri "${{KIPRJMOD}}/../{project_name}/") (options "") (descr ""))'
            for project_name in projects
        ]
    )

    return f"""(sym_lib_table
	(version 7)
	(lib (name "Shared Library") (type "KiCad") (uri "${{KIPRJMOD}}/../../Shared Library/Symbols") (options "") (descr ""))
{entries}
)
"""


project_directory = Path("Projects")
projects = [f.name for f in project_directory.iterdir() if f.is_dir()]

with open("Shared Library/shared-fp-lib-table", "w") as f:
    f.write(create_shared_footprint_table(projects))

with open("Shared Library/shared-sym-lib-table", "w") as f:
    f.write(create_shared_symbol_table(projects))
