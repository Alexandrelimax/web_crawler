import requests
from config import ConnectionPostgres
from repository import VehicleRepository
from utils.format_response import format_value



def extract_by_brand():

    url = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas'

    payload = {
        "codigoTabelaReferencia": 312,
        "codigoTipoVeiculo": 1,
        "anoModelo": 2008,
        "codigoTipoCombustivel": 1,
        "tipoVeiculo": "carro",
        "modeloCodigoExterno": "024112-1",
        "tipoConsulta": "codigo"
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()
        
        connection = ConnectionPostgres()
        repository = VehicleRepository(connection)

        
        brand_data = {
            "valor": format_value(data['Valor']),
            "marca": data["Marca"],
            "modelo": data["Modelo"],
            "ano_modelo": str(data["AnoModelo"]),
            "combustivel": data["Combustivel"],
            "codigo_fipe": data["CodigoFipe"],
            "mes_referencia": data["MesReferencia"].strip(),
            "autenticacao": data["Autenticacao"],
            "tipo_veiculo": str(data["TipoVeiculo"]),
            "sigla_combustivel": data["SiglaCombustivel"],
            "data_consulta": data["DataConsulta"]
        }

        repository.insert(brand_data)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if connection:
            connection.close()








def entrypoint():
    url = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros'

    payload = {
        "codigoTabelaReferencia": 312,
        "codigoTipoVeiculo": 1,
        "anoModelo": 2008,
        "codigoTipoCombustivel": 1,
        "tipoVeiculo": "carro",
        "modeloCodigoExterno": "024112-1",
        "tipoConsulta": "codigo"
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()

        connection = ConnectionPostgres()
        repository = VehicleRepository(connection)

        vehicle_data = {
            "valor": format_value(data['Valor']),
            "marca": data["Marca"],
            "modelo": data["Modelo"],
            "ano_modelo": str(data["AnoModelo"]),
            "combustivel": data["Combustivel"],
            "codigo_fipe": data["CodigoFipe"],
            "mes_referencia": data["MesReferencia"].strip(),
            "autenticacao": data["Autenticacao"],
            "tipo_veiculo": str(data["TipoVeiculo"]),
            "sigla_combustivel": data["SiglaCombustivel"],
            "data_consulta": data["DataConsulta"]
        }

        repository.insert(vehicle_data)
        print("Dados inseridos com sucesso!")
        
    except Exception as e:
        print(f"Error: {e}")

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    entrypoint()