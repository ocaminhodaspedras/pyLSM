import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QSlider, QGroupBox, QFormLayout, 
                             QPushButton, QMessageBox)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PyLSMEducacional(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyLSM - Explorador Didático do Modelo de Deformação de Rede")
        self.resize(900, 600)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout_principal = QHBoxLayout(main_widget)
        
        # --- Painel Lateral (Controles) ---
        painel_controles = QVBoxLayout()
        grupo_sliders = QGroupBox("Parâmetros Termodinâmicos e Elásticos")
        form_layout = QFormLayout()
        
        # 1. Slider D0 (Escala Logarítmica: 10^-4 a 10^1)
        self.sl_d0 = QSlider(Qt.Horizontal)
        self.sl_d0.setRange(-400, 100) 
        self.sl_d0.setValue(0) # 10^0 = 1.0
        self.lbl_d0 = QLabel()
        
        # 2. Slider E_N (Módulo de Young: 50 a 800 GPa)
        self.sl_en = QSlider(Qt.Horizontal)
        self.sl_en.setRange(50, 800)
        self.sl_en.setValue(250)
        self.lbl_en = QLabel()
        
        # 3. Slider r0 (Raio ideal: 0.50 a 1.50 Å)
        self.sl_r0 = QSlider(Qt.Horizontal)
        self.sl_r0.setRange(50, 150)
        self.sl_r0.setValue(100) # 1.0 Å
        self.lbl_r0 = QLabel()
        
        # 4. Slider T (Temperatura: 600 a 2000 K)
        self.sl_t = QSlider(Qt.Horizontal)
        self.sl_t.setRange(600, 2000)
        self.sl_t.setValue(1300)
        self.lbl_t = QLabel()

        # Conectando sliders à função de atualização
        sliders = [self.sl_d0, self.sl_en, self.sl_r0, self.sl_t]
        for sl in sliders:
            sl.valueChanged.connect(self.atualizar_grafico)

        # Adicionando ao formulário
        form_layout.addRow("D0 (Partição Ideal):", self.lbl_d0)
        form_layout.addRow(self.sl_d0)
        form_layout.addRow("E_N (Módulo de Young):", self.lbl_en)
        form_layout.addRow(self.sl_en)
        form_layout.addRow("r0 (Raio Ideal):", self.lbl_r0)
        form_layout.addRow(self.sl_r0)
        form_layout.addRow("T (Temperatura):", self.lbl_t)
        form_layout.addRow(self.sl_t)
        
        grupo_sliders.setLayout(form_layout)
        painel_controles.addWidget(grupo_sliders)
        
        # Bloco de texto explicativo para guiar os alunos
        texto_didatico = QLabel(
            "<b>Guia Rápido:</b><br>"
            "- <b>E_N alto:</b> Mineral rígido, parábola estreita.<br>"
            "- <b>T alta:</b> Mineral dilatado, parábola relaxa/alarga.<br>"
            "- <b>r0:</b> Desloca o pico para cátions maiores ou menores.<br>"
            "- <b>D0:</b> Move a parábola inteira verticalmente."
        )
        texto_didatico.setWordWrap(True)
        texto_didatico.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 5px;")
        painel_controles.addWidget(texto_didatico)
        
        # --- Botão de Referências ---
        btn_referencias = QPushButton("Referências Bibliográficas")
        btn_referencias.setCursor(Qt.PointingHandCursor)
        btn_referencias.setStyleSheet("padding: 8px; font-weight: bold; background-color: #e0e0e0; border-radius: 4px;")
        btn_referencias.clicked.connect(self.mostrar_referencias)
        painel_controles.addWidget(btn_referencias)
        
        painel_controles.addStretch()
        
        # --- Assinatura Institucional ---
        lbl_creditos = QLabel("<small>Desenvolvido por Felipe P. Leitzke<br>Mineralogia / UFRGS</small>")
        lbl_creditos.setAlignment(Qt.AlignCenter)
        lbl_creditos.setStyleSheet("color: #555555;")
        painel_controles.addWidget(lbl_creditos)
        
        # --- Área do Gráfico (Matplotlib) ---
        self.figura = Figure(figsize=(6, 5), dpi=100)
        self.canvas = FigureCanvas(self.figura)
        self.ax = self.figura.add_subplot(111)
        
        layout_principal.addLayout(painel_controles, 1)
        layout_principal.addWidget(self.canvas, 3)
        
        self.atualizar_grafico() # Plot inicial
        
    def mostrar_referencias(self):
        texto = (
            "<h3>Fundamentação Teórica - Lattice Strain Model</h3>"
            "<p>A equação termodinâmica de partição utilizada para o cálculo do trabalho elástico "
            "de expansão/contração da rede cristalina embasa-se rigorosamente na literatura abaixo:</p>"
            "<p><b>1. Balanço Termodinâmico de Cristais Tensionados:</b><br>"
            "Brice, J. C. (1975). Some thermodynamic aspects of the growth of strained crystals. "
            "<i>Journal of Crystal Growth</i>, 28(2), 249-253.</p>"
            "<p><b>2. Aplicação à Partição Cristal-Líquido Silicático:</b><br>"
            "Blundy, J., & Wood, B. (1994). Prediction of crystal-melt partition coefficients "
            "from elastic moduli. <i>Nature</i>, 372(6505), 452-454.</p>"
        )
        caixa_msg = QMessageBox(self)
        caixa_msg.setWindowTitle("Referências Bibliográficas")
        caixa_msg.setText(texto)
        caixa_msg.setIcon(QMessageBox.Information)
        caixa_msg.exec_()
        
    def atualizar_grafico(self):
        D0 = 10 ** (self.sl_d0.value() / 100.0)
        E_N = float(self.sl_en.value())
        r0 = self.sl_r0.value() / 100.0
        T = float(self.sl_t.value())
        
        self.lbl_d0.setText(f"{D0:.4f}")
        self.lbl_en.setText(f"{E_N:.0f} GPa")
        self.lbl_r0.setText(f"{r0:.2f} Å")
        self.lbl_t.setText(f"{T:.0f} K")
        
        r_i = np.linspace(0.5, 1.6, 200)
        N_A = 6.02214076e23
        R = 8.314462618
        
        E_N_Pa = E_N * 1e9
        r_i_m = r_i * 1e-10
        r0_m = r0 * 1e-10
        
        term1 = (r0_m / 2.0) * (r_i_m - r0_m)**2
        term2 = (1.0 / 3.0) * (r_i_m - r0_m)**3
        W_site = 4 * np.pi * E_N_Pa * (term1 + term2)
        
        exponent = -(W_site * N_A) / (R * T)
        Di = D0 * np.exp(exponent)
        
        self.ax.clear()
        self.ax.plot(r_i, Di, color='#003366', linewidth=2.5)
        self.ax.axvline(x=r0, color='red', linestyle='--', alpha=0.7, label=f'r0 = {r0:.2f} Å')
        
        self.ax.set_yscale('log')
        self.ax.set_ylim(1e-4, 1e1)
        self.ax.set_xlim(0.5, 1.6)
        
        self.ax.set_xlabel("Raio Iônico $r_i$ (Å)", fontsize=11)
        self.ax.set_ylabel("Coeficiente de Partição $D_i$", fontsize=11)
        self.ax.set_title(f"Isoterma {T:.0f} K", fontsize=13)
        self.ax.grid(True, which="both", linestyle=":", alpha=0.6)
        self.ax.legend()
        
        self.figura.tight_layout()
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = PyLSMEducacional()
    janela.show()
    sys.exit(app.exec_())
