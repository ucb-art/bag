# Mock tech library for unit tests

This is a mock technology library with the bare minimum requirements to start BagProject. This is NOT meant to be a reference library and is only intended for use in unit testing. For examples of tech-specific plugins, see the Sky130 projects.

## Files
- `README.md`: this file
- `bag_libs.def`: list of available BAG libraries
- `cds.lib`: placeholder for OA libraries, required for OAInterface
- `bag_config.yaml`: configuration for BAG
- `tech_config.yaml`: describes basic physical parameters
- `corners_setup.yaml`: lists simulation files for different corners
- `templates_mock`: layout templates
    - `tech.py`: Main tech-specific layout plugin
    - `data/tech_params.yaml`: Parameters for tech drawing.
