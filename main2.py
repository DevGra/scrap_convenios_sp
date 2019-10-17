from bs4 import BeautifulSoup as bs
import requests
import json
import urllib
import csv

base_url = 'http://www.portaltransparencia.gov.br/convenios/consulta?paginacaoSimples=true&tamanhoPagina=&offset=&direcaoOrdenacao=asc'
# ------ modelo----------
# periodoVigenciaDe=01%2F01%2F2015&
# periodoVigenciaAte=31%2F12%2F2018&
# orgaos=OR25000&
# uf=SP&
# colunasSelecionadas=linkDetalhamento%2CnumeroConvenio%2CnumeroOriginal%2Cuf%2CmunicipioConvenente%2Csituacao%2CtipoTransferencia%2Cobjetivo%2CorgaoSuperior%2Corgao%2Cconcedente%2Cconvenente%2CdataInicioVigencia%2CdataFimVigencia%2CvalorCelebrado&
# ordenarPor=orgao&
# direcao=desc
#----------------------------------

# ------ funcao que retorna a data formatada do link
def convert_data(data):
    dt_final = ''
    data = str(data)
    for letra in data:
        if '/' in letra:
            letra = '%2F'
        dt_final = dt_final + letra
    return dt_final

# ---------------- montagem da URL do site ------------
data_de = '01/01/2015'
data_ate = '31/12/2018'
periodoVigenciaDe = convert_data(data_de)
periodoVigenciaAte = convert_data(data_ate)
codigo_orgao = 'OR25000'

# ------ PEGAR OS CODIGOS DOS ORGAOS E CRIAR UM FOR AQUI PARA PERCORRER A LISTA DE CODIGO DO ORGAOS

orgaos = codigo_orgao
uf = 'SP'
colunasSelecionadas = 'linkDetalhamento%2CnumeroConvenio%2CnumeroOriginal%2Cuf%2CmunicipioConvenente%2Csituacao%2CtipoTransferencia%2Cobjetivo%2CorgaoSuperior%2Corgao%2Cconcedente%2Cconvenente%2CdataInicioVigencia%2CdataFimVigencia%2CvalorCelebrado'
ordenarPor = 'orgao'
direcao = 'desc'

full_url = base_url+'&periodoVigenciaDe='+periodoVigenciaDe+ \
    '&periodoVigenciaAte='+periodoVigenciaAte+ \
    '&orgaos='+orgaos+ \
    '&uf='+uf+ \
    '&colunasSelecionadas='+colunasSelecionadas+ \
    '&ordenarPor='+ordenarPor+ \
    '&direcao='+direcao
#print(full_url)

# -------------------- montagem do link do ajax ---------------
def ajax_principal(offset_size):
    # -- para a paginacao o offset varia de acordo com a qtde de itens por pg
    # -- comeca em 0 e se a qtde de itens exibidos for de 50 por pg, o offset
    # -- vai de 50 em 50 ate a ultima pg, por isso foi criado o iterator.

    offset_size = str(offset_size)
    base_ajax = 'http://www.portaltransparencia.gov.br/convenios/consulta/resultado?'
    paginacao_simples_ajax = 'paginacaoSimples=false&'
    tamanhao_pg_ajax = 'tamanhoPagina=50&'
    offset_ajax = 'offset='+offset_size+'&'
    direcao_ordenacao_ajax = 'direcaoOrdenacao=desc&'
    coluna_ordenacao_ajax = 'colunaOrdenacao=orgao&'
    periodo_vigencia_de_ajax = 'periodoVigenciaDe='+periodoVigenciaDe+'&'
    periodo_vigencia_ate_ajax = 'periodoVigenciaAte='+periodoVigenciaAte+'&'
    orgaos_ajax = 'orgaos='+orgaos+'&'
    uf_ajax = 'uf='+uf+'&'
    colunas_sel = 'colunasSelecionadas=linkDetalhamento%2CnumeroConvenio%2CnumeroOriginal%2Cuf%2CmunicipioConvenente%2Csituacao%2CtipoTransferencia%2Cobjetivo%2CorgaoSuperior%2Corgao%2Cconcedente%2Cconvenente%2CdataInicioVigencia%2CdataFimVigencia%2CvalorCelebrado&'
    codigo = '*'
    codigo_ajax = '_=' + codigo

    ajax_full_url = base_ajax + paginacao_simples_ajax + tamanhao_pg_ajax + offset_ajax + direcao_ordenacao_ajax +\
        coluna_ordenacao_ajax + periodo_vigencia_de_ajax + periodo_vigencia_ate_ajax + orgaos_ajax + \
        uf_ajax + colunas_sel + codigo_ajax

    # --------------------------------------

    ajax_url = ajax_full_url
    page_url = full_url

    data_ajax = {'paginacaoSimples':'true','tamanhoPagina':'50', 'offset': offset_size,'direcaoOrdenacao':'desc', \
        'colunaOrdenacao':'orgao', 'periodoVigenciaDe': data_de, 'periodoVigenciaAte': data_ate, 'orgaos': orgaos, \
            'uf': uf, 'colunasSelecionadas': 'linkDetalhamento,numeroConvenio,numeroOriginal,uf,municipioConvenente,situacao,tipoTransferencia,objetivo,orgaoSuperior,orgao,concedente,convenente,dataInicioVigencia,dataFimVigencia,valorCelebrado', \
                '_': codigo
    }

    customHead = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Cookie": "_ga=GA1.3.1701369779.1558824505; _gid=GA1.3.1013749662.1558824505; _gat_gtag_UA_1665737_25=1; JSESSIONID=xHjOUSMPY0wI8qLUTuwlpe95rLbOGVoM70OSSUGv.idc-jboss2-ap2-p",
            "DNT": "1",
            "Host": "www.portaltransparencia.gov.br",
            "Referer": "http://www.portaltransparencia.gov.br/convenios/consulta?paginacaoSimples=true&tamanhoPagina=&offset=&direcaoOrdenacao=asc&periodoVigenciaDe=01%2F01%2F2015&periodoVigenciaAte=31%2F12%2F2018&orgaos=OR25000&uf=SP&colunasSelecionadas=linkDetalhamento%2CnumeroConvenio%2CnumeroOriginal%2Cuf%2CmunicipioConvenente%2Csituacao%2CtipoTransferencia%2Cobjetivo%2CorgaoSuperior%2Corgao%2Cconcedente%2Cconvenente%2CdataInicioVigencia%2CdataFimVigencia%2CvalorCelebrado&ordenarPor=orgao&direcao=desc",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

    ajax_response = requests.get(ajax_url, headers=customHead, data=data_ajax)
    dict_convenio = json.loads(ajax_response.content)
    return dict_convenio
    # --------------------   fim da funcao ajax principal -----------

# -----  Funcao para consultar os detalhes de cada convenio - ordem de pagamento
def ajax_detalhar(num_convenio = 0):

    base_ajax_detalhe = 'http://www.portaltransparencia.gov.br/convenios/'+num_convenio+'/valores-liberados/resultado?'
    paginacao_simples_ajax = 'paginacaoSimples=true&'
    tamanhao_pg_ajax = 'tamanhoPagina=50&'
    offset_ajax = 'offset=0&'
    direcao_ordenacao_ajax = 'direcaoOrdenacao=desc&'
    coluna_ordenacao_ajax = 'colunaOrdenacao=data&'
    colunas_sel = 'colunasSelecionadas=detalhar%2Cdata%2Cdocumento%2Cvalor&'
    codigo = '*'
    codigo_ajax = '_=' + codigo

    ajax_full_url = base_ajax_detalhe + paginacao_simples_ajax + tamanhao_pg_ajax + offset_ajax + direcao_ordenacao_ajax +\
        coluna_ordenacao_ajax +  colunas_sel + codigo_ajax


    ajax_url_detalhe = ajax_full_url

    data_ajax = {'paginacaoSimples':'true','tamanhoPagina':'50', 'offset':'0','direcaoOrdenacao':'desc', \
        'colunaOrdenacao':'data', 'colunasSelecionadas': 'detalhar,data,documento,valor', '_': codigo
    }

    customHead = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Host": "www.portaltransparencia.gov.br",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

    ajax_response = requests.get(ajax_url_detalhe, headers=customHead, data=data_ajax)
    dict_convenio_detalhes = json.loads(ajax_response.content)

    return dict_convenio_detalhes
# ---------------  FIM da funcao --------------------------------

i = 1
# variavel usada para requisicao ajax se houve paginacao, eh passada 0 - primeira,
# a partir disso, eh passda de 50 em 50, pq é a exibicao escolhida de itens por pg.
offset_size = 0
nome_arquivo = codigo_orgao + '.csv'
while True:
    ajax_pg_main = ajax_principal(offset_size)
    # ------------- codigo aqui --------------
    #import pdb; pdb.set_trace()
    if ajax_pg_main['data']:
        data = ajax_pg_main['data']
        colunas = dict(data[0])
        nm_columns = ''

        # try:
        with open(nome_arquivo, 'w') as f:
            if  i == 1:
                # pega o nome das colunas em data
                nm_columns = colunas.keys()
                nm_columns = list(nm_columns)
                nm_columns.extend(('ValorTotal', 'Valor_2018'))
                #nm_columns.append('ValorTotal')
                #import pdb; pdb.set_trace()
                writer = csv.DictWriter(f, fieldnames=nm_columns)
                writer.writeheader()

            valor_total = 0
            valor_por_ano = 0
            data_ano = ''
            data_padrao = '2018'
            valores = 0

            for value in data:
                # --------- VALORES DETALHADOS DE CADA CONVENIO ---------
                tb_detalhes = ajax_detalhar(value['numConvenio'])
                print(value['numConvenio'])
                #import pdb; pdb.set_trace()

                if tb_detalhes['data']:
                    data_detalhe = tb_detalhes['data'][0]['data']
                    for campo in tb_detalhes['data']:
                        print(type(campo['valor']))
                        print(type(valor_total))

                        #import pdb; pdb.set_trace()
                        valor_total += int(campo['valor'].replace(".","").split(",")[0])
                        #import pdb; pdb.set_trace()
                        data_ano = (campo['data']).split("/")[2]
                        if data_ano == data_padrao:
                            valores += int(campo['valor'].replace(".","").split(",")[0])
                        else:
                            valores = 0

                else:

                    valor_total = 0

                value.update({'ValorTotal': valor_total, 'Valor_2018': valores })

                writer.writerow(value)
                print("FIM DA GRAVACAO DA LINHA DE CONVENIO")

    # -------------- fim codigo --------------
    #import pdb; pdb.set_trace()
    # verifica se a primera pagina exibe 50 itens, se sim, continua o loop.
    if len(ajax_pg_main['data']) == 50:
        i += 1
        # pq eh 50 por pagina
        offset_size += 50
        continue
    else:
        break
exit()
print("FIM DA GRAVACAO DO ARQUIVO!")
