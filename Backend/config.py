import json 
import os 

config_file = "config.json"

class ConfigManager:

    @staticmethod 
    def guardar_api_key(api_key: str) -> None:
        api_key = api_key.strip()

        datos = {
            "GEMINI_API_KEY": api_key
        }

        try:
            with open(config_file, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar la API key {e}")

        os.environ["GEMINI_API_KEY"] = api_key

    @staticmethod 
    def cargar_api_key() -> str:
        if os.path.exists(config_file):
            try:
                with open(config_file, "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
                    api_key = datos.get("GEMINI_API_KEY", "").strip()

                    if api_key:
                        os.environ["GEMINI_API_KEY"] = api_key
                        return api_key

            except Exception as e:
                print(f"Error al cargar la API key: {e}")
        return ""