# - API Weeding

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
  
```shell
pip list
```

- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```
4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```


## Rodando os testes de cada tarefa isoladamente

Ao fim de cada tarefa será possível executar uma suite de testes direcionada àquela tarefa específica. Lembre-se de sempre estar com o **virtual enviroment (venv) ativado**.

- Rodando testes 1:
```python
pytest --testdox -vvs tests/tarefas/t1/
```

- Rodando testes 2:
```python
pytest --testdox -vvs tests/tarefas/t2/
```

- Rodando testes 3:
```python
pytest --testdox -vvs tests/tarefas/t3/
```

- Rodando testes 4:
```python
pytest --testdox -vvs tests/tarefas/t4/
```#   A P I - W e e d i n g 

- A Documentação poderá ser consultada após instalação de Pacotes com o comando: pip install -r  requirements.txt
Logo após a instalação o comando: python manage.py runserver  
Ao Rodar a API basta acessar o Link http://127.0.0.1:8000/api/docs/swagger-ui/ onde exibirá todas as Rotas.

A API não foi finalizada por completo devido a minha quantidade de tempo para desenvolver. 
Pontos de Melhora que eu gostaria de Implementar seria ao invés de ser só um album de fotos, poderia ser um album também de Videos,
onde seria possivel implementar microserviços adicionando RabbitMq e Go para upload mais rapidos e eficientes. 
Utilizei no Front End NextJs um Framework com SSR onde poderia ser um site bem mais Rápido e com atualizações de dados mais dinâmicas.
Finalizar a parte Funcional de Photos e Videos com a Validação dos Noivos.
Utilizei o SQlite para facilitar a execução da API. 

 
