# Sistema de busca e recomendação de cursos (UFPB) — v5

Protótipo acadêmico: **interface web em Python/Flask** com **base lógica em Prolog** (SWI-Prolog), via **PySwip**. O motor declarativo concentra fatos (`cursos.pl`) e regras (`regras.pl`); a aplicação monta consultas, ranqueia por interesses e exibe resultados.

## Requisitos

- Python 3.10+ (recomendado)
- [SWI-Prolog](https://www.swi-prolog.org/) instalado e no `PATH` (Windows: marque a opção de adicionar ao PATH na instalação)
- Dependências Python: `pip install -r requirements.txt`

## Como executar

```bash
cd caminho/do/projeto
pip install -r requirements.txt
python app.py
```

Abra `http://127.0.0.1:5000/` para a busca e `http://127.0.0.1:5000/comparar` para o comparador de dois cursos.

No modo desenvolvimento o servidor usa `threaded=False` por estabilidade do PySwip.

> **⚠️ Limitação de thread-safety (importante para produção)**
> O PySwip compartilha uma única instância do motor SWI-Prolog por processo e **não é thread-safe**.
> Execute sempre com um único worker e **sem** multi-threading (Gunicorn: `--workers 1 --threads 1`).
> Requisições concorrentes via múltiplas threads **podem causar crashes** no motor Prolog.

## Testes

**Python (pytest):**

```bash
pytest
```

**Prolog (consistência da base), a partir da pasta `prolog`:**

```bash
cd prolog
swipl -q -g "consult(kb_tests), run_tests(knowledge_base), halt" -t halt
```

## Estrutura principal

| Artefato | Papel |
|----------|--------|
| `prolog/cursos.pl` | Fatos dos cursos (área, turno, campus, `indicado_para/2`, etc.) |
| `prolog/regras.pl` | Regras (`score_interesses`, similaridade em camadas, classificações auxiliares) |
| `prolog/main.pl` | Carrega `cursos.pl` e `regras.pl` |
| `prolog/kb_tests.pl` | Testes PlUnit de integridade da base |
| `app.py` | Flask, ponte PySwip, busca, comparador, enriquecimento da UI |
| `form_query.py` | Montagem de queries atômicas e parsing do formulário |

Os dados de nota de corte e carga horária são **referência/simulação** para demonstração; não substituem editais oficiais.

## Escopo

Subconjunto de cursos da UFPB para fins de projeto e artigo; a modelagem e a integração Prolog ↔ Python são o foco central.
