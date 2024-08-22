import requests
import pandas as pd

df = pd.read_csv('modelos_fipe2.csv', encoding='utf-8')

final_results = []
initial_url = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarAnoModeloPeloCodigoFipe'
final_url = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros'
reference_table_code = 312
vehicle_type_code = 1


for index, row in df.iterrows():
    fipe_code = row['Código FIPE']
    
    initial_payload = {
        "codigoTipoVeiculo": vehicle_type_code,
        "codigoTabelaReferencia": reference_table_code,
        "modeloCodigoExterno": fipe_code
    }
    
    response = requests.post(initial_url, json=initial_payload)
    response_data = response.json()


    extractions = []
    for item in response_data:
        value = item['Value']
        model_year, fuel_code = value.split('-')
        extractions.append({
            "model_year": int(model_year),
            "fuel_code": int(fuel_code),
            "external_model_code": fipe_code
        })
    

    for extraction in extractions:
        final_payload = {
            "codigoTabelaReferencia": reference_table_code,
            "codigoTipoVeiculo": vehicle_type_code,
            "anoModelo": extraction['model_year'],
            "codigoTipoCombustivel": extraction['fuel_code'],
            "tipoVeiculo": "car",
            "modeloCodigoExterno": extraction['external_model_code'],
            "tipoConsulta": "codigo"
        }
        
        final_response = requests.post(final_url, json=final_payload)
        response = final_response.json()


        final_results.append({
            "value": response["Valor"],
            "brand": response["Marca"],
            "model": response["Modelo"],
            "model_year": response["AnoModelo"],
            "fuel_type": response["Combustivel"],
            "fipe_code": response["CodigoFipe"],
            "reference_month": response["MesReferencia"],
            "authentication": response["Autenticacao"],
            "vehicle_type": response["TipoVeiculo"],
            "fuel_abbreviation": response["SiglaCombustivel"],
            "query_date": response["DataConsulta"]
        })


df_final_results = pd.DataFrame(final_results)
df_final_results.to_csv('final_results.csv', index=False, encoding='utf-8')

print("Concluído")
