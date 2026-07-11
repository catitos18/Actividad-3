import json
import yaml

def main():
   
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

   
    nuevo_puerto = {
        "id": 4,
        "nombre": "GigabitEthernet0/3",
        "estado": "down",
        "velocidad": "1Gbps",
        "descripcion": "Nuevo puerto agregado"
    }

    datos["puertos"].append(nuevo_puerto)

    
    with open("datos_modificado.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    
    with open("datos.yaml", "w", encoding="utf-8") as archivo:
        yaml.dump(datos, archivo, allow_unicode=True, sort_keys=False)

    print("Archivos creados correctamente:")
    print("- datos_modificado.json")
    print("- datos.yaml")


if __name__ == "__main__":
    main()
