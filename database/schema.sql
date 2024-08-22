CREATE TABLE vehicle_reference (
    id SERIAL PRIMARY KEY,
    codigoTabelaReferencia CHAR(3) NOT NULL,
    codigoTipoVeiculo CHAR(1) NOT NULL,
    anoModelo INTEGER NOT NULL,
    codigoTipoCombustivel CHAR(1) NOT NULL,
    tipoVeiculo VARCHAR(50) NOT NULL,
    modeloCodigoExterno VARCHAR(20) NOT NULL,
    tipoConsulta VARCHAR(20) NOT NULL
);


CREATE TABLE vehicle_detalhes (
    id SERIAL PRIMARY KEY,
    vehicle_reference_id INTEGER NOT NULL REFERENCES vehicle_reference(id),
    Valor VARCHAR(20) NOT NULL,
    Marca VARCHAR(50) NOT NULL,
    Modelo VARCHAR(100) NOT NULL,
    AnoModelo INTEGER NOT NULL,
    Combustivel VARCHAR(20) NOT NULL,
    CodigoFipe VARCHAR(20) NOT NULL,
    MesReferencia VARCHAR(20) NOT NULL,
    Autenticacao VARCHAR(50) NOT NULL,
    TipoVeiculo CHAR(1) NOT NULL,
    SiglaCombustivel CHAR(1) NOT NULL,
    DataConsulta TIMESTAMP NOT NULL
);
