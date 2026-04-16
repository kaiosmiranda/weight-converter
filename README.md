# weight-converter

Conversor de unidades de massa desenvolvido em Python.

## O que faz

Recebe um valor de peso e a unidade informada pelo usuário (kg ou lbs) e retorna o valor convertido para a outra unidade.

## Como usar

```bash
python weight_converter.py
```

Exemplo de execução:

```
Weight: 170
(K)g or (L)bs: l
Weight in Kg: 76.5
```

## Entradas aceitas

| Entrada | Significado | Resultado |
|--------|-------------|-----------|
| `k` ou `K` | O valor está em lbs | Converte para kg |
| `l` ou `L` | O valor está em kg | Converte para lbs |

## Fórmulas utilizadas

- **lbs → kg:** `peso × 0.450`
- **kg → lbs:** `peso ÷ 0.450`

## Conceitos aplicados

- Variáveis e tipos de dados
- Conversão de tipos (`float`)
- Entrada do usuário (`input`)
- Normalização de string (`.lower()`)
- Condicionais (`if / elif / else`)

## Melhorias futuras

- [ ] Tratamento de erros para entradas inválidas (`try/except`)
- [ ] Suporte a outras unidades (gramas, toneladas)
- [ ] Interface via linha de comando com argumentos (`argparse`)

## Status

`v1.0` — funcional. Melhorias planejadas conforme avanço no currículo de Python.