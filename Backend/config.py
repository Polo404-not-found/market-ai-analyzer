import json
import os

CONFIG_FILE = "config.json"

class ConfigManager:

    @staticmethod 
    def save_api_key(api_key: str) -> None:
        api_key = api_key.strip()

        config_data = {
            "GEMINI_API_KEY": api_key
        }

        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as archive:
                json.dump(config_data, archive, indent=4)
        except Exception as e:
            print(f"Failed to save the Key {e}")

        os.environ["GEMINI_API_KEY"] = api_key

    @staticmethod 
    def load_api_key() -> str:
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as archive:
                    config_data = json.load(archive)
                    api_key = config_data.get("GEMINI_API_KEY", "").strip()

                    if api_key:
                        os.environ["GEMINI_API_KEY"] = api_key
                        return api_key

            except Exception as e:
                print(f"Failed to load API key {e}")
        return ""