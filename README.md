# 🍝 Restaurant Orders — Gestão Dinâmica de Cardápios e Controle de Estoque

O **Restaurant Orders** é uma aplicação em Python focada na modernização das ferramentas de backend do restaurante *Chapa Quente*. O objetivo principal do projeto foi substituir um fluxo ineficiente baseado em planilhas CSV estáticas por uma arquitetura robusta e dinâmica orientada a objetos, capaz de gerar cardápios personalizados de acordo com restrições alimentares e gerenciar a disponibilidade de estoque em tempo real.

O motor da aplicação foi integrado com o **FastAPI**, disponibilizando rotas mapeadas para consumo dinâmico.

---

## 🚀 Habilidades Desenvolvidas & Consolidadas

Este projeto consolidou conceitos de Otimização de Algoritmos, Estruturas de Dados e Testes Avançados em Python:

* **Domínio de Hashmaps (`Dict` e `Set`):**
    * Utilização de conjuntos (`Set`) para garantir a unicidade de pratos e restrições alimentares, eliminando redundâncias nas leituras de arquivos CSV estruturados em tabelas dinâmicas de relacionamento muitos-para-muitos.
    * Mapeamento de receitas através de dicionários (`Dict`), atrelando ingredientes (`Ingredient`) às suas respectivas proporções/quantidades numéricas para otimização do cálculo de estoque.
* **Consistência de Estados em POO (Métodos Mágicos):**
    * Validação prática de hashing de objetos através da sobrescrita dos métodos `__hash__`, `__eq__` e `__repr__`, garantindo integridade posicional e comparativa na memória.
* **Lógica de Filtros e Agrupamentos Complexos:**
    * Cruzamento matricial de dados para gerar cardápios filtrados por exclusão de restrições alimentares e verificação de dependências de insumos.
* **Controle Transacional de Estoque:**
    * Implementação de rotas lógicas de checagem prévia (`check_recipe_availability`) e consumo atômico (`consume_recipe`), blindando o sistema contra quebras de estoque e levantando exceções adequadas (`ValueError`).
* **Testes de Software Baseados em Mutação e Comportamento:**
    * Criação de suítes de testes automatizados com o framework **Pytest**, simulando cenários que esperavam falhas controladas (*XFAIL*) para atestar a estabilidade estrutural das instâncias contra tipos de dados inválidos (`TypeError`).

---

## 📁 Arquitetura dos Módulos Desenvolvidos

A estrutura lógica foi modelada para garantir separação de conceitos através de classes de modelos e serviços:

### 1. Camada de Modelos (`src/models/`)
* **`ingredient.py`**: Representação de insumos individuais mapeados por nome e suas respectivas tabelas de restrições alérgicas (Ex: Lactose, Glúten, Derivados Animais).
* **`dish.py`**: Definição dos pratos da casa, seus respectivos valores comerciais e a sua receita matemática (ingredientes necessários).

### 2. Camada de Serviços (`src/services/`)
* **`menu_data.py`**: Módulo transacional que lê os arquivos CSV brutos da pasta `data/` e instancia automaticamente os relacionamentos de objetos complexos na memória.
* **`menu_builder.py`**: Gerador dinâmico de cardápio focado na experiência do usuário, omitindo opções indisponíveis ou proibidas por dietas restritivas.
* **`inventory_control.py`**: Motor de auditoria interna e baixa do estoque físico do estabelecimento.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem Principal:** Python 3 (v3.8+)
* **Framework Web Integrado:** FastAPI / Uvicorn
* **Framework de Testes:** Pytest
* **Linter Estático:** Flake8 (PEP 8)

---

## 🏕️ Configuração do Ambiente e Execução

### 1. Preparando o Ambiente Virtual

```bash
# Criar o ambiente virtual (.venv)
python3 -m venv .venv

# Ativar o ambiente virtual
source .venv/bin/activate

# Instalar as dependências de desenvolvimento
python3 -m pip install -r dev-requirements.txt
```

### 2. Executando os testes automatizados

Para certificar-se da integridade dos hashing, comparadores lógicos e métodos transacionais:

```bash
python3 -m pytest
python3 -m pytest -x
```

### 3. Rodando o servidor localmente (fastapi)

Para subir a aplicação integrada com a interface dinâmica e visualizar a documentação gerada de forma automatizada:

```bash
python3 -m uvcorn app:app
```

Após executar, acesse a interface interativa do swagger em: http://127.0.0.1:8000/docs

### Estrutura do repositório

```text
├── data/
│   ├── inventory_base_data.csv   # Histórico de estoque inicial do restaurante
│   └── menu_base_data.csv        # Tabela com as composições das receitas
├── src/
│   ├── models/                   # Definição e regras de negócio das entidades
│   └── services/                 # Motores de geração de cardápio e estoque
└── tests/                        # Casos de teste estruturais (Dish e Ingredient)
```
