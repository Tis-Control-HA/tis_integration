import os
import re
from ruamel.yaml import YAML
import logging


# ------ Security Settings Setup
def create():
    current_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(current_dir, "../../"))
    config_path = os.path.join(base_dir, "configuration.yaml")
    dashboard_filename = "tis_configuration.yaml"
    dashboard_path = os.path.join(base_dir, dashboard_filename)
    try:
        # YAML setup
        yaml = YAML()
        yaml.preserve_quotes = True

        # 1. Load configuration.yaml
        with open(config_path, "r") as f:
            config = yaml.load(f)

        # 2. Add dashboard if missing
        if "lovelace" not in config:
            config["lovelace"] = {}
        if "dashboards" not in config["lovelace"]:
            config["lovelace"]["dashboards"] = {}

        if "tis-configuration" not in config["lovelace"]["dashboards"]:
            config["lovelace"]["dashboards"]["tis-configuration"] = {
                "mode": "yaml",
                "title": "TIS Configuration",
                "icon": "mdi:tune",
                "show_in_sidebar": True,
                "filename": dashboard_filename,
                "require_admin": True,
            }

        if "panel_custom" not in config or config["panel_custom"] is None:
            config["panel_custom"] = []

        password_dashboard = {
            "name": "password-dashboard-loader",
            "sidebar_title": "My Passwords",
            "sidebar_icon": "mdi:lock-smart",
            "module_url": "/local/tis_assets/password_dashboard_loader.js?v=4.0.1",
            "require_admin": True,
            "url_path": "my-passwords",
        }

        def get_version_from_url(url_str):
            """Helper to extract version float/string from url parameters"""
            if not url_str:
                return [0, 0, 0]
            # Looks for v=X.X.X
            match = re.search(r"[?&]v=(\d+(?:\.\d+)*)", url_str)
            if match:
                # Convert "4.0.0" -> [4, 0, 0] for easy comparison
                return [int(x) for x in match.group(1).split(".")]
            return [0, 0, 0]

        # Logic to check existence and version
        if isinstance(config["panel_custom"], list):
            target_version = get_version_from_url(password_dashboard["module_url"])
            entry_index = -1

            # 1. Search for existing entry
            for idx, entry in enumerate(config["panel_custom"]):
                if entry.get("name") == password_dashboard["name"]:
                    entry_index = idx
                    break

            # 2. Update or Append
            if entry_index != -1:
                # Entry exists, check version
                existing_url = config["panel_custom"][entry_index].get("module_url", "")
                current_version = get_version_from_url(existing_url)

                # Compare lists of integers (e.g. [4, 1, 0] > [4, 0, 0])
                if target_version > current_version:
                    logging.info(
                        f"Upgrading Password Dashboard from {current_version} to {target_version}"
                    )
                    config["panel_custom"][entry_index] = password_dashboard
                else:
                    logging.info("Password Dashboard version is up to date.")
            else:
                # Entry does not exist, append it
                logging.info("Adding Password Dashboard to panel_custom.")
                config["panel_custom"].append(password_dashboard)

        # 3. Save configuration.yaml
        with open(config_path, "w") as f:
            yaml.dump(config, f)

        # 4. Create dashboard file if not exists
        if not os.path.exists(dashboard_path):
            dashboard_content = {
                "title": "YAML Dashboard",
                "views": [
                    {
                        "title": "TIS Configuration",
                        "path": "main",
                        "cards": [
                            {
                                "type": "button",
                                "name": "Change Lock Password",
                                "icon": "mdi:lock",
                                "tap_action": {
                                    "action": "url",
                                    "url_path": "http://homeassistant.local:8000/api/change-password",
                                },
                            },
                            {
                                "type": "button",
                                "name": "Tier Price",
                                "icon": "mdi:flash",
                                "tap_action": {
                                    "action": "url",
                                    "url_path": "http://homeassistant.local:8000/api/electricity-bill",
                                },
                            },
                        ],
                    }
                ],
            }
            with open(dashboard_path, "w") as f:
                yaml.dump(dashboard_content, f)
    except Exception as e:
        logging.error(f"Could Not Setup Security Settings Dashboard: {e}")
