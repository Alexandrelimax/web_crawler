CREATE TABLE vehicle (
    id SERIAL PRIMARY KEY,
    value VARCHAR(20) NOT NULL,         
    brand VARCHAR(50) NOT NULL,                 
    model VARCHAR(100) NOT NULL,           
    model_year INTEGER NOT NULL,            
    fuel_type VARCHAR(20) NOT NULL,            
    fipe_code VARCHAR(20) NOT NULL,               
    reference_month VARCHAR(20) NOT NULL,       
    authentication VARCHAR(100) NOT NULL,   
    vehicle_type INTEGER NOT NULL,                
    fuel_abbreviation VARCHAR(10) NOT NULL,      
    created_at TIMESTAMP NOT NULL                 
);