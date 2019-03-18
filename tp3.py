import socket
import psutil
import cpuinfo

info_memoria = psutil.virtual_memory()
info_cpu = psutil.cpu_percent(interval=1)
info_disco = psutil.disk_usage(".")
info_hostname = socket.gethostname()
info_rede = socket.gethostbyname(info_hostname)
disco_total = round(info_disco[0]/(1024 * 1024 * 1024))
disco_disponivel = round(info_disco[2]/(1024 * 1024 * 1024))
disco_uso_porcentagem = info_disco[3]

info = cpuinfo.get_cpu_info()['brand']
print("0 - sair\n"
      "1 - informações associadas ao processador\n"
      "2 - informações associadas à memória\n"
      "3 - informações associadas ao Disco\n"
      "4 - informações associadas ao IP\n"
      "5 - resumo dos dados\n")
while True:
      valor = int(input("digite a opção desejada: "))

      if valor == 1:
            print("=============================================")
            print(f'Cpu: {info}')
            print("=============================================\n")
      elif valor == 2:
            print("=============================================")
            print(f'Memoria: {info_memoria}%')
            print("=============================================\n")
      elif valor == 3:
            print("=============================================")
            print(f'Disco: {info_disco}%')
            print("=============================================\n")
      elif valor == 4:
            print(f'IP do computador: {info_rede}\n')
      elif valor == 5:
            print("=============================================")
            print(f'Uso da cpu: {info_cpu}%\n'
                  f'Cpu: {info}'
                  f'Uso de memoria: {info_memoria[2]}%\n'
                  f'Disco disponivel: {disco_disponivel}GB\n'
                  f'Disco total: {disco_total}GB\n'
                  f'Disco utilizado: {disco_uso_porcentagem}%\n'
                  f'IP do computador: {info_rede}')
            print("=============================================\n")
      elif valor == 0:
            break
      else:
            print("=============================================")
            print("erro opção invalida")
            print("============================================")