import json 
import os 

config_file = "config.json"

class ConfigManager:

    @staticmethod 
    def save_api_key(api_key: str) -> None:
        api_key = api_key.strip()

        datos = {
            "GEMINI_API_KEY": api_key
        }

        try:
            with open(config_file, "w", encoding="utf-8") as archive:
                json.dump(datos, archive, indent=4)
        except Exception as e:
            print(f"Failed to save the Key {e}")

        os.environ["GEMINI_API_KEY"] = api_key

    @staticmethod 
    def load_api_key() -> str:
        if os.path.exists(config_file):
            try:
                with open(config_file, "r", encoding="utf-8") as archive:
                    datos = json.load(archive)
                    api_key = datos.get("GEMINI_API_KEY", "").strip()

                    if api_key:
                        os.environ["GEMINI_API_KEY"] = api_key
                        return api_key

            except Exception as e:
                print(f"Failed to load API key {e}")
        return ""