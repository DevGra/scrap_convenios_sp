from bs4 import BeautifulSoup as bs
import requests

base_url = 'https://startupbase.abstartups.com.br/startups?hitsPerPage=80&page='
str_url = '&hierarchicalMenu%5Blocation.state%5D%5B0%5D=SP'
i = 1
while i <= 42:
    page_url = base_url + str(i) + str_url
    print(page_url)
    pagina  = requests.get(page_url)
    soup = bs(pagina.content, "html.parser")
    import pdb; pdb.set_trace()
    div_conteiner_links = soup.find('div', {'class':'col-12'}).find('div', {'class': 'row cards-list no-gutters'})
    import pdb; pdb.set_trace()
    i += 1
    # self.br_colunas = []
    # #import pdb; pdb.set_trace()
    # self.ajax_url = 'http://shedar.fapesp.br:9002/pt/data_graphics/'
    # self.page_url = 'http://shedar.fapesp.br:9002/pt/acordo-convenio'
    # qs = ''
    # if query == 'aplicacao_exact':
    #     qs = 'aplicacao_exact:"Pesquisa Inovativa em Pequenas Empresas (PIPE)" OR aplicacao_exact:"PAPPE-PIPE III"'
    # else:
    #     qs = '('+query+':*)'
    #
    # data_ajax = {'q':qs,'fq':'*:*', 'selected_facets':'[]','grafico':'groupedbar', 'csrfmiddlewaretoken':'V7iAECznHstbMSmITOgQom3EIkP3ZLxf'}
    # customHead = {'Accept': 'application/json, text/javascript, */*; q=0.01',
    #     'Cookie': 'csrftoken=V7iAECznHstbMSmITOgQom3EIkP3ZLxf; _ga=GA1.2.1452929270.1544619393; __utma=249330960.1452929270.1544619393.1544793023.1547568161.2; __utmz=249330960.1547568161.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _gid=GA1.2.1322267330.1554830968; sc_is_visitor_unique=rx11601073.1554904039.E891D8C48E2C4F052AA9593303F4EEE8.2.2.2.2.2.2.1.1.1; _gat=1; _gat_UA-2957958-1=1; __atuvc=13%7C13%2C20%7C14%2C40%7C15; __atuvs=5caf4783218b1f1f000',
    #     'X-Requested-With': 'XMLHttpRequest',
    #     'Referer': self.page_url
    #     }
    #
    # ajax_response = requests.post(self.ajax_url, headers=customHead, data=data_ajax).json()
    # self.br_colunas = ajax_response['format_compatible']
    #
    # i += 1
