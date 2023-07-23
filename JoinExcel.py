import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QTableWidget, \
    QTableWidgetItem, QFileDialog, QMainWindow, QAction, QTabWidget
from PyQt5.QtGui import QFont, QIcon


class ResultadosJanela(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resultado")
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        self.setWindowIcon(QIcon("Raphael.png"))


    def adicionar_resultado(self, df):
        tabela = QTableWidget(len(df.index), len(df.columns))
        tabela.setHorizontalHeaderLabels(df.columns)
        for row_idx, row in df.iterrows():
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                tabela.setItem(row_idx, col_idx, item)
                font = QFont()
                font.setPointSize(8) 
                item.setFont(font)
        self.tab_widget.addTab(tabela, "Resultado")




class ExcelJoinApp(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JoinExcel")
        self.setWindowIcon(QIcon("Raphael.png"))
        self.resultados_janela = ResultadosJanela()
        self.file_path1 = "" 
        self.file_path2 = ""  
        self.init_ui()


    def init_ui(self):
        self.layout = QVBoxLayout()
        self.btn_arquivo1 = QPushButton("Carregar Arquivo 1")
        self.btn_arquivo1.clicked.connect(lambda: self.carregar_arquivo(1))
        self.layout.addWidget(self.btn_arquivo1)
        self.btn_arquivo2 = QPushButton("Carregar Arquivo 2")
        self.btn_arquivo2.clicked.connect(lambda: self.carregar_arquivo(2))
        self.layout.addWidget(self.btn_arquivo2)
        self.tabela1 = QTableWidget(5, 5)
        self.tabela2 = QTableWidget(5, 5)
        self.layout.addWidget(self.tabela1)
        self.layout.addWidget(self.tabela2)
        self.coluna1_label = QLabel("Selecione a coluna do arquivo 1:")
        self.coluna1_menu = QComboBox()
        self.coluna2_label = QLabel("Selecione a coluna do arquivo 2:")
        self.coluna2_menu = QComboBox()
        self.join_label = QLabel("Selecione o tipo de join:")
        self.join_menu = QComboBox()
        self.layout.addWidget(self.coluna1_label)
        self.layout.addWidget(self.coluna1_menu)
        self.layout.addWidget(self.coluna2_label)
        self.layout.addWidget(self.coluna2_menu)
        self.layout.addWidget(self.join_label)
        self.layout.addWidget(self.join_menu)
        joins_sql = ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN", "INNER JOIN USING", "LEFT JOIN USING",
                     "RIGHT JOIN USING", "FULL OUTER JOIN USING"]  
        self.join_menu.addItems(joins_sql)
        self.btn_iniciar = QPushButton("Iniciar Join")
        self.btn_iniciar.clicked.connect(self.realizar_join)
        self.layout.addWidget(self.btn_iniciar)
        self.setLayout(self.layout)
        
        
    def carregar_arquivo(self, arquivo_num):
        file_path, _ = QFileDialog.getOpenFileName(self, "Carregar Arquivo Excel", "", "Arquivos Excel (*.xlsx)")
        if file_path:
            if arquivo_num == 1:
                self.file_path1 = file_path 
                df = pd.read_excel(file_path)
                self.exibir_tabela(df, self.tabela1, self.coluna1_menu)
            elif arquivo_num == 2:
                self.file_path2 = file_path 
                df = pd.read_excel(file_path)
                self.exibir_tabela(df, self.tabela2, self.coluna2_menu)


    def exibir_tabela(self, df, tabela, coluna_menu):
        colunas = df.columns.tolist()
        coluna_menu.clear()
        coluna_menu.addItems(colunas)
        tabela.setColumnCount(len(colunas))
        tabela.setHorizontalHeaderLabels(colunas)
        tabela.setRowCount(0)
        for _, row in df.head(5).iterrows():
            row_data = [str(value) for value in row]
            row_position = tabela.rowCount()
            tabela.insertRow(row_position)
            for col_index, cell_value in enumerate(row_data):
                tabela.setItem(row_position, col_index, QTableWidgetItem(cell_value))


    def realizar_join(self):
        coluna1 = self.coluna1_menu.currentText()
        coluna2 = self.coluna2_menu.currentText()
        join_type = self.join_menu.currentText()
        df1 = pd.read_excel(self.file_path1)
        df2 = pd.read_excel(self.file_path2)
        if join_type == "INNER JOIN":
            df_resultado = pd.merge(df1, df2, left_on=coluna1, right_on=coluna2, how='inner')
        elif join_type == "LEFT JOIN":
            df_resultado = pd.merge(df1, df2, left_on=coluna1, right_on=coluna2, how='left')
        elif join_type == "RIGHT JOIN":
            df_resultado = pd.merge(df1, df2, left_on=coluna1, right_on=coluna2, how='right')
        elif join_type == "FULL OUTER JOIN":
            df_resultado = pd.merge(df1, df2, left_on=coluna1, right_on=coluna2, how='outer')
        elif join_type == "INNER JOIN USING":
            df_resultado = pd.merge(df1, df2, on=coluna1, how='inner')
        elif join_type == "LEFT JOIN USING":
            df_resultado = pd.merge(df1, df2, on=coluna1, how='left')
        elif join_type == "RIGHT JOIN USING":
            df_resultado = pd.merge(df1, df2, on=coluna1, how='right')
        elif join_type == "FULL OUTER JOIN USING":
            df_resultado = pd.merge(df1, df2, on=coluna1, how='outer')
        else:
            return
        self.resultados_janela.adicionar_resultado(df_resultado)
        self.resultados_janela.setGeometry(self.x() + self.width() + 5, self.y() + 30, 700, self.height())  
        self.resultados_janela.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExcelJoinApp()
    window.show()
    sys.exit(app.exec_())