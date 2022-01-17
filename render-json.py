import json


def main() -> None:
    write_vimium_options()
    return


def write_vimium_options() -> None:
    vimium_options_template_path = "vimium-options.template.json"

    key_mappings_path = "keyMappings.vim"
    search_engines_path = "searchEngines.properties"
    user_defined_link_hint_css_path = "userDefinedLinkHintCss.css"

    vimium_options_path = "vimium-options.json"

    with open(vimium_options_template_path, 'r') as vimium_options_template_file, \
            open(key_mappings_path, 'r') as key_mappings_file, \
            open(search_engines_path, 'r') as search_engines_file, \
            open(user_defined_link_hint_css_path, 'r') as user_defined_link_hint_css_file, \
            open(vimium_options_path, 'w') as vimium_options_file:

        vimium_options = json.load(vimium_options_template_file)

        vimium_options["keyMappings"] = key_mappings_file.read()
        vimium_options["searchEngines"] = search_engines_file.read()
        vimium_options["userDefinedLinkHintCss"] = user_defined_link_hint_css_file.read()

        json.dump(vimium_options, vimium_options_file, indent=2)

    return


if __name__ == "__main__":
    main()
