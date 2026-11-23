CREATE TABLE IF NOT EXISTS pacotes (
    codigo_barras TEXT PRIMARY KEY,
    peso REAL NOT NULL,
    tamanho TEXT NOT NULL,
    fragil INTEGER NOT NULL
);

INSERT INTO pacotes (codigo_barras, peso, tamanho, fragil) VALUES
('BR-RIO-NIT-001', 2.0, 'pequeno', 0),
('EXPRESS-SP-042', 7.5, 'grande', 0),
('LOG-NIT-FRG-03', 1.5, 'pequeno', 1),
('CARGO-INT-999', 4.0, 'grande', 0),
('HUB-RIO-ESP-05', 8.0, 'pequeno', 1),
('BR-NIT-ICR-12', 3.0, 'pequeno', 0),
('EXPRESS-RJ-088', 6.0, 'grande', 0),
('LOG-RIO-FRG-09', 0.5, 'pequeno', 1),
('HUB-SP-LOG-10', 5.0, 'grande', 0),
('BR-RIO-ZS-015', 2.5, 'grande', 0);