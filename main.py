import sqlite3
import cv2
import time

# biblioteca de leitura
import zxingcpp

def ler_codigo(frame):
    for resultado in zxingcpp.read_barcodes(frame):
        if resultado.text:
            return resultado.text
    return None


# leitor do código de barras
def leitor():
    cap = cv2.VideoCapture(0)
    print("Aponte o código de barras para a câmera (ESC cancela)")

    try:
        while True:
            sucesso, frame = cap.read()
            if not sucesso:
                print("Erro ao acessar a câmera.")
                return None

            texto_codigo = ler_codigo(frame)
            if texto_codigo:
                print(f"Código lido com sucesso: {texto_codigo}")
                return texto_codigo

            cv2.imshow("Leitor de Codigo de Barras", frame)

            if cv2.waitKey(1) & 0xFF == 27:  # ESC
                return None
    finally:
        cap.release()
        cv2.destroyAllWindows()


# identificador de informações do pacote
def identificador(cursor, texto_codigo):
    cursor.execute(
        "SELECT * FROM pacotes WHERE codigo_barras = ?",
        (texto_codigo,),
    )
    return cursor.fetchone()



#selecionador de rota
def rota(pacote):
    if pacote is None:
        print("Pacote não encontrado. Revise as informações.")
    elif pacote[3] == 1:
        print("Pacote:", pacote[0], "Frágil: Sim")
        print("Destino: ÁREA DE FRÁGEIS")
        print("Simulação: Pacote encaminhado")
    elif pacote[2] == "grande" or pacote[1] > 5:
        print("Pacote:", pacote[0], "Frágil: Não")
        print("Destino: ÁREA DE CARGAS")
        print("Simulação: Pacote encaminhado")
    else:
        print("Pacote:", pacote[0], "Frágil: Não")
        print("Destino: ÁREA DE COMUNS")
        print("Simulação: Pacote encaminhado")


# programa principal
def main():
    conexao = sqlite3.connect("database.db")
    try:
        cursor = conexao.cursor()

        while True:
            texto = leitor()

            if texto is None:  # ESC ou erro de câmera
                print("Leitura encerrada.")
                break

            rota(identificador(cursor, texto))
            print("-" * 30)
            time.sleep(3)  # tempo para tirar o pacote da frente da câmera
    finally:
        conexao.close()

if __name__ == "__main__":
    main()
