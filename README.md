</br>
<h2>O que é JoinExcel.py</h2>
<p>O JoinExcel é uma ferramenta desenvolvida para facilitar a realização de operações de junção (join) entre dois arquivos Excel. Com essa aplicação, é possível combinar informações de duas planilhas diferentes com base em uma coluna em comum, de acordo com diferentes tipos de joins disponíveis. Para utilizar o programa, siga o guia passo a passo abaixo:</p>
</br>
<p><strong><h2>Passo 1: Carregando os arquivos Excel</h2></strong></p>
<p>Ao executar o programa, a interface gráfica será exibida. Nela, você encontrará dois botões: "Carregar Arquivo 1" e "Carregar Arquivo 2". Clique em cada um deles para carregar os dois arquivos Excel que deseja unir.</p>
<p><strong><h2>Passo 2: Visualizando os dados dos arquivos carregados</h2></strong></p>
<p>Após carregar os arquivos, você poderá visualizar os dados contidos em cada planilha nas tabelas exibidas na interface. Isso ajudará você a selecionar as colunas corretas para realizar o join.</p>
<p><strong><h2>Passo 3: Selecionando as colunas de junção</h2></strong></p>
<p>Logo abaixo das tabelas, você encontrará duas opções de menu chamadas "Selecione a coluna do arquivo 1" e "Selecione a coluna do arquivo 2". Escolha a coluna que servirá como critério de junção para cada arquivo a partir desses menus.</p>
<p><strong><h2>Passo 4: Escolhendo o tipo de join</h2></strong></p>
<p>O próximo passo é selecionar o tipo de join que você deseja realizar entre os arquivos. No menu "Selecione o tipo de join", você encontrará opções como "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN" e outras. Escolha o tipo de join que melhor atenda às suas necessidades.</p>
<p><strong><h2>Passo 5: Iniciando o join</h2></strong></p>
<p>Após selecionar as colunas e o tipo de join, clique no botão "Iniciar Join" para realizar a operação. O programa executará o join entre os arquivos com base nas suas escolhas.</p>
<p><strong><h2>Passo 6: Resultados da junção</h2></strong></p>
<p>Uma nova janela intitulada "Resultado" será aberta, exibindo a planilha resultante da junção dos arquivos. Essa janela apresentará os dados combinados de acordo com o tipo de join selecionado.</p>
<p><strong><h2>Passo 7: Exportando os resultados (opcional)</h2></strong></p>
<p>Caso deseje salvar os resultados obtidos, você pode utilizar os recursos do Excel para exportar a tabela exibida na janela de resultados para um novo arquivo.</p>
<p><strong><h2>Passo 8: Fechando o programa</h2></strong></p>
<p>Após concluir a análise dos resultados ou salvar os dados em um novo arquivo, você pode fechar o programa clicando no botão de fechar ou saindo da aplicação normalmente.</p>
<p><strong>Observação:</strong></p>
<p>Lembramos que o JoinExcel requer a instalação do Python, do pacote pandas e da biblioteca PyQt5. Certifique-se de possuir essas dependências instaladas em seu ambiente antes de executar o programa.</p></br>
<p><h3>**Descrição e exemplos de uso do JoinExcel:**</h3></p>
<p><strong>O que é o JoinExcel?</strong></p>
<p>O JoinExcel é uma aplicação desenvolvida em Python com a biblioteca PyQt5, voltada para a realização de operações de junção (join) entre dois arquivos Excel. Essa ferramenta foi criada para facilitar a integração e análise de dados provenientes de diferentes fontes, permitindo combinar informações de planilhas distintas com base em critérios definidos pelo usuário.</p>
<p>**Exemplos de uso do JoinExcel:**</p>
<p><strong>Exemplo 1 - Inner Join:</strong></p>
<p>Suponha que você possua dois arquivos Excel contendo informações de funcionários de uma empresa. O primeiro arquivo (Arquivo1.xlsx) contém detalhes sobre os funcionários e seus respectivos setores, enquanto o segundo arquivo (Arquivo2.xlsx) possui informações sobre os salários e bônus concedidos a cada funcionário. Para combinar essas informações em uma única planilha, você pode seguir os passos abaixo:</p>
<p>1. Carregue os dois arquivos usando os botões "Carregar Arquivo 1" e "Carregar Arquivo 2".</p>
<p>2. Visualize os dados em cada tabela para identificar a coluna que servirá como critério de junção em ambos os arquivos.</p>
<p>3. Selecione a coluna "Setor" do "Arquivo1.xlsx" no menu "Selecione a coluna do arquivo 1" e a coluna "Nome" do "Arquivo2.xlsx" no menu "Selecione a coluna do arquivo 2".</p>
<p>4. Escolha a opção "INNER JOIN" no menu "Selecione o tipo de join".</p>
<p>5. Clique em "Iniciar Join" para realizar a operação.</p>
<p>6. A nova janela "Resultado" exibirá os dados combinados dos funcionários comuns a ambos os arquivos, ou seja, aqueles que possuem informações tanto no arquivo de detalhes quanto no arquivo de salários.</p>
<p><strong>Exemplo 2 - Left Join:</strong></p>
<p>Continuando o exemplo anterior, suponha que você deseje visualizar todos os funcionários do "Arquivo1.xlsx", mesmo aqueles que não possuem salário registrado no "Arquivo2.xlsx". Para isso, utilize o "Left Join":</p>
<p>1. Repita os passos 1 a 3 do exemplo anterior.</p>
<p>2. Escolha a opção "LEFT JOIN" no menu "Selecione o tipo de join".</p>
<p>3. Clique em "Iniciar Join" para realizar a operação.</p>
<p>4. A janela "Resultado" mostrará os dados combinados dos funcionários do "Arquivo1.xlsx" com seus respectivos salários, caso existam. Aqueles funcionários que não possuem informações de salário terão os campos correspondentes preenchidos com valores nulos.</p>
<p><strong>Exemplo 3 - Full Outer Join:</strong></p>
<p>Neste exemplo, você deseja obter uma lista completa de todos os funcionários de ambos os arquivos, independentemente de haver correspondência entre eles:</p>
<p>1. Repita os passos 1 a 3 do primeiro exemplo.</p>
<p>2. Escolha a opção "FULL OUTER JOIN" no menu "Selecione o tipo de join".</p>
<p>3. Clique em "Iniciar Join" para realizar a operação.</p>
<p>4. A janela "Resultado" exibirá todos os funcionários dos arquivos "Arquivo1.xlsx" e "Arquivo2.xlsx", preenchendo com valores nulos aqueles campos que não possuem informações em um dos arquivos.</p>
<p>Esses exemplos demonstram algumas das possibilidades de uso do JoinExcel para a combinação de dados em arquivos Excel, permitindo análises mais abrangentes e completas a partir de diferentes fontes de informações.</p>
