## 📘 Data Catalog


[en-us]
| Variable Name       | Role         | Variable Type     | Description                                                                 |
|---------------------|--------------|-------------------|-----------------------------------------------------------------------------|
| Flight Number       | Attribute    | Numeric           | Unique identifier for each launch attempt                                   |
| Date                | Attribute    | Date/Time         | Date of the launch                                                          |
| Booster Version     | Attribute    | Categorical       | Version/type of the rocket booster used                                     |
| Payload Mass        | Attribute    | Numeric           | Mass of the payload being delivered into orbit (in kilograms)               |
| Orbit               | Attribute    | Categorical       | Type of orbit for the payload (e.g., LEO, GTO)                              |
| Launch Site         | Attribute    | Categorical       | Location where the rocket was launched (e.g., Kennedy Space Center)         |
| Outcome             | Target       | Categorical       | Describes if the booster landing was successful or not                      |
| Flights             | Attribute    | Numeric           | Number of times the booster has flown                                       |
| Grid Fins           | Attribute    | Boolean           | Whether the booster had grid fins to help it land                           |
| Reused              | Attribute    | Boolean           | Indicates whether the booster had been used in a previous mission           |
| Legs                | Attribute    | Boolean           | Indicates whether the booster had landing legs                              |
| Landing Pad         | Attribute    | Categorical       | Specific location used for landing (e.g., drone ship or ground pad)         |
| Block               | Attribute    | Categorical       | Block number indicating major version of the booster                        |
| Reused Count        | Attribute    | Numeric           | Number of times a booster has been reused                                   |
| Serial              | Attribute    | Categorical       | Serial number of the booster                                                |
| Longitude           | Attribute    | Numeric           | Geographic longitude of the launch site                                     |
| Latitude            | Attribute    | Numeric           | Geographic latitude of the launch site                                      |
| Class               | Target       | Binary (0 or 1)   | Classification variable: 1 = successful landing, 0 = failed landing         |

---

[pt-br]
| Nome da Variável     | Função       | Tipo de Variável     | Descrição                                                                 |
|----------------------|--------------|-----------------------|--------------------------------------------------------------------------|
| Flight Number        | Atributo     | Numérica              | Identificador único para cada tentativa de lançamento                    |
| Date                 | Atributo     | Data/Hora             | Data do lançamento                                                       |
| Booster Version      | Atributo     | Categórica            | Versão/tipo do propulsor usado                                           |
| Payload Mass         | Atributo     | Numérica              | Massa da carga útil enviada à órbita (em quilogramas)                    |
| Orbit                | Atributo     | Categórica            | Tipo de órbita da carga útil (ex: LEO, GTO)                              |
| Launch Site          | Atributo     | Categórica            | Local de lançamento (ex: Kennedy Space Center)                           |
| Outcome              | Alvo         | Categórica            | Indica se o pouso do propulsor foi bem-sucedido ou não                   |
| Flights              | Atributo     | Numérica              | Número de voos realizados pelo propulsor                                 |
| Grid Fins            | Atributo     | Booleana              | Indica se o propulsor usava aletas direcionais para pouso                |
| Reused               | Atributo     | Booleana              | Indica se o propulsor já havia sido reutilizado                          |
| Legs                 | Atributo     | Booleana              | Indica se o propulsor possuía pernas de pouso                            |
| Landing Pad          | Atributo     | Categórica            | Local específico de pouso (ex: drone ship ou base terrestre)             |
| Block                | Atributo     | Categórica            | Número do bloco indicando a versão principal do propulsor                |
| Reused Count         | Atributo     | Numérica              | Número de vezes que o propulsor foi reutilizado                          |
| Serial               | Atributo     | Categórica            | Número de série do propulsor                                             |
| Longitude            | Atributo     | Numérica              | Longitude geográfica do local de lançamento                              |
| Latitude             | Atributo     | Numérica              | Latitude geográfica do local de lançamento                               |
| Class                | Alvo         | Binária (0 ou 1)      | Variável de classificação: 1 = pouso com sucesso, 0 = pouso mal-sucedido |
